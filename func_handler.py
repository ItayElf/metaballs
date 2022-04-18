from typing import Callable

from classes import Point

WIDTH, HEIGHT = 641, 641

assert WIDTH % 2 == 1 and HEIGHT % 2 == 1

fn_type = Callable[[float, float], float]


def calc_fn(fn: fn_type, x: float, y: float) -> float:
    """Calculates a function with the screen x and y as if they were on an axis"""
    return fn(x - WIDTH // 2, y - HEIGHT // 2)


def calc_square(fn: fn_type, x_top: int, y_top: int) -> tuple[float, float, float, float]:
    """Calculate a square using the top left corner while True means green (greater than 1, inside) and false blue (less than 1, outside) and the points are clockwise"""
    return (
        calc_fn(fn, x_top, y_top),
        calc_fn(fn, x_top + 1, y_top),
        calc_fn(fn, x_top + 1, y_top + 1),
        calc_fn(fn, x_top, y_top + 1),
    )


def _generate_point_of_square(x_top: int, y_top: int, idx: int) -> Point:
    """Returns a point based on the idx in square"""
    if idx < 0:
        idx = 4 + idx
    return Point(x_top + int(idx in (1, 2)), y_top + int(idx in (2, 3)))


def _get_line_point(p1: Point, p2: Point, p1_val: float, p2_val: float) -> Point:
    """Returns a point of the contour"""
    k = abs(p1_val - 1)
    l = abs(1 - p2_val)
    return Point(((p1.x * l + p2.x * k) / (k + l)), ((p1.y * l + p2.y * k) / (k + l)))


def get_lines_from_square(square: tuple[float, float, float, float], x_top: int, y_top: int) -> list[
    tuple[Point, Point]]:
    """Returns a list with tuples of start and end of lines to draw"""
    bool_square = [v > 1 for v in square]
    if sum(bool_square) == 4 or sum(bool_square) == 0:
        return []
    elif sum(bool_square) == 1:
        idx = bool_square.index(True)
        p = _generate_point_of_square(x_top, y_top, idx)
        next_idx = (idx + 1) % 4
        next_p = _generate_point_of_square(x_top, y_top, next_idx)
        prev_p = _generate_point_of_square(x_top, y_top, idx - 1)
        return [
            (
                _get_line_point(p, next_p, square[idx], square[next_idx]),
                _get_line_point(prev_p, p, square[idx - 1], square[idx])
            )
        ]
    elif sum(bool_square) == 2:
        idx = bool_square.index(True)
        if bool_square[idx] and bool_square[(idx + 2) % 4]:  # diagonals
            p = _generate_point_of_square(x_top, y_top, idx)
            p2 = _generate_point_of_square(x_top, y_top, (idx + 1) % 4)
            p3 = _generate_point_of_square(x_top, y_top, (idx + 2) % 4)
            t1 = (
                _get_line_point(p, p2, square[idx], square[(idx + 1) % 4]),
                _get_line_point(p2, p3, square[(idx + 1) % 4], square[(idx + 2) % 4])
            )
            p4 = _generate_point_of_square(x_top, y_top, idx - 1)
            t2 = (
                _get_line_point(p3, p4, square[(idx + 2) % 4], square[idx - 1]),
                _get_line_point(p4, p, square[idx - 1], square[idx])
            )
            return [t1, t2]
        else:  # adjacent
            if bool_square[(idx + 1) % 4]:
                idx, next_idx = idx, (idx + 1) % 4
            else:
                idx, next_idx = idx - 1, idx
            next_p = _generate_point_of_square(x_top, y_top, next_idx)
            next_next_p = _generate_point_of_square(x_top, y_top, (next_idx + 1) % 4)
            p = _generate_point_of_square(x_top, y_top, idx)
            prev_p = _generate_point_of_square(x_top, y_top, idx - 1)
            return [
                (
                    _get_line_point(next_p, next_next_p, square[next_idx], square[(next_idx + 1) % 4]),
                    _get_line_point(prev_p, p, square[idx - 1], square[idx])
                )
            ]
    elif sum(bool_square) == 3:
        idx = bool_square.index(False)
        p = _generate_point_of_square(x_top, y_top, idx)
        next_idx = idx + 1 % 4
        next_p = _generate_point_of_square(x_top, y_top, next_idx)
        prev_p = _generate_point_of_square(x_top, y_top, idx - 1)
        return [
            (
                _get_line_point(p, next_p, square[idx], square[next_idx]),
                _get_line_point(prev_p, p, square[idx - 1], square[idx])
            )
        ]
