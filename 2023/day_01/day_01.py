def get_file_content(file_name: str):
    """
    :param file_name: name of the file located in the day_01 folder
    :return: content of the file with the provided file_name
    :rtype: str
    """
    file_content = False
    with open(file_name, 'r') as file:
        file_content = file.read()
    file.close()
    return file_content


def get_calibration_value(input_data: str):
    """
    :param input_data: file_content
    :return: calculated calibration value
    :rtype: int
    """
    lines = input_data.split("\n")
    return _get_calculated_calibration_value(lines)


def _get_calculated_calibration_value(lines: list):
    """ Building the sum of numbers per line for the calibration value
    :param lines: list of lines
                  One line corresponds to one element in the lines-list and is one row in the txt-file.
    :return: calibration value
    :rtype: int
    """
    sum_of_numbers = 0
    for line in lines:
        if line:
            tens = _get_digit(line, True)
            units = _get_digit(line, False)
            sum_of_numbers += int(tens + units)
    return sum_of_numbers


def _get_digit(line: str, is_tens: bool):
    """
    :param line: is one row in the txt-file
    :param is_tens: flag
                    If it is True then the searched number is the ten else it is the unit
    :return: two numbers (tens merged with units) as str
    :rtype: str
    """
    index = 0 if is_tens else len(line) - 1

    while (is_tens and index < len(line)) or (not is_tens and index >= 0):
        sign = line[index]
        if sign.isdigit():
            return sign
        elif (is_tens and index >= 2) or (not is_tens and (len(line) - index) > 2):
            part_of_current_read_text = line[0:index + 1] if is_tens else line[index:len(line)]
            if "one" in part_of_current_read_text:
                return "1"
            elif "two" in part_of_current_read_text:
                return "2"
            elif "three" in part_of_current_read_text:
                return "3"
            elif "four" in part_of_current_read_text:
                return "4"
            elif "five" in part_of_current_read_text:
                return "5"
            elif "six" in part_of_current_read_text:
                return "6"
            elif "seven" in part_of_current_read_text:
                return "7"
            elif "eight" in part_of_current_read_text:
                return "8"
            elif "nine" in part_of_current_read_text:
                return "9"
        if is_tens:
            index += 1
        else:
            index -= 1


if __name__ == '__main__':
    data = get_file_content('puzzle_input.txt')
    calibration_value = get_calibration_value(data)
    print(calibration_value)
