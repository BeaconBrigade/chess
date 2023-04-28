import unittest

from board import Board
from pieces import create_board_grid, Colour, Pos


class ParseFen(unittest.TestCase):
    def test_normal(self):
        board = Board(fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
        self.assertEqual(create_board_grid(), board.grid)
        self.assertEqual(Colour.WHITE, board.turn)
        self.assertIsNone(board.en_passent_target)
        self.assertEqual(0, board.half_move_count)
        self.assertEqual([], board.half_moves)
        self.assertEqual(1, board.move_number)

    def test_oh_no_my_queen(self):
        from pieces.king import King
        from pieces.knight import Knight
        from pieces.pawn import Pawn
        from pieces.queen import Queen
        from pieces.rook import Rook
        from pieces.bishop import Bishop
        board = Board(fen='r2Bk2r/ppp2ppp/2p5/8/4n1b1/3P4/PPP1KbPP/RN1Q1B1R w kq - 2 9')
        grid = [
            # 1
            Rook(Colour.WHITE, Pos(0, 0)), Knight(Colour.WHITE, Pos(1, 0)), None,
            Queen(Colour.WHITE, Pos(3, 0)), None, Bishop(Colour.WHITE, Pos(5, 0)),
            None, Rook(Colour.WHITE, Pos(7, 0)),
            # 2
            Pawn(Colour.WHITE, Pos(0, 1)), Pawn(Colour.WHITE, Pos(1, 1)), Pawn(Colour.WHITE, Pos(2, 1)),
            None, King(Colour.WHITE, Pos(4, 1), king_castle=False, queen_castle=False), Bishop(Colour.BLACK, Pos(5, 1)),
            Pawn(Colour.WHITE, Pos(6, 1)), Pawn(Colour.WHITE, Pos(7, 1)),
            # 3
            None, None, None, Pawn(Colour.WHITE, Pos(3, 2)), None, None, None, None,
            # 4
            None, None, None, None, Knight(Colour.BLACK, Pos(4, 3)), None, Bishop(Colour.BLACK, Pos(6, 3)), None,
            # 5
            None, None, None, None, None, None, None, None,
            # 6
            None, None, Pawn(Colour.BLACK, Pos(2, 5)), None, None, None, None, None,
            # 7
            Pawn(Colour.BLACK, Pos(0, 6)), Pawn(Colour.BLACK, Pos(1, 6)), Pawn(Colour.BLACK, Pos(2, 6)),
            None, None, Pawn(Colour.BLACK, Pos(5, 6)),
            Pawn(Colour.BLACK, Pos(6, 6)), Pawn(Colour.BLACK, Pos(7, 6)),
            # 8
            Rook(Colour.BLACK, Pos(0, 7)), None, None,
            Bishop(Colour.WHITE, Pos(3, 7)), King(Colour.BLACK, Pos(4, 7)), None,
            None, Rook(Colour.BLACK, Pos(7, 7)),
        ]

        self.assertEqual(grid, board.grid)
        self.assertEqual(Colour.WHITE, board.turn)
        self.assertIsNone(board.en_passent_target)
        self.assertEqual(2, board.half_move_count)
        self.assertEqual(9, board.move_number)


if __name__ == '__main__':
    unittest.main()
