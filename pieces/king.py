from pieces import Piece, Pos, Colour


class King(Piece):
    LETTER = 'k'
    can_king_castle: bool
    can_queen_castle: bool

    def __init__(self, colour: Colour, pos: Pos):
        super().__init__(colour, pos)
        self.can_king_castle = True
        self.can_queen_castle = True

    def verify_move(self, pos: Pos, other_piece) -> bool:
        # check for correct direction
        delta_x, delta_y = pos.x - self.pos.x, pos.y - self.pos.y

        # can only move one square at a time
        if (abs(delta_x) != 0 and abs(delta_x) != 1) or (abs(delta_y) != 0 and abs(delta_y) != 1):
            return False
        return True
