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
    """
    :param lines: list of lines
                  One line corresponds to one element in the lines-list and is one row in the txt-file.
    :return: calibration value
    :rtype: int
    """
    sum_of_numbers = 0
    for line in lines:
        numbers_of_current_line = []
        for sign in line:
            if sign.isdigit():
                numbers_of_current_line.append(sign)
        if numbers_of_current_line:
            if len(numbers_of_current_line) >= 1:
                tens = numbers_of_current_line[0]
                if len(numbers_of_current_line) == 1:
                    units = tens
                else:
                    units = numbers_of_current_line[len(numbers_of_current_line) - 1]
                sum_of_numbers += int(tens + units)
    return sum_of_numbers


if __name__ == '__main__':
    data = get_file_content('puzzle_input.txt')
    calibration_value = get_calibration_value(data)
    print(calibration_value)
