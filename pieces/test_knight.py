import unittest

from board import Board
from pieces import Pos, InvalidMove


class KnightMove(unittest.TestCase):
    def test_first(self):
        board = Board()
        board.move("g1", "f3")
        self.assertEqual('n', board[Pos.from_str('f3')].LETTER)

    def test_vertical(self):
        board = Board()
        board.move("g2", "g4")
        board.move("e7", "e5")
        try:
            board.move("g1", "g2")
        except InvalidMove:
            return
        self.fail("knight moved vertically")

    def test_diagonal(self):
        board = Board()
        board.move("f2", "f4")
        board.move("e7", "e5")
        try:
            board.move("g1", "f2")
        except InvalidMove:
            return
        self.fail("knight moved diagonally")

    def test_horizontal(self):
        board = Board()
        board.move("g1", "f3")
        board.move("e7", "e5")
        try:
            board.move("f3", "g3")
        except InvalidMove:
            return
        self.fail("knight moved horizontally")


if __name__ == '__main__':
    unittest.main()
