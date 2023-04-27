from dataclasses import dataclass
from enum import Enum


class Colour(Enum):
    WHITE = 0
    BLACK = 1

    def __invert__(self):
        if self == self.WHITE:
            return self.BLACK
        else:
            return self.WHITE


@dataclass
class Pos:
    x: int
    y: int

    @staticmethod
    def from_str(pos: str) -> 'Pos':
        from board.parse import parse_coord
        coord = parse_coord(pos)

        return coord


class MoveNotImplemented(Exception):
    pass


class InvalidMove(Exception):
    pass


class Piece:
    LETTER: str
    colour: Colour
    pos: Pos

    def __init__(self, colour: Colour, pos: Pos):
        self.colour = colour
        self.pos = pos

    def letter(self):
        if self.colour == Colour.WHITE:
            return self.LETTER.upper()
        elif self.colour == Colour.BLACK:
            return self.LETTER.lower()

    def verify_move(self, pos: Pos, other_piece) -> bool:
        raise MoveNotImplemented


class Move:
    start: Pos
    end: Pos


def create_board_grid() -> [Piece]:
    from pieces.bishop import Bishop
    from pieces.king import King
    from pieces.knight import Knight
    from pieces.pawn import Pawn
    from pieces.queen import Queen
    from pieces.rook import Rook

    return [
        # 1
        Rook(Colour.WHITE, Pos(0, 0)), Knight(Colour.WHITE, Pos(1, 0)), Bishop(Colour.WHITE, Pos(2, 0)),
        Queen(Colour.WHITE, Pos(3, 0)), King(Colour.WHITE, Pos(4, 0)), Bishop(Colour.WHITE, Pos(5, 0)),
        Knight(Colour.WHITE, Pos(6, 0)), Rook(Colour.WHITE, Pos(7, 0)),
        # 2
        Pawn(Colour.WHITE, Pos(0, 1)), Pawn(Colour.WHITE, Pos(1, 1)), Pawn(Colour.WHITE, Pos(2, 1)),
        Pawn(Colour.WHITE, Pos(3, 1)), Pawn(Colour.WHITE, Pos(4, 1)), Pawn(Colour.WHITE, Pos(5, 1)),
        Pawn(Colour.WHITE, Pos(6, 1)), Pawn(Colour.WHITE, Pos(7, 1)),
        # 3
        None, None, None, None, None, None, None, None,
        # 4
        None, None, None, None, None, None, None, None,
        # 5
        None, None, None, None, None, None, None, None,
        # 6
        None, None, None, None, None, None, None, None,
        # 7
        Pawn(Colour.BLACK, Pos(0, 6)), Pawn(Colour.BLACK, Pos(1, 6)), Pawn(Colour.BLACK, Pos(2, 6)),
        Pawn(Colour.BLACK, Pos(3, 6)), Pawn(Colour.BLACK, Pos(4, 6)), Pawn(Colour.BLACK, Pos(5, 6)),
        Pawn(Colour.BLACK, Pos(6, 6)), Pawn(Colour.BLACK, Pos(7, 6)),
        # 8
        Rook(Colour.BLACK, Pos(0, 7)), Knight(Colour.BLACK, Pos(1, 7)), Bishop(Colour.BLACK, Pos(2, 7)),
        Queen(Colour.BLACK, Pos(3, 7)), King(Colour.BLACK, Pos(4, 7)), Bishop(Colour.BLACK, Pos(5, 7)),
        Knight(Colour.BLACK, Pos(6, 7)), Rook(Colour.BLACK, Pos(7, 7)),
    ]
