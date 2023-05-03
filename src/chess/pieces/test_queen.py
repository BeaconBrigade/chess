import unittest

from ..board import Board
from . import Pos, Colour
from .queen import Queen


class QueenMove(unittest.TestCase):
    def test_horizontal(self):
        board = Board()
        board.move("d2", "d4")
        board.move("d7", "d5")
        board.move("d1", "d3")
        board.move("c7", "c5")
        board.move("d3", "h3")
        self.assertEqual('q', board[Pos.from_str("h3")].LETTER)

    def test_vertical(self):
        board = Board()
        board.move("d2", "d4")
        board.move("d7", "d5")
        board.move("d1", "d3")
        self.assertEqual("q", board[Pos.from_str("d3")].LETTER)

    def test_diagonal(self):
        board = Board()
        board.move("e2", "e4")
        board.move("e7", "e5")
        board.move("d1", "h5")
        self.assertEqual("q", board[Pos.from_str("h5")].LETTER)

    def test_valid_moves(self):
        queen = Queen(Colour.WHITE, Pos(0, 0))
        self.assertCountEqual(
            [Pos(1, 1), Pos(2, 2), Pos(3, 3), Pos(4, 4), Pos(5, 5), Pos(6, 6), Pos(7, 7), Pos(1, 0), Pos(2, 0),
             Pos(3, 0), Pos(4, 0), Pos(5, 0), Pos(6, 0), Pos(7, 0), Pos(0, 1), Pos(0, 2),
             Pos(0, 3), Pos(0, 4), Pos(0, 5), Pos(0, 6), Pos(0, 7)], queen.valid_moves())

    def test_valid_centre(self):
        queen = Queen(Colour.WHITE, Pos(4, 4))
        self.assertCountEqual(
            [Pos(3, 3), Pos(2, 2), Pos(1, 1), Pos(0, 0), Pos(5, 5), Pos(6, 6), Pos(7, 7), Pos(3, 5), Pos(2, 6),
             Pos(1, 7), Pos(5, 3), Pos(6, 2), Pos(7, 1), Pos(5, 4), Pos(6, 4), Pos(7, 4), Pos(3, 4), Pos(2, 4),
             Pos(1, 4), Pos(0, 4), Pos(4, 5), Pos(4, 6),
             Pos(4, 7), Pos(4, 3), Pos(4, 2), Pos(4, 1), Pos(4, 0)], queen.valid_moves())


if __name__ == '__main__':
    unittest.main()
