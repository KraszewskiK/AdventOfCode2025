def solve_part1(input_data: str) -> int:
    grid = input_data.split('\n')
    accessible_positions = get_accessible_positions(grid)
    return len(accessible_positions)


def solve_part2(input_data: str) -> int:
    grid = input_data.split('\n')
    removed = 0
    while True:
        accessible_positions = get_accessible_positions(grid)
        if not accessible_positions:
            break
        removed += len(accessible_positions)
        for x, y in accessible_positions:
            grid[x] = grid[x][:y] + '.' + grid[x][y+1:]
    return removed


def get_accessible_positions(grid):
    accessible = {(x, y): 0 for x in range(len(grid)) for y in range(len(grid[x])) if grid[x][y] == '@'}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != '@':
                continue
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    x, y = i + dx, j + dy
                    if (x, y) in accessible:
                        accessible[(x, y)] += 1
                        if accessible[(x, y)] >= 4:
                            del accessible[(x, y)]
    return accessible.keys()
