import unittest

from board import Board
from pieces import InvalidMove, Pos, Colour


class BishopMove(unittest.TestCase):
    def test_vertical(self):
        board = Board()
        board.move("f2", "f4")
        board.move("f7", "f5")
        try:
            board.move("f1", "f2")
        except InvalidMove:
            return
        self.fail("bishop moved vertically")

    def test_horizontal(self):
        board = Board()
        board.move("e2", "e4")
        board.move("e7", "e5")
        board.move("f1", "d3")
        board.move("g8", "f6")
        try:
            board.move("d3", "c3")
        except InvalidMove:
            return
        self.fail("bishop moved horizontally")

    def test_diagonal(self):
        board = Board()
        board.move("e2", "e4")
        board.move("e7", "e5")
        board.move("f1", "c4")
        self.assertEqual(Colour.WHITE, board[Pos.from_str("c4")].colour)


if __name__ == '__main__':
    unittest.main()
