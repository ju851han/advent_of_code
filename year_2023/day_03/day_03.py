from year_2023.helper import get_file_content

IRRELEVANT_SYMBOLS = "."
GEAR = "*"


def get_symbol_positions(lines):
    """
    The for loop with index instead of for loop with item in list is used
    because .index function only returns the first occurrence

    :param lines:
    :return:
    """
    relevant_symbol_positions = []
    for line in lines:
        if line:
            for index in range(len(line)):
                sign = line[index]
                is_relevant_symbol = not sign.isdecimal() and sign != IRRELEVANT_SYMBOLS
                if is_relevant_symbol:
                    relevant_symbol_positions.append((lines.index(line), index))
    return relevant_symbol_positions


def get_part_numbers(start_positions, lines):
    """

    :param start_positions: symbol positions
    :param lines:
    :return: nested list : list is qrouped by symbol_position
    """
    all_part_numbers = []

    for symbol_row, symbol_column in start_positions:
        part_numbers = []
        # check horizontal
        do_collect_part_number(part_numbers, lines, symbol_row, symbol_column + 1)
        do_collect_part_number(part_numbers, lines, symbol_row, symbol_column - 1)
        # check vertical
        do_collect_part_number(part_numbers, lines, symbol_row + 1, symbol_column)
        do_collect_part_number(part_numbers, lines, symbol_row - 1, symbol_column)

        # check diagonal
        if not lines[symbol_row + 1][symbol_column].isdecimal():
            do_collect_part_number(part_numbers, lines, symbol_row + 1, symbol_column + 1)
            do_collect_part_number(part_numbers, lines, symbol_row + 1, symbol_column - 1)
        if not lines[symbol_row - 1][symbol_column].isdecimal():
            do_collect_part_number(part_numbers, lines, symbol_row - 1, symbol_column - 1)
            do_collect_part_number(part_numbers, lines, symbol_row - 1, symbol_column + 1)

        all_part_numbers.append(part_numbers)

    return all_part_numbers


def do_collect_part_number(part_numbers, lines, row, col):
    part_number = get_part_number(lines, row, col)
    if part_number:
        new_part_number = int(part_number)
        part_numbers.append(new_part_number)


def get_part_number(lines, start_row, start_col, row=False, col=False, part_number="", state=0):
    """
    :param lines:
    :param row:
    :param col:
    :param part_number:
    :param state: 0 - default
                  1 - read right numbers
                  -1 - read left numbers
    :return: str with part number
    """
    if state == 0:
        row = start_row
        col = start_col
    if 0 <= col < len(lines[row]):
        if lines[row][col].isdecimal():
            if state in [0, 1]:
                part_number += lines[row][col]
                new_col = col + 1
                state = 1
            else:
                part_number = f"{lines[row][col]}{part_number}"
                new_col = col - 1
            part_number = get_part_number(lines, start_row, start_col, row, new_col, part_number, state)
        elif state == 1:
            new_col = start_col - 1
            part_number = get_part_number(lines, start_row, start_col, start_row, new_col, part_number, state=-1)
    return part_number


def get_calculated_part_numbers(all_part_numbers):
    res = 0
    for part_numbers_per_symbol in all_part_numbers:
        for part_number in part_numbers_per_symbol:
            res += part_number
    return res


def get_recalculated_part_numbers(all_part_numbers):
    res = 0
    for part_numbers_per_symbol in all_part_numbers:
        if len(part_numbers_per_symbol) == 2:
            res += (part_numbers_per_symbol[0] * part_numbers_per_symbol[1])
    return res


if __name__ == '__main__':
    data = get_file_content("puzzle_input.txt")
    lines = data.split("\n")

    symbol_positions = get_symbol_positions(lines)
    part_numbers = get_part_numbers(symbol_positions, lines)
    print(part_numbers)
    print(f"part 1: sum of all of the part numbers: {get_calculated_part_numbers(part_numbers)}")
    print(f"part 2: sum of all of the part numbers: {get_recalculated_part_numbers(part_numbers)}")
