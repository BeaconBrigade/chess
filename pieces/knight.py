from pieces import Piece, Pos, Colour


class Knight(Piece):
    LETTER = 'n'

    def __init__(self, colour: Colour, pos: Pos):
        super().__init__(colour, pos)

    def verify_move(self, pos: Pos, other_piece) -> bool:
        delta_x, delta_y = pos.x - self.pos.x, pos.y - self.pos.y

        # horse must move 1 or 2 in both x and y
        if (abs(delta_x) != 1 and abs(delta_x) != 2) or (abs(delta_y) != 1 and abs(delta_y) != 2):
            return False

        # horse moves two in one direction, one in the other
        if abs(delta_x) == 1 and abs(delta_y) != 2:
            return False
        if abs(delta_x) == 2 and abs(delta_y) != 1:
            return False

        return True

    def __str__(self):
        return f'Knight(pos={self.pos}, colour={self.colour})'
