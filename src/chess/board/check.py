from ..board import Board, squares_between, Blocked
from ..pieces import Colour, Pos, Piece, InvalidMove


class KingIsMissing(Exception):
    pass


def king_in_check(board: Board, colour: Colour) -> bool:
    """
    Check if the king of a certain colour is in check. Will throw if the
    king does not exist.
    :param board: The board itself
    :param colour: The colour of the king to check for
    :return: True if the king is in check, False otherwise
    """
    # find king
    king = None
    for square in board.grid:
        if square is None:
            continue
        if square.LETTER == 'k' and square.colour == colour:
            king = square
            break
    if king is None:
        raise KingIsMissing()

    # look through every piece on the board
    for piece in board.grid:
        # skip blanks and our own pieces
        if piece is None or piece.colour == colour:
            continue
        # look through every move that piece has
        moves = piece.valid_moves()
        for move in moves:
            # skip moves that don't land on the king
            if move != king.pos:
                continue
            # make sure the piece has line of sight
            if piece.LETTER != 'n':
                if move_can_reach(board, piece, move):
                    return True
            # knights can always reach
            else:
                return True

    return False


def is_in_checkmate(board: Board, colour: Colour) -> bool:
    """
    Check if a certain colour is in checkmate
    :param board: The board
    :param colour: The colour
    :return: Whether the colour is checkmated
    """
    if not king_in_check(board, colour):
        return False

    def cb():
        if king_in_check(board, colour):
            return False
        return True
    # use a for i in range loop because, apply_remove_move mutates the original
    # value in board.grid and replaces it with a new one. The for loop isn't aware
    # so after the first potential move, the iterator variable references an out of
    # date piece. By only using indexes we always have the up-to-date value.
    for i in range(len(board.grid)):
        if board.grid[i] is None or board.grid[i].colour != colour:
            continue
        moves = board.grid[i].valid_moves()
        for move in moves:
            try:
                blocks = board.apply_remove_move(board.grid[i].pos, move, cb)
            except InvalidMove:
                continue
            except Blocked:
                continue
            if blocks:
                return False

    return True


def move_can_reach(board: Board, piece: Piece, move: Pos) -> bool:
    between = squares_between(piece.pos, move)
    for square in between:
        if board[square] is not None:
            return False
    return True
