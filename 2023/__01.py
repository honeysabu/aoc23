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
    keywords = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    
    lines = data.split("\n")

    def find_all_numbers(keywords, line):
        for word, digit in keywords.items():
            line = line.replace(word, digit)
        return ''.join(filter(str.isdigit, line))

    total_sum = 0

    for line in lines:
        line = line.strip()
        numbers = find_all_numbers(keywords, line)
        if numbers:
            total_sum += int(numbers[0] + numbers[-1])

    return total_sum

   

#def test_part1():
    #assert part1(test_data) == 142

def test_part2():
    assert part2(test_data) == 281

data = get_data(day=1, year=2023)

print("Part 1:", part1(data))
print("Part 2:", part2(data))

test_data = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
