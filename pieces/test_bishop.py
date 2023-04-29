import unittest

from board import Board
from pieces import InvalidMove, Pos, Colour
from pieces.bishop import Bishop


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

    def test_valid_moves(self):
        bishop = Bishop(Colour.WHITE, Pos(0, 0))
        self.assertEqual([Pos(1, 1), Pos(2, 2), Pos(3, 3), Pos(4, 4), Pos(5, 5), Pos(6, 6), Pos(7, 7)],
                         bishop.valid_moves())

    def test_valid_centre(self):
        bishop = Bishop(Colour.WHITE, Pos(4, 4))
        self.assertCountEqual(
            [Pos(3, 3), Pos(2, 2), Pos(1, 1), Pos(0, 0), Pos(5, 5), Pos(6, 6), Pos(7, 7), Pos(3, 5), Pos(2, 6),
             Pos(1, 7), Pos(5, 3), Pos(6, 2), Pos(7, 1)], bishop.valid_moves())


if __name__ == '__main__':
    unittest.main()
