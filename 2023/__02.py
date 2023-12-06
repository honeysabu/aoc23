from aocd import get_data


def part1(data):
    games = data.split("\n")
    possible_games = []

    for game in games:
        if ':' not in game:  # Skip lines that don't have the expected format
            continue

        game_id, draws = game.split(": ")
        game_id = int(game_id.split(" ")[1])  # Extracting game ID number
        draws = draws.split("; ")

        # Convert each draw into a dictionary of cube counts
        draw_dicts = []
        for draw in draws:
            draw_dict = {'red': 0, 'green': 0, 'blue': 0}
            cubes = draw.split(", ")
            for cube in cubes:
                count, color = cube.split(" ")
                draw_dict[color] = max(draw_dict[color], int(count))
            draw_dicts.append(draw_dict)

        # Check if any draw exceeds the available cubes
        possible = True
        for draw_dict in draw_dicts:
            if draw_dict['red'] > 12 or draw_dict['green'] > 13 or draw_dict['blue'] > 14:
                possible = False
                break

        if possible:
            possible_games.append(game_id)

    return sum(possible_games)



def part2(data):
    games = data.split("\n")
    total_power = 0

    for game in games:
        if ':' not in game:  # Skip lines that don't have the expected format
            continue

        _, draws = game.split(": ")
        draws = draws.split("; ")

        # Initialize the minimum cube counts to 0
        min_cubes = {'red': 0, 'green': 0, 'blue': 0}

        for draw in draws:
            cubes = draw.split(", ")
            for cube in cubes:
                count, color = cube.split(" ")
                min_cubes[color] = max(min_cubes[color], int(count))

        # Calculate the power of the set of cubes for this game
        power = min_cubes['red'] * min_cubes['green'] * min_cubes['blue']
        total_power += power

    return total_power


def test_part1():
    assert part1(test_data) == 8

def test_part2():
    assert part2(test_data) == 2286.

data = get_data(day=1, year=2023)

print(part1(data))
print(part2(data))

test_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
