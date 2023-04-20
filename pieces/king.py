from pieces import Piece, Pos, Colour


class King(Piece):
    LETTER = 'k'
    king_castle: bool
    queen_castle: bool

    def __init__(self, colour: Colour, pos: Pos):
        super().__init__(colour, pos)
        self.king_castle = False
        self.queen_castle = False

    def move(self, pos: Pos):
        # check for correct direction
        pass
