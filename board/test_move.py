import unittest

from board import Board
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


if __name__ == '__main__':
    unittest.main()
