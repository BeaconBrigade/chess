from board import Board, squares_between
from pieces import Colour, Pos, Piece


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


def move_can_reach(board: Board, piece: Piece, move: Pos) -> bool:
    between = squares_between(piece.pos, move)
    for square in between:
        if board[square] is not None:
            return False
    return True
