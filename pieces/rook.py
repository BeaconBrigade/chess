from pieces import Piece, Pos, Colour


class Rook(Piece):
    LETTER = 'r'

    def __init__(self, colour: Colour, pos: Pos):
        super().__init__(colour, pos)

    def verify_move(self, pos: Pos, other_piece) -> bool:
        # check for correct direction
        return True
