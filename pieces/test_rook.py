import unittest

from board import Board
from pieces import InvalidMove, Colour, Pos
from pieces.rook import Rook


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

    def test_valid_moves(self):
        rook = Rook(Colour.WHITE, Pos(0, 0))
        self.assertCountEqual(
            [Pos(1, 0), Pos(2, 0), Pos(3, 0), Pos(4, 0), Pos(5, 0), Pos(6, 0), Pos(7, 0), Pos(0, 1), Pos(0, 2),
             Pos(0, 3), Pos(0, 4), Pos(0, 5), Pos(0, 6), Pos(0, 7)], rook.valid_moves())

    def test_valid_centre(self):
        rook = Rook(Colour.WHITE, Pos(4, 4))
        self.assertCountEqual(
            [Pos(5, 4), Pos(6, 4), Pos(7, 4), Pos(3, 4), Pos(2, 4), Pos(1, 4), Pos(0, 4), Pos(4, 5), Pos(4, 6),
             Pos(4, 7), Pos(4, 3), Pos(4, 2), Pos(4, 1), Pos(4, 0)], rook.valid_moves())


if __name__ == '__main__':
    unittest.main()
