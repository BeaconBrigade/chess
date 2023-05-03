import unittest

from board import Board
from board.check import king_in_check, is_in_checkmate
from pieces import Colour


class Check(unittest.TestCase):
    def test_not_in_check(self):
        board = Board()
        self.assertFalse(king_in_check(board, Colour.WHITE))

    def test_bishop_check(self):
        board = Board(fen='2k5/8/8/8/8/5b2/8/3K4 w - - 0 1')
        self.assertTrue(king_in_check(board, Colour.WHITE))

    def test_queen_check(self):
        board = Board(fen='rnb1kbnr/pppp1ppp/8/4p3/6Pq/5P2/PPPPP2P/RNBQKBNR w KQkq - 0 1')
        self.assertTrue(king_in_check(board, Colour.WHITE))

    def test_check_blocked(self):
        board = Board(fen='4k3/8/8/8/7b/8/5P2/4K3 w - - 0 1')
        self.assertFalse(king_in_check(board, Colour.WHITE))

    def test_knight_check(self):
        board = Board(fen='rnbqkb1r/pppppppp/8/8/3N4/5n2/PPPPPPPP/RNBQKB1R w KQkq - 0 1')
        self.assertTrue(king_in_check(board, Colour.WHITE))

    def test_pawn_check(self):
        board = Board(fen='8/8/4k3/8/8/8/5p2/4K3 w - - 0 1')
        self.assertTrue(king_in_check(board, Colour.WHITE))

    def test_pawn_check_wrong_direction(self):
        board = Board(fen='8/8/4k3/8/8/4K3/5p2/8 w - - 0 1')
        self.assertFalse(king_in_check(board, Colour.WHITE))

    def test_no_check_no_checkmate(self):
        board = Board(fen='3k4/8/8/8/8/8/8/3K4 w - - 0 1')
        self.assertFalse(is_in_checkmate(board, board.turn))

    def test_check_no_checkmate(self):
        board = Board(fen='3k4/8/8/8/6b1/8/8/3K4 w - - 0 1')
        self.assertFalse(is_in_checkmate(board, board.turn))

    def test_check_checkmate(self):
        board = Board(fen='8/8/8/8/3b4/k2b4/8/K7 w - - 0 1')
        self.assertTrue(is_in_checkmate(board, board.turn))

    def test_fools_mate(self):
        board = Board(fen='rnb1kbnr/pppp1ppp/8/4p3/6Pq/5P2/PPPPP2P/RNBQKBNR w KQkq - 0 1')
        self.assertTrue(is_in_checkmate(board, board.turn))

    def test_block_mate(self):
        board = Board(fen='1k4rq/8/8/8/8/8/R7/7K w - - 0 1')
        self.assertFalse(is_in_checkmate(board, board.turn))


if __name__ == '__main__':
    unittest.main()
