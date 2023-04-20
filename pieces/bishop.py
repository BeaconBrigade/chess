from pieces import Piece, Pos, Colour


class Bishop(Piece):
    LETTER = 'b'

    def __init__(self, colour: Colour, pos: Pos):
        super().__init__(colour, pos)

    def move(self, pos: Pos):
        # check for correct direction
        pass
