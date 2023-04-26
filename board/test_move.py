import unittest

from board import Board, Blocked, squares_between
from pieces import Pos, InvalidMove


class TestMove(unittest.TestCase):
    def test_no_movement(self):
        board = Board()
        try:
            board.move(Pos(4, 1), Pos(4, 1))
        except InvalidMove:
            return
        self.fail("piece didn't move")

    def test_move_self(self):
        board = Board()
        board.move(Pos(4, 1), Pos(4, 2))
        board.move(Pos(4, 6), Pos(4, 5))
        try:
            board.move(Pos(3, 1), Pos(4, 2))
        except InvalidMove:
            return
        self.fail("piece captured itself")

    def test_move_nothing(self):
        board = Board()
        try:
            board.move(Pos(4, 4), Pos(4, 6))
        except InvalidMove:
            return
        self.fail("moved a piece that didn't exist")

    def test_collision_vertical(self):
        board = Board()
        try:
            board.move(Pos(4, 0), Pos(4, 2))
        except Blocked:
            return
        self.fail("moved through your own piece vertically")


class TestSquaresBetween(unittest.TestCase):
    def test_horizontal_one_square(self):
        intermediate = squares_between(Pos(0, 0), Pos(1, 0))
        self.assertEqual([], intermediate)

    def test_horizontal_two_square(self):
        intermediate = squares_between(Pos(0, 0), Pos(2, 0))
        self.assertEqual([Pos(1, 0)], intermediate)

    def test_horizontal_one_square_left(self):
        intermediate = squares_between(Pos(1, 0), Pos(0, 0))
        self.assertEqual([], intermediate)

    def test_horizontal_three_square_left(self):
        intermediate = squares_between(Pos(4, 0), Pos(1, 0))
        self.assertEqual([Pos(3, 0), Pos(2, 0)], intermediate)

    def test_vertical_one_square(self):
        intermediate = squares_between(Pos(0, 0), Pos(0, 1))
        self.assertEqual([], intermediate)

    def test_vertical_two_square(self):
        intermediate = squares_between(Pos(0, 0), Pos(0, 2))
        self.assertEqual([Pos(0, 1)], intermediate)

    def test_vertical_one_square_down(self):
        intermediate = squares_between(Pos(0, 3), Pos(0, 2))
        self.assertEqual([], intermediate)

    def test_vertical_three_square_down(self):
        intermediate = squares_between(Pos(0, 4), Pos(0, 1))
        self.assertEqual([Pos(0, 3), Pos(0, 2)], intermediate)


if __name__ == '__main__':
    unittest.main()
