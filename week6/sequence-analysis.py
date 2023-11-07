import math

DECIMAL_POINT = 4


def get_filename():
    return input()


def open_file(filename):
    try:
        return open(filename, "r")
    except FileNotFoundError:
        return ""


def valid_float(flaot_list):
    if len(flaot_list) >= 1:
        return flaot_list


def convert_to_float(filename):
    float_list = []
    for item in filename:
        try:
            float_num = float(item)
            float_list.append(float_num)
        except ValueError:
            pass

    return valid_float(float_list)


def get_sum(data: list):
    # loop over the list_data and calcualte the sum
    sf = 0
    sf_list = []
    # for each iteration add the current sum as a string to list of sumations
    for item in data:
        sf += item
        result = sf
        sf_list.append(round(result, DECIMAL_POINT))
    # return the list of sumations
    return sf_list


def get_median(data):
    list_length = len(data)
    list_devide_by_two = math.floor(list_length / 2)
    index = list_devide_by_two
    median_list = []

    if list_length % 2 == 0:
        data_points = []
        data_points.append(data[index - 1])
        data_points.append(data[index])
        resault = (data_points[0] + data_points[1]) / 2
        median_list.append(round(resault, DECIMAL_POINT))
    elif list_length % 2 == 1:
        median_list.append(data[index])
    return median_list


def proses_data(data: list):
    original_data = data
    float_sum = get_sum(data)
    sorted_data = sorted(data)
    middel_num = get_median(sorted_data)

    return [original_data, float_sum, sorted_data, middel_num]


def strinfify(data: list):
    # takes in a list of floats
    for row in data:
        return row
    # converts all items to strings


def print_data(data):
    for item in data:
        print(*item)


def main():
    file_name = get_filename()
    file_content = open_file(file_name)
    # the convert float also take in a validate function to check if there are any float to opertae on
    list_of_floats = convert_to_float(file_content)
    resault = proses_data(list_of_floats)
    print_data(resault)


main()
