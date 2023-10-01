#!/usr/bin/env python3
def split_input(input_str: str, seperator) -> list:
    return input_str.split(seperator)


def count_grades(a_list):
    count = 0

    for item in a_list:
        if "-" in item:
            num_range = split_input(item, "-")
            START = int(num_range[0])
            STOP = int(num_range[1])
            for num in range(START, STOP + 1):
                count += 1
        else:
            count += 1

    print(count)


user_input = input()
input_list = split_input(user_input, ";")
count_grades(input_list)
