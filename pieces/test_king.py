import unittest

from board import Board
from pieces import InvalidMove, Colour, Pos


class KingMove(unittest.TestCase):
    def test_vertical(self):
        board = Board()
        board.move("e2", "e4")
        board.move("e7", "e5")
        board.move("e1", "e2")
        self.assertEqual('k', board[Pos.from_str('e2')].LETTER)

    def test_horizontal(self):
        board = Board()
        board.move("e2", "e4")
        board.move("e7", "e5")
        board.move("e1", "e2")
        board.move("d7", "d5")
        board.move("e2", "e3")
        board.move("c7", "c5")
        board.move("e3", "f3")
        self.assertEqual('k', board[Pos.from_str('f3')].LETTER)

    def test_diagonal(self):
        board = Board()
        board.move("e2", "e4")
        board.move("e7", "e5")
        board.move("e1", "e2")
        board.move("d7", "d5")
        board.move("e2", "f3")
        self.assertEqual('k', board[Pos.from_str('f3')].LETTER)

    def test_multiple_squares(self):
        board = Board()
        board.move("e2", "e4")
        board.move("e7", "e5")
        try:
            board.move("e1", "e3")
        except InvalidMove:
            return
        self.fail("king moved multiple squares")


if __name__ == '__main__':
    unittest.main()
