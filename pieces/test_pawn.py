import unittest

from board import Board
from pieces import Pos, Colour


class PawnMove(unittest.TestCase):
    def test_capture_horizontal(self):
        board = Board()
        board.move_coord(Pos(4, 1), Pos(4, 3))
        board.move_coord(Pos(7, 7), Pos(2, 2))
        board.move_coord(Pos(3, 1), Pos(2, 2))
        self.assertEqual(board[Pos(2, 2)].colour, Colour.WHITE)


if __name__ == '__main__':
    unittest.main()
