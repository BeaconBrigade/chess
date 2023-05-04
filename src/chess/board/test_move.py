import copy
import unittest

from . import Board, Blocked, squares_between
from ..pieces import Pos, InvalidMove, Move


class TestMove(unittest.TestCase):
    def test_no_movement(self):
        board = Board()
        try:
            board.move_coord(Pos(4, 1), Pos(4, 1))
        except InvalidMove:
            return
        self.fail("piece didn't move")

    def test_move_self(self):
        board = Board()
        board.move_coord(Pos(4, 1), Pos(4, 2))
        board.move_coord(Pos(4, 6), Pos(4, 5))
        try:
            board.move_coord(Pos(3, 1), Pos(4, 2))
        except InvalidMove:
            return
        self.fail("piece captured itself")

    def test_move_nothing(self):
        board = Board()
        try:
            board.move_coord(Pos(4, 4), Pos(4, 6))
        except InvalidMove:
            return
        self.fail("moved a piece that didn't exist")

    def test_collision_vertical(self):
        board = Board()
        try:
            board.move_coord(Pos(3, 0), Pos(3, 2))
        except Blocked:
            return
        self.fail("moved through your own piece vertically")

    def test_collision_horizontal(self):
        board = Board()
        board.move_coord(Pos(1, 0), Pos(2, 2))
        board.move_coord(Pos(4, 6), Pos(4, 5))
        try:
            board.move_coord(Pos(3, 0), Pos(1, 0))
        except Blocked:
            return
        self.fail("moved through your own piece horizontally")

    def test_error_in_the_wild(self):
        # this didn't work when I reached this position in the cli
        moves = [Move(start=Pos(x=4, y=1), end=Pos(x=4, y=3)), Move(start=Pos(x=4, y=6), end=Pos(x=4, y=4)),
                 Move(start=Pos(x=6, y=0),
                      end=Pos(x=5, y=2)), Move(start=Pos(x=6, y=7), end=Pos(x=5, y=5)),
                 Move(start=Pos(x=3, y=1), end=Pos(x=3, y=3)), Move(start=Pos(x=4, y=4), end=Pos(x=3, y=3)),
                 Move(start=Pos(x=5, y=2),
                      end=Pos(x=3, y=3)), Move(start=Pos(x=5, y=5), end=Pos(x=4, y=3)),
                 Move(start=Pos(x=3, y=0), end=Pos(x=4, y=1)), Move(start=Pos(x=3, y=6), end=Pos(x=3, y=4)),
                 Move(start=Pos(x=5, y=1),
                      end=Pos(x=5, y=2)), Move(start=Pos(x=5, y=7), end=Pos(x=2, y=4)),
                 Move(start=Pos(x=5, y=2), end=Pos(x=4, y=3)), Move(start=Pos(x=2, y=4), end=Pos(x=3, y=3)),
                 Move(start=Pos(x=4, y=3),
                      end=Pos(x=3, y=4)), Move(start=Pos(x=3, y=7), end=Pos(x=4, y=6)),
                 Move(start=Pos(x=4, y=1), end=Pos(x=4, y=6)), Move(start=Pos(x=4, y=7), end=Pos(x=4, y=6)),
                 Move(start=Pos(x=2, y=0),
                      end=Pos(x=6, y=4)), Move(start=Pos(x=5, y=6), end=Pos(x=5, y=5)),
                 Move(start=Pos(x=2, y=1), end=Pos(x=2, y=2)), Move(start=Pos(x=3, y=3), end=Pos(x=2, y=2)),
                 Move(start=Pos(x=1, y=0),
                      end=Pos(x=2, y=2)), Move(start=Pos(x=5, y=5), end=Pos(x=6, y=4)),
                 Move(start=Pos(x=5, y=0), end=Pos(x=2, y=3))
                 ]
        board = Board(move_list=moves)
        board.move('b8', 'd7')
        self.assertEqual('n', board[Pos.from_str('d7')].LETTER)


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

    def test_diagonal_right_up_one(self):
        intermediate = squares_between(Pos(0, 0), Pos(1, 1))
        self.assertEqual([], intermediate)

    def test_diagonal_right_up_two(self):
        intermediate = squares_between(Pos(0, 0), Pos(2, 2))
        self.assertEqual([Pos(1, 1)], intermediate)

    def test_diagonal_left_up_one(self):
        intermediate = squares_between(Pos(1, 0), Pos(0, 1))
        self.assertEqual([], intermediate)

    def test_diagonal_left_up_two(self):
        intermediate = squares_between(Pos(2, 0), Pos(0, 2))
        self.assertEqual([Pos(1, 1)], intermediate)

    def test_diagonal_right_down_one(self):
        intermediate = squares_between(Pos(0, 1), Pos(1, 0))
        self.assertEqual([], intermediate)

    def test_diagonal_right_down_two(self):
        intermediate = squares_between(Pos(0, 2), Pos(2, 0))
        self.assertEqual([Pos(1, 1)], intermediate)

    def test_diagonal_left_down_one(self):
        intermediate = squares_between(Pos(1, 1), Pos(0, 0))
        self.assertEqual([], intermediate)

    def test_diagonal_left_down_two(self):
        intermediate = squares_between(Pos(2, 2), Pos(0, 0))
        self.assertEqual([Pos(1, 1)], intermediate)


class MoveRemoveMove(unittest.TestCase):
    @staticmethod
    def blank_callback():
        pass

    def test_no_change(self):
        board = Board()
        temp = copy.deepcopy(board)

        board.apply_remove_move(Pos(4, 1), Pos(4, 2), self.blank_callback)

        self.assertEqual(temp, board)

    def test_no_change_2(self):
        board = Board(fen='3k4/8/8/8/6b1/8/8/3K4 w - - 0 1')
        temp = copy.deepcopy(board)

        board.apply_remove_move(Pos(3, 0), Pos(2, 1), self.blank_callback)
        self.assertEqual(temp, board)


if __name__ == '__main__':
    unittest.main()
