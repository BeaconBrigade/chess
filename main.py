from board import Board


def main():
    board = Board()
    board.move("e2", "e4")
    board.move("e7", "e5")
    board.move("d1", "h5")
    board.move("b8", "c6")
    board.move("f1", "c4")
    board.move("g8", "f6")
    print(board)
    board.move("h5", "f7")
    print(board)


if __name__ == '__main__':
    main()
