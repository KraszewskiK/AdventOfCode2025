def solve_part1(input_data: str) -> int:
    result = 0
    ranges = process_input(input_data)
    for lower, upper in ranges:
        result += sum(n for n in get_possible_invalid_ids(lower, upper))
    return result


def solve_part2(input_data: str) -> int:
    result = 0
    ranges = process_input(input_data)
    for lower, upper in ranges:
        for n in range(lower, upper + 1):
            if is_id_invalid(n):
                result += n
    return result


def process_input(input_data: str):
    ranges = input_data.replace("\n", "").strip().split(',')
    ranges = [r.strip().split("-") for r in ranges if r]
    ranges = [(int(start), int(end)) for start, end in ranges]
    return ranges


def n2nn(n: int) -> int:
    return n * (10 ** (len(str(n)))) + n


def get_ids_of_length(length):
    if length % 2 != 0:
        return
    cur_len = length // 2
    start = 10 ** (cur_len - 1)
    end = 10 ** cur_len - 1
    for n in range(n2nn(start), n2nn(end) + 1, 10 ** cur_len + 1):
        yield n


def get_possible_invalid_ids(lower, upper):
    lower_len = len(str(lower))
    upper_len = len(str(upper))
    for i in range(lower_len, upper_len + 1):
        for n in get_ids_of_length(i):
            if lower <= n <= upper:
                yield n


def is_id_invalid(n: int) -> bool:
    s = str(n)
    for r in range(1, len(s) // 2 + 1):
        if len(s) % r == 0 and s[:r] * (len(s) // r) == s:
            return True
    return False
