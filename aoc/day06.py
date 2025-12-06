def solve_part1(input_data: str) -> int:
    input_data = [line.split() for line in input_data.splitlines() if line.strip()]
    tasks = []
    for i in range(len(input_data[0])):
        task = {
            'numbers': [int(input_data[j][i]) for j in range(len(input_data) - 1)],
            'operation': input_data[-1][i]
        }
        tasks.append(task)
    total = solve_tasks(tasks)
    return total


def solve_part2(input_data: str) -> int:
    input_data = [line for line in input_data.splitlines() if line.strip()]
    tasks = []
    numbers = []
    operation = ""
    for i in range(len(input_data[0]) + 1):
        if i == len(input_data[0]) or all(line[i].isspace() for line in input_data):
            if numbers:
                task = {
                    'numbers': numbers,
                    'operation': operation
                }
                tasks.append(task)
                numbers, operation = [], ""
        else:
            numbers.append(int("".join(line[i] for line in input_data[:-1]).strip()))
            if operation == "":
                operation = input_data[-1][i]
    total = solve_tasks(tasks)
    return total


def solve_tasks(tasks: list[dict]) -> int:
    total = 0
    for task in tasks:
        if task["operation"] == "+":
            total += sum(task["numbers"])
        elif task["operation"] == "*":
            product = 1
            for number in task["numbers"]:
                product *= number
            total += product
    return total
