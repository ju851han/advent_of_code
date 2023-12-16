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
