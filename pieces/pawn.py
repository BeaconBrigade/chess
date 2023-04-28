from pieces import Piece, Pos, Colour


class Pawn(Piece):
    LETTER = 'p'
    has_moved: bool

    def __init__(self, colour: Colour, pos: Pos):
        super().__init__(colour, pos)
        self.has_moved = False

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

        return True
