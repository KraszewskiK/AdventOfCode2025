from aoc.day01 import solve_part1, solve_part2

input_data = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


def test_solve_part1():
    assert solve_part1(input_data) == 3


def test_solve_part2():
    assert solve_part2(input_data) == 6