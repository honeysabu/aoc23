from aocd import get_data


def part1(data):
    total_sum = 0
    lines = data.split("\n")

    for line in lines:
        first_digit = next((char for char in line if char.isdigit()), None)
        last_digit = next((char for char in reversed(line) if char.isdigit()), None)

        if first_digit and last_digit:
            total_sum += int(first_digit + last_digit)

    return total_sum

def part2(data):
    
    return None

def test_part1():
    assert part1(test_data) == 142

def test_part2():
    assert part2(test_data) == 900

data = get_data(day=1, year=2023)

print("Part 1:", part1(data))
print("Part 2:", part2(data))

test_data = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
