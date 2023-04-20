import os

from pieces import Piece, create_board_grid


class Board:
    """ Represents a chess board.

        grid: the array of pieces. Pieces are stored in order from bottom left and rightward for each column
        and upward for each row. (a1 -> h1...a8->h8). `None` represents an empty square
    """
    grid: [Piece]

    def __init__(self):
        self.grid = create_board_grid()

    def __str__(self):
        string = ""
        for i in range(7, -1, -1):
            for j in range(8):
                piece = self.grid[i * 8 + j]
                string += (piece.letter() if piece is not None else "-") + " "
            string += os.linesep
        return string
