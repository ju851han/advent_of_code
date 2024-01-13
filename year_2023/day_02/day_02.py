from year_2023.helper import get_file_content

from functools import reduce
from operator import mul

if __name__ == '__main__':
    MAX_NUMBER_CUBES_RED = 12
    MAX_NUMBER_CUBES_GREEN = 13
    MAX_NUMBER_CUBES_BLUE = 14

    data = get_file_content("puzzle_input.txt")
    lines = data.split("\n")
    valid_game_ids = []
    power = []
    for line in lines:
        if line:
            is_invalid = False
            game_id = int(line.split(":")[0][4:])
            throws = line.split(":")[1].split(";")
            max_values = {}
            for throw in throws:
                for cube in throw.split(","):
                    _, number, color = cube.split(" ")
                    number = int(number)
                    is_valid = -1
                    match color:
                        case "red":
                            is_valid = MAX_NUMBER_CUBES_RED
                        case "green":
                            is_valid = MAX_NUMBER_CUBES_GREEN
                        case "blue":
                            is_valid = MAX_NUMBER_CUBES_BLUE
                    if number > max_values.get(color, 0):
                        max_values[color] = number
                    if number > is_valid:
                        is_invalid = True
            power.append(reduce(mul, max_values.values()))
            if not is_invalid:
                valid_game_ids.append(game_id)
    print(f"Sum of the IDs for part 1: {sum(valid_game_ids)}")
    print(f"Sum of the power for part 2: {sum(power)}")
