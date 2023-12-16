from year_2023.helper import get_file_content

if __name__ == '__main__':
    MAX_NUMBER_CUBES_RED = 12
    MAX_NUMBER_CUBES_GREEN = 13
    MAX_NUMBER_CUBES_BLUE = 14

    data = get_file_content("puzzle_input.txt")
    lines = data.split("\n")
    valid_game_ids = []
    for line in lines:
        if line:
            is_invalid = False
            game_id = int(line.split(":")[0][4:])
            throws = line.split(":")[1].split(";")
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
                    if number > is_valid:
                        is_invalid = True
            if not is_invalid:
                valid_game_ids.append(game_id)
    print(f"sum: {sum(valid_game_ids)}")
