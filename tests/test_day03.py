from aoc.day03 import solve_part1, solve_part2

input_data = """\
987654321111111
811111111111119
234234234234278
818181911112111"""


def test_solve_part1():
    assert solve_part1(input_data) == 357


def test_solve_part2():
    assert solve_part2(input_data) == 3121910778619