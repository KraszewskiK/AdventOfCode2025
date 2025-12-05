def solve_part1(input_data: str) -> int:
    ranges, ids = parse_input(input_data)
    fresh_ids = set()
    for id_ in ids:
        for r in ranges:
            if r[0] <= id_ <= r[1]:
                fresh_ids.add(id_)
                break
    return len(fresh_ids)


def solve_part2(input_data: str) -> int:
    ranges, _ = parse_input(input_data)
    ranges.sort(key=lambda r: r[0])
    merged_ranges = [list(ranges.pop(0))]
    for start, end in ranges:
        if start <= merged_ranges[-1][1] + 1:
            merged_ranges[-1][1] = max(merged_ranges[-1][1], end)
        else:
            merged_ranges.append([start, end])
    n_fresh_ids = sum(end - start + 1 for start, end in merged_ranges)
    return n_fresh_ids


def parse_input(input_data: str):
    input_data = input_data.strip().split('\n\n')
    ranges = [r.split('-') for r in input_data[0].split('\n')]
    ranges = [(int(x), int(y)) for x, y in ranges]
    ids = [int(x) for x in input_data[1].split('\n')]
    return ranges, ids
