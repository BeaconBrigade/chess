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

    def valid_moves(self) -> [Pos]:
        moves = []
        left_range = range(self.pos.x - 1, -1, -1)
        right_range = range(self.pos.x + 1, 8)
        up_range = range(self.pos.y + 1, 8)
        down_range = range(self.pos.y - 1, -1, -1)

        for (x, y) in zip(left_range, up_range):
            moves.append(Pos(x, y))
        for (x, y) in zip(left_range, down_range):
            moves.append(Pos(x, y))
        for (x, y) in zip(right_range, up_range):
            moves.append(Pos(x, y))
        for (x, y) in zip(right_range, down_range):
            moves.append(Pos(x, y))

        return moves

    def __str__(self):
        return f'Bishop(pos={self.pos}, colour={self.colour})'
