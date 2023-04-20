from pieces import Piece, Pos, Colour


class Pawn(Piece):
    LETTER = 'p'
    has_moved: bool

    def __init__(self, colour: Colour, pos: Pos):
        super().__init__(colour, pos)
        self.has_moved = False

    def move(self, to: Pos):
        # check for correct direction
        delta_x, delta_y = abs(self.pos.x - to.x), abs(self.pos.y - to.y)

