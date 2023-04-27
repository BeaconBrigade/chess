from pieces import Pos


class InvalidCoordinate(Exception):
    pass


def parse_coord(pos: str) -> Pos:
    """
    Parses a chess notation coordinate into a coordinate: e4 -> Pos(4, 3)
    :param pos: The coordinate in chess notation, e.g.: e4 or d5 or h7
    :return: The parsed coordinate
    """
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
