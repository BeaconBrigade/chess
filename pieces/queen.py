from pieces import Piece, Pos, Colour


class Queen(Piece):
    LETTER = 'q'

    def __init__(self, colour: Colour, pos: Pos):
        super().__init__(colour, pos)

    def move(self, pos: Pos):
        # check for correct direction
        pass
