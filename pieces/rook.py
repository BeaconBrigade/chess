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

    def valid_moves(self) -> [Pos]:
        moves = []

        left_range = range(self.pos.x - 1, -1, -1)
        right_range = range(self.pos.x + 1, 8)
        up_range = range(self.pos.y + 1, 8)
        down_range = range(self.pos.y - 1, -1, -1)

        for x in left_range:
            moves.append(Pos(x, self.pos.y))
        for x in right_range:
            moves.append(Pos(x, self.pos.y))
        for y in up_range:
            moves.append(Pos(self.pos.x, y))
        for y in down_range:
            moves.append(Pos(self.pos.x, y))

        return moves

    def __str__(self):
        return f'Rook(pos={self.pos}, colour={self.colour})'
