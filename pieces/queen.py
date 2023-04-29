from pieces import Piece, Pos, Colour


class Queen(Piece):
    LETTER = 'q'

    def __init__(self, colour: Colour, pos: Pos):
        super().__init__(colour, pos)

    def verify_move(self, pos: Pos, other_piece) -> bool:
        # check for correct direction
        return True

    def valid_moves(self) -> [Pos]:
        moves = []

        left_range = range(self.pos.x - 1, -1, -1)
        right_range = range(self.pos.x + 1, 8)
        up_range = range(self.pos.y + 1, 8)
        down_range = range(self.pos.y - 1, -1, -1)

        # diagonals
        for (x, y) in zip(left_range, up_range):
            moves.append(Pos(x, y))
        for (x, y) in zip(left_range, down_range):
            moves.append(Pos(x, y))
        for (x, y) in zip(right_range, up_range):
            moves.append(Pos(x, y))
        for (x, y) in zip(right_range, down_range):
            moves.append(Pos(x, y))

        # straight
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
        return f'Queen(pos={self.pos}, colour={self.colour})'
