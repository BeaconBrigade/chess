from board import Board, Blocked, WrongTurn
from board.parse import InvalidCoordinate
from pieces import InvalidMove


def main():
    board = Board()

    while True:
        print(board)
        move_from = input("From:\t")
        move_to = input("To:\t\t")

        try:
            board.move(move_from, move_to)
        except InvalidMove:
            show_error("That was not a valid move")
        except Blocked:
            show_error("That piece was blocked")
        except WrongTurn:
            show_error("That piece is the wrong colour")
        except InvalidCoordinate:
            if move_from == 'q' or move_to == 'q':
                turn = board.turn.name.lower()
                print(f'Finishing, {turn[0].upper()}{turn[1:]} resigned')
                return

            show_error("That was not a valid coordinate")


def show_error(msg: str):
    print(msg)
    input("Hit enter to continue\t")


if __name__ == '__main__':
    main()
