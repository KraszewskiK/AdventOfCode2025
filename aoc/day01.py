def solve_part1(input_data: str):
    instructions = parse_input(input_data)
    position = 50
    password = 0
    for direction, distance in instructions:
        if direction == 'L':
            position = (position - distance) % 100
        elif direction == 'R':
            position = (position + distance) % 100
        if position == 0:
            password += 1
    return password


def solve_part2(input_data: str):
    instructions = parse_input(input_data)
    position = 50
    password = 0
    for direction, distance in instructions:
        password += distance // 100
        distance %= 100
        if direction == 'L':
            password += 1 if 0 < position <= distance else 0
            position = (position - distance) % 100
        elif direction == 'R':
            password += 1 if (position + distance) >= 100 else 0
            position = (position + distance) % 100
    return password


def parse_input(input_data: str):
    input_data = [line.strip() for line in input_data.splitlines() if line.strip()]
    return [(line[0], int(line[1:])) for line in input_data]
