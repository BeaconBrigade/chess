import os

from pieces import Piece, create_board_grid, Pos, InvalidMove, Colour


class WrongTurn(Exception):
    pass


class Board:
    """ Represents a chess board.

        grid: the array of pieces. Pieces are stored in order from bottom left and rightward for each column
        and upward for each row. (a1 -> h1...a8->h8). `None` represents an empty square
    """
    grid: [Piece | None]
    turn: Colour

    def __init__(self):
        self.grid = create_board_grid()
        self.turn = Colour.WHITE

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

    def move(self, pre: Pos, new: Pos):
        """ Move a piece on the board
        pre: the square to move a piece from
        new: the square to move the piece to

        new - pre: positive is right and up, negative left and down (from white's perspective)

        if pre.x < new.x the piece moved right (towards h file)
        if pre.x > new.x the piece moved left (towards a file)
        if pre.y < new.y the piece moved up the board (towards the 8th rank)
        if pre.y > new.y the piece moved down the board (towards the 1st rank)
        """
        # check if valid

        if (self[pre] is None) or (self[new] is not None and self[new].colour == self[pre].colour) or (
                                                                            not self[pre].verify_move(new, self[new])):
            raise InvalidMove()
        if self[pre].colour != self.turn:
            raise WrongTurn()

        # TODO: see if there's a collision

        # TODO: see if there's a check on the king

        # TODO: king castling

        # TODO: en passant

        self[new] = self[pre]
        self[pre] = None
        self.turn = ~self.turn
