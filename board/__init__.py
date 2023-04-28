import os
from dataclasses import dataclass
from enum import Enum

from pieces import Piece, create_board_grid, Pos, InvalidMove, Colour, Move


class WrongTurn(Exception):
    pass


class Blocked(Exception):
    pass


class GameState(Enum):
    RUNNING = 0
    DRAW = 1
    WIN_WHITE = 2
    WIN_BLACK = 3


class Draw(Exception):
    pass


@dataclass
class Victory(Exception):
    colour: Colour


class Board:
    """ Represents a chess board.

        grid: the array of pieces. Pieces are stored in order from bottom left and rightward for each column
        and upward for each row. (a1 -> h1...a8->h8). `None` represents an empty square
    """
    grid: [Piece | None]
    turn: Colour
    half_moves: [Move]
    move_number: int
    half_move_count_50_rule: int
    en_passent_target: Pos | None
    game_state: GameState

    def __init__(self, fen=None):
        if fen is None:
            self.grid = create_board_grid()
            self.turn = Colour.WHITE
            self.half_moves = []
            self.move_number = 1
            self.half_move_count_50_rule = 0
            self.en_passent_target = None
        else:
            from board.parse import parse_fen
            board = parse_fen(fen)
            self.grid = board.grid
            self.turn = board.turn
            self.half_moves = board.half_moves
            self.move_number = board.move_number
            self.half_move_count_50_rule = board.half_move_count_50_rule
            self.en_passent_target = board.en_passent_target
        self.game_state = GameState.RUNNING

    def __str__(self):
        string = ""
        for i in range(7, -1, -1):
            for j in range(8):
                piece = self.grid[i * 8 + j]
                string += (piece.letter() if piece is not None else "-") + " "
            string += os.linesep
        string += f"{self.turn.name.lower()}'s turn{os.linesep}"
        return string

    def __getitem__(self, pos: Pos):
        return self.grid[pos.y * 8 + pos.x]

    def __setitem__(self, pos: Pos, piece: Piece | None):
        self.grid[pos.y * 8 + pos.x] = piece

    def __delitem__(self, pos: Pos):
        self.grid[pos.y * 8 + pos.x] = None

    def move(self, pre: str, new: str):
        """
        Make a move. Throws an exception if the move is invalid
        e.g.: board.move('e2', 'e4')
        :param pre: coordinate to move from
        :param new: coordinate to move to
        """
        pre = Pos.from_str(pre)
        new = Pos.from_str(new)
        self.move_coord(pre, new)

    def move_coord(self, pre: Pos, new: Pos):
        """
        Move a piece on the board
        :param pre: the square to move a piece from
        :param new: the square to move the piece to

        new - pre: positive is right and up, negative left and down (from white's perspective)

        if pre.x < new.x the piece moved right (towards h file)
        if pre.x > new.x the piece moved left (towards a file)
        if pre.y < new.y the piece moved up the board (towards the 8th rank)
        if pre.y > new.y the piece moved down the board (towards the 1st rank)
        """
        if self.game_state == GameState.DRAW:
            raise Draw()
        elif self.game_state == GameState.WIN_WHITE:
            raise Victory(Colour.WHITE)
        elif self.game_state == GameState.WIN_BLACK:
            raise Victory(Colour.BLACK)

        # check if squares are in bounds
        board_range = range(0, 8)
        if pre.x not in board_range or pre.y not in board_range or new.x not in board_range or new.y not in board_range:
            raise InvalidMove()

        # check if valid move
        # the check if the other square has the same colour as the starting piece prevents a piece
        # from moving zero squares since it will try to move onto itself
        if (self[pre] is None) or (self[new] is not None and self[new].colour == self[pre].colour) or (
                not self[pre].verify_move(new, self[new])):
            raise InvalidMove()
        if self[pre].colour != self.turn:
            raise WrongTurn()

        # only if there's not a knight
        if self[pre].LETTER != 'n':
            # squares_between will also verify the piece moves properly in the diagonal direction (if applicable)
            intermediate = squares_between(pre, new)
            for square in intermediate:
                if self[square] is not None:
                    raise Blocked()

        # TODO: see if there's a check on the king

        # TODO: king castling

        # TODO: en passant

        # TODO: fifty move rule

        # TODO: three move repetition

        if self[pre].LETTER == 'k':
            self[pre].can_queen_castle = False
            self[pre].can_king_castle = False
        if self[pre].LETTER == 'p':
            self[pre].has_moved = True
            # reset 50 move rule, set to -1 because we increment it next
            self.half_move_count_50_rule = -1
            if abs(new.y - pre.y) == 2:
                pos = Pos(new.x, new.y - 1 if self.turn == Colour.WHITE else new.y + 1)
                self.en_passent_target = pos
            else:
                self.en_passent_target = None
        else:
            self.en_passent_target = None
        self.half_move_count_50_rule += 1
        # if black just moved, that means we're onto a new move
        if self.turn == Colour.BLACK:
            self.move_number += 1
        self.half_moves.append(Move(pre, new))
        self[pre].pos = new
        self[new] = self[pre]
        self[pre] = None
        self.turn = ~self.turn

        # TODO: check for checkmate

        # TODO: check for draw


def squares_between(pre: Pos, new: Pos) -> [Pos]:
    """
    Find each square in between the two squares
    :param pre: from square
    :param new: to square
    :return: list of each square in between the two points
    """
    delta_x = new.x - pre.x
    delta_y = new.y - pre.y

    # moving diagonally
    if abs(delta_x) > 0 and abs(delta_y) > 0:
        # for every normal move x and y should be the same (excluding horses - but they don't worry about collisions)
        if abs(delta_x) != abs(delta_y):
            raise InvalidMove()

        # each x between the two squares, and each y between the two squares

        # these are the ranges from the x and y specific movements
        x_range = range(pre.x + 1, new.x) if delta_x > 0 else range(pre.x - 1, new.x, -1)
        y_range = range(pre.y + 1, new.y) if delta_y > 0 else range(pre.y - 1, new.y, -1)

        arr = []
        for (x, y) in zip(x_range, y_range):
            arr.append(Pos(x, y))
        return arr

    # move in the x direction
    if abs(delta_x) > 0:
        # delta_x = 2 ---- pre.x = 0 ---- new.x = 2
        # between.x = [1] or from pre.x + 1 to new.x
        # delta_x = -3 --- pre.x = 4 ---- new.x = 1
        # between.x = [3, 2] or from pre.x - 1 to new.x
        arr = []
        if delta_x > 0:
            for i in range(pre.x + 1, new.x):
                arr.append(Pos(i, new.y))
        else:
            for i in range(pre.x - 1, new.x, -1):
                arr.append(Pos(i, new.y))
        return arr

    # move in the y direction
    if abs(delta_y) > 0:
        # same as x direction but in the y
        arr = []
        if delta_y > 0:
            for i in range(pre.y + 1, new.y):
                arr.append(Pos(new.x, i))
        else:
            for i in range(pre.y - 1, new.y, -1):
                arr.append(Pos(new.x, i))
        return arr

    return []
