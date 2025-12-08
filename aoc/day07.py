def solve_part1(input_data: str) -> int:
    input_data = input_data.strip().splitlines()
    beams = {input_data[0].index("S")}
    splits = 0
    for line in input_data[1:]:
        new_beams = set()
        for i in range(len(line)):
            if i in beams:
                if line[i] == "^":
                    new_beams.update([i - 1, i + 1])
                    splits += 1
                elif line[i] == ".":
                    new_beams.add(i)
        beams = new_beams
    return splits


def solve_part2(input_data: str) -> int:
    input_data = input_data.strip().splitlines()
    timelines = {input_data[0].index("S"): 1}
    for line in input_data[1:]:
        new_timelines = {}
        for i in range(len(line)):
            if i in timelines:
                if line[i] == "^":
                    new_timelines[i - 1] = new_timelines.get(i - 1, 0) + timelines[i]
                    new_timelines[i + 1] = new_timelines.get(i + 1, 0) + timelines[i]
                elif line[i] == ".":
                    new_timelines[i] = new_timelines.get(i, 0) + timelines[i]
        timelines = new_timelines
    return sum(timelines.values())
