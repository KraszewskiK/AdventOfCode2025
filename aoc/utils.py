import requests


def read_input(day):
    with open(f"input/day{day:02}.txt") as f:
        return f.read().strip()


def fetch_input(day, session_cookie):
    url = f"https://adventofcode.com/2025/day/{day}/input"
    headers = {"Cookie": f"session={session_cookie}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(f"input/day{day:02}.txt", "w") as f:
            f.write(response.text.strip())
        print(f"Input for day {day} fetched and saved.")
    else:
        print(f"Error fetching input for day {day}: {response.status_code}")
