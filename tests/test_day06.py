from aoc.day06 import solve_part1, solve_part2

input_data = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """


def test_solve_part1():
    assert solve_part1(input_data) == 4277556


def test_solve_part2():
    assert solve_part2(input_data) == 3263827
