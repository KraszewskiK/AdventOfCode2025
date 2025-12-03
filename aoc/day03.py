def solve_part1(input_data: str) -> int:
    result = 0
    for bank in parse_input(input_data):
        l = max(bank[:-1])
        r = max(bank[bank.index(l) + 1:])
        result += l * 10 + r
    return result


def solve_part2(input_data: str) -> int:
    result = 0
    for bank in parse_input(input_data):
        l = 0
        for i in range(12, 0, -1):
            v = max(bank[l:(-(i - 1) if i != 1 else len(bank))])
            l = bank.index(v, l) + 1
            result += v * 10 ** (i - 1)
    return result


def parse_input(input_data: str):
    input_data = input_data.strip().split('\n')
    banks = [[int(battery) for battery in bank] for bank in input_data if bank]
    return banks
