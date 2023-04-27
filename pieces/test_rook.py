import unittest

from board import Board
from pieces import InvalidMove, Colour, Pos


class RookMove(unittest.TestCase):
    def test_vertical(self):
        board = Board()
        board.move("h2", "h4")
        board.move("h7", "h5")
        board.move("h1", "h3")
        self.assertEqual(Colour.WHITE, board[Pos.from_str("h3")].colour)

    def test_horizontal(self):
        board = Board()
        board.move("h2", "h4")
        board.move("h7", "h5")
        board.move("h1", "h3")
        board.move("a7", "a5")
        board.move("h3", "c3")
        self.assertEqual(Colour.WHITE, board[Pos.from_str("c3")].colour)

    def test_diagonal(self):
        board = Board()
        board.move("e2", "e4")
        board.move("e7", "e5")
        board.move("f1", "d3")
        board.move("g8", "f6")
        try:
            board.move("d3", "c3")
        except InvalidMove:
            return
        self.fail("rook moved diagonally")


if __name__ == '__main__':
    unittest.main()
