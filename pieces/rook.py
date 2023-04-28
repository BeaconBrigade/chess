from pieces import Piece, Pos, Colour


class Rook(Piece):
    LETTER = 'r'

    def __init__(self, colour: Colour, pos: Pos):
        super().__init__(colour, pos)

    def verify_move(self, pos: Pos, other_piece) -> bool:
        delta_x, delta_y = pos.x - self.pos.x, pos.y - self.pos.y

        # can't move diagonally
        if delta_x != 0 and delta_y != 0:
            return False
        return True

    def __str__(self):
        return f'Rook(pos={self.pos}, colour={self.colour})'
