from aoc.day04 import solve_part1, solve_part2

input_data = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


def test_solve_part1():
    assert solve_part1(input_data) == 13


def test_solve_part2():
    assert solve_part2(input_data) == 43
