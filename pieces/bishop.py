from pieces import Piece, Pos, Colour


class Bishop(Piece):
    LETTER = 'b'

    def __init__(self, colour: Colour, pos: Pos):
        super().__init__(colour, pos)

    def verify_move(self, pos: Pos, other_piece) -> bool:
        # check for correct direction
        delta_x, delta_y = pos.x - self.pos.x, pos.y - self.pos.y

        # the piece must move diagonally
        if delta_x == 0 or delta_y == 0:
            return False
        return True
