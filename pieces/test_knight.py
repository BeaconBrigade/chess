import unittest

from board import Board
from pieces import Pos, InvalidMove, Colour
from pieces.knight import Knight


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

    def test_valid_moves(self):
        knight = Knight(Colour.WHITE, Pos(0, 0))
        self.assertCountEqual([Pos(1, 2), Pos(2, 1)], knight.valid_moves())

    def test_valid_centre(self):
        knight = Knight(Colour.WHITE, Pos(4, 4))
        self.assertCountEqual([Pos(3, 6), Pos(5, 6), Pos(6, 5), Pos(6, 3), Pos(5, 2), Pos(3, 2), Pos(2, 3), Pos(2, 5)],
                              knight.valid_moves())


if __name__ == '__main__':
    unittest.main()
