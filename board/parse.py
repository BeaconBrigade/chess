from board import Board
from pieces import Pos, Colour


class InvalidCoordinate(Exception):
    pass


def parse_coord(pos: str) -> Pos:
    """
    Parses a chess notation coordinate into a coordinate: e4 -> Pos(4, 3)
    :param pos: The coordinate in chess notation, e.g.: e4 or d5 or h7
    :return: The parsed coordinate
    """
    if len(pos) < 2:
        raise InvalidCoordinate()

    file = -1
    match pos[0].lower():
        case 'a':
            file = 0
        case 'b':
            file = 1
        case 'c':
            file = 2
        case 'd':
            file = 3
        case 'e':
            file = 4
        case 'f':
            file = 5
        case 'g':
            file = 6
        case 'h':
            file = 7

    try:
        rank = int(pos[1]) - 1
    except ValueError:
        raise InvalidCoordinate()

    if rank not in range(0, 8):
        raise InvalidCoordinate()

    return Pos(file, rank)


def parse_capture(pos: str) -> (Pos, Pos):
    """
    Parses captures using coordinates: e4xd5 -> Pos(4, 3), Pos(3, 4)
    :param pos: The string with two coordinates separated by 'x'
    :return: The parsed start, and end coordinates
    """
    [start, end] = pos.split('x', 1)
    start, end = parse_coord(start.strip()), parse_coord(end.strip())

    return start, end


class InvalidFen(Exception):
    pass


def parse_fen(fen: str) -> Board:
    from pieces.pawn import Pawn
    from pieces.rook import Rook
    from pieces.knight import Knight
    from pieces.bishop import Bishop
    from pieces.queen import Queen
    from pieces.king import King

    [pieces, end] = fen.split(' ', maxsplit=1)
    ranks = pieces.split('/')
    grid = []

    # parse where each piece is
    # reverse the ranks, because the white comes first in the Board
    # but in FEN, black comes first
    for (i, rank) in enumerate(reversed(ranks)):
        if len(rank) > 8:
            raise InvalidFen()
        for c in rank:
            # blank spaces
            if c.isdigit():
                for num in range(int(c)):
                    grid.append(None)
                continue
            colour = Colour.WHITE if c.isupper() else Colour.BLACK
            pos = Pos(len(grid) - i * 8, i)
            match c.lower():
                case 'p':
                    grid.append(Pawn(colour, pos))
                case 'r':
                    grid.append(Rook(colour, pos))
                case 'n':
                    grid.append(Knight(colour, pos))
                case 'b':
                    grid.append(Bishop(colour, pos))
                case 'q':
                    grid.append(Queen(colour, pos))
                case 'k':
                    grid.append(King(colour, pos))
                case _:
                    raise InvalidFen()

    if len(grid) != 64:
        raise InvalidFen()

    board = Board()
    board.grid = grid

    [turn, castles, en_passent, half_move_count, move_count] = end.split(' ', maxsplit=5)
    board.turn = Colour.WHITE if turn == 'w' else Colour.BLACK
    try:
        board.en_passent_target = parse_coord(en_passent)
    except InvalidCoordinate:
        board.en_passent_target = None
    try:
        board.move_number = int(move_count)
    except ValueError:
        raise InvalidFen()
    # find kings
    for piece in board.grid:
        if piece is None:
            continue
        if piece.LETTER == 'k':
            if piece.colour == Colour.WHITE:
                piece.can_king_castle = 'K' in castles
                piece.can_queen_castle = 'Q' in castles
            else:
                piece.can_king_castle = 'k' in castles
                piece.can_queen_castle = 'q' in castles

    try:
        board.half_move_count = int(half_move_count)
    except ValueError:
        raise InvalidFen()

    return board
