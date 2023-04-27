import unittest

from board import Board
from pieces import Pos


class PawnMove(unittest.TestCase):
    def test_capture_horizontal(self):
        board = Board()
        board.move_coord(Pos(4, 1), Pos(4, 3))
        board.move_coord(Pos(4, 6), Pos(4, 4))
        board.move_coord(Pos(5, 1), Pos(5, 3))
        board.move_coord(Pos(3, 7), Pos(6, 4))
        board.move_coord(Pos(5, 3), Pos(6, 4))
        self.assertEqual(board[Pos(6, 4)].LETTER, 'p')


if __name__ == '__main__':
    unittest.main()
