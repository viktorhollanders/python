def file_data(file_name):
    try:
        with open(file_name, "r") as file_name:
            data_file = file_name
            return data_file
    except FileNotFoundError:
        return