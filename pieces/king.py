from pieces import Piece, Pos, Colour


class King(Piece):
    LETTER = 'k'
    can_king_castle: bool
    can_queen_castle: bool

    def __init__(self, colour: Colour, pos: Pos, king_castle=True, queen_castle=True):
        super().__init__(colour, pos)
        self.can_king_castle = king_castle
        self.can_queen_castle = queen_castle

    def verify_move(self, pos: Pos, other_piece) -> bool:
        # check for correct direction
        delta_x, delta_y = pos.x - self.pos.x, pos.y - self.pos.y

        # can only move one square at a time
        if (abs(delta_x) != 0 and abs(delta_x) != 1) or (abs(delta_y) != 0 and abs(delta_y) != 1):
            return False
        return True

    def valid_moves(self) -> [Pos]:
        moves = []
        if self.pos.x > 0:
            moves.append(Pos(self.pos.x - 1, self.pos.y))
            if self.pos.y > 0:
                moves.append(Pos(self.pos.x - 1, self.pos.y - 1))
            if self.pos.y < 7:
                moves.append(Pos(self.pos.x - 1, self.pos.y + 1))
        if self.pos.x < 7:
            moves.append(Pos(self.pos.x + 1, self.pos.y))
            if self.pos.y > 0:
                moves.append(Pos(self.pos.x + 1, self.pos.y - 1))
            if self.pos.y < 7:
                moves.append(Pos(self.pos.x + 1, self.pos.y + 1))
        if self.pos.y > 0:
            moves.append(Pos(self.pos.x, self.pos.y - 1))
        if self.pos.y < 7:
            moves.append(Pos(self.pos.x, self.pos.y + 1))

        return moves

    def __eq__(self, other: Piece) -> bool:
        if not super().__eq__(other):
            return False
        if self.can_king_castle != other.can_king_castle:
            return False
        if self.can_queen_castle != other.can_queen_castle:
            return False
        return True

    def __str__(self):
        return f'King(pos={self.pos}, king={self.can_king_castle}, queen={self.can_queen_castle}, colour={self.colour})'
