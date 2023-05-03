import unittest

from ..board import Board
from . import InvalidMove, Colour, Pos
from .king import King


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

    def test_valid_moves(self):
        king = King(Colour.WHITE, Pos(0, 0))
        self.assertCountEqual([Pos(1, 0), Pos(1, 1), Pos(0, 1)], king.valid_moves())

    def test_valid_centre(self):
        king = King(Colour.WHITE, Pos(4, 4))
        self.assertCountEqual([Pos(3, 3), Pos(3, 4), Pos(3, 5), Pos(4, 5), Pos(4, 3), Pos(5, 5), Pos(5, 4), Pos(5, 3)],
                              king.valid_moves())


if __name__ == '__main__':
    unittest.main()
