import importlib
import os.path

from aoc import read_input

def run_day(day):
    module = importlib.import_module(f"aoc.day{day:02}")
    input_data = read_input(day)
    print(f"Part 1: {module.solve_part1(input_data)}")
    print(f"Part 2: {module.solve_part2(input_data)}")

if __name__ == "__main__":
    import sys

    day_to_run = sys.argv[1]

    try:
        day_to_run = int(day_to_run)
    except ValueError:
        print("Please provide a valid day number.")
        sys.exit(1)

    if not (1 <= day_to_run <= 12):
        print("Day number must be between 1 and 12.")
        sys.exit(1)

    if not os.path.exists(f"aoc/day{day_to_run:02}.py"):
        print(f"Day {day_to_run} is not yet implemented.")
        sys.exit(1)

    run_day(day_to_run)