from aocd import get_data


def part1(data):
    input = [s for s in data.split("\n")]
    print(input)
    return len(input)


def part2(data):
    input = [s for s in data.split("\n")]

    return len(input)


def test_part1():
    assert part1(test_data) == 142


def test_part2():
    assert part2(test_data) == 900


data = get_data(day=1, year=2023)

print(part1(data))
print(part2(data))

test_data = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
