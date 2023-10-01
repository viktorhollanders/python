# Write a program that reads a floating point number
# sequence from an input file and outputs various information about the sequence.
# Outpur
#   The output is either nothing, in the case were the input data file does not contain any floats or if it cannot be opened
#   1. The numbers in the sequence
#   2. The cumulative sum of the numbers in the sequence
#   3. The sorted version (ascending order) of the numbers in the sequence
#   4. The median of the sequence
#   All numbers should be rounded to four digits after the decimal point.

# 1. let user input file name
# 2. open the file
# 3. check file
# 4. read file
# 5. display output


def get_filename():
    return input("Enter a file name: ")


def open_file(filename):
    try:
        return open(filename, "r")
    except FileNotFoundError:
        return "File not found"


def valid_float(flaot_list):
    if len(flaot_list) > 1:
        return flaot_list


def convert_to_float(filename):
    float_list = []
    for item in filename:
        try:
            if float(item):
                float_num = float(item.strip())
                float_list.append(float_num)
        except ValueError:
            pass

    return valid_float(float_list)

def list_of_sums(data):
    # loop over the list_data and calcualte the sum
    #for each iteration add the current sum as a string to list of sumations 
    # return the list of sumations
    pass


def proses_data(data: list):
    #   1. The numbers in the sequence
    original_data = data
    #   2. The cumulative sum of the numbers in the sequence
    cumalitive_sum = list_of_sums(data)


    #   3. The sorted version (ascending order) of the numbers in the sequence
    sorted_data = sorted(data)
    #   4. The median of the sequence
    #   All numbers should be rounded to four digits after the decimal point.
    print(original_data)
    print(sorted_data)


def print_data(data):
    pass


def main():
    file_name = get_filename()
    file_content = open_file(file_name)
    # the convert float also take in a validate function to check if there are any float to opertae on
    list_of_floats = convert_to_float(file_content)
    proses_data(list_of_floats)


main()
