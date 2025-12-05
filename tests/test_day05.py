from aoc.day05 import solve_part1, solve_part2

input_data = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


def test_solve_part1():
    assert solve_part1(input_data) == 3


def test_solve_part2():
    assert solve_part2(input_data) == 14
