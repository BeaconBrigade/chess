from . import Piece, Pos, Colour


class Pawn(Piece):
    LETTER = 'p'
    has_moved: bool

    def __init__(self, colour: Colour, pos: Pos):
        super().__init__(colour, pos)
        if (self.colour == Colour.WHITE and pos.y == 1) or (self.colour == Colour.BLACK and pos.y == 6):
            self.has_moved = False
        else:
            self.has_moved = True

    def verify_move(self, pos: Pos, other_piece: Piece) -> bool:
        # check for correct direction
        delta_x, delta_y = pos.x - self.pos.x, pos.y - self.pos.y

        # piece is going wrong direction
        if self.colour == Colour.WHITE and delta_y < 0:
            return False
        elif self.colour == Colour.BLACK and delta_y > 0:
            return False

        # we can only move by 1 in the x direction
        if abs(delta_x) != 0 and abs(delta_x) != 1:
            return False

        # we can only move by one or two in the y direction
        if abs(delta_y) != 1 and abs(delta_y) != 2:
            return False

        # can't jump by two and capture
        if abs(delta_y) == 2 and abs(delta_x) == 1:
            return False

        # can't move by two squares multiple times
        if abs(delta_y) == 2 and self.has_moved:
            return False

        # can't capture without moving horizontally
        if other_piece is not None and abs(delta_x) == 0:
            return False

        # can only move horizontally if other square has a piece
        if abs(delta_x) != 0 and other_piece is None:
            return False

        return True

    def valid_moves(self) -> [Pos]:
        moves = []
        direction = 1 if self.colour == Colour.WHITE else -1

        moves.append(Pos(self.pos.x, self.pos.y + 1 * direction))
        if not self.has_moved:
            moves.append(Pos(self.pos.x, self.pos.y + 2 * direction))
        if self.pos.x > 0:
            moves.append(Pos(self.pos.x - 1, self.pos.y + 1 * direction))
        if self.pos.x < 7:
            moves.append(Pos(self.pos.x + 1, self.pos.y + 1 * direction))

        return moves

    def __eq__(self, other: Piece) -> bool:
        if not super().__eq__(other):
            return False
        if self.has_moved != other.has_moved:
            return False
        return True

    def __str__(self):
        return f'Pawn(pos={self.pos}, has_moved={self.has_moved} colour={self.colour})'
