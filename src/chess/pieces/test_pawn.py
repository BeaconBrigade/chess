import unittest

from ..board import Board
from . import Pos, InvalidMove, Colour
from .pawn import Pawn


class PawnMove(unittest.TestCase):
    def test_capture_horizontal(self):
        board = Board()
        board.move_coord(Pos(4, 1), Pos(4, 3))
        board.move_coord(Pos(4, 6), Pos(4, 4))
        board.move_coord(Pos(5, 1), Pos(5, 3))
        board.move_coord(Pos(3, 7), Pos(6, 4))
        board.move_coord(Pos(5, 3), Pos(6, 4))
        self.assertEqual(board[Pos(6, 4)].LETTER, 'p')

    def test_move_two_squares_twice(self):
        board = Board()
        board.move_coord(Pos(4, 1), Pos(4, 3))
        board.move_coord(Pos(0, 6), Pos(0, 5))
        try:
            board.move_coord(Pos(4, 3), Pos(4, 5))
        except InvalidMove:
            return
        self.fail("pawn moved two squares twice")

    def test_valid_moves(self):
        pawn = Pawn(Colour.WHITE, Pos(0, 1))
        self.assertCountEqual([Pos(0, 2), Pos(0, 3), Pos(1, 2)], pawn.valid_moves())

    def test_valid_centre(self):
        pawn = Pawn(Colour.WHITE, Pos(4, 1))
        self.assertCountEqual([Pos(4, 2), Pos(4, 3), Pos(3, 2), Pos(5, 2)], pawn.valid_moves())


if __name__ == '__main__':
    unittest.main()
