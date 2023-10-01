#!/usr/bin/env python3

num_list = []


def main():
    # implement your code here

    list_lengt = int(input())
    count = 1

    while count <= list_lengt:
        user_input = int(input())
        add_item(user_input, num_list)
        count += 1

    reverse_list(num_list)


def add_item(item, list):
    return list.append(item)


def reverse_list(list):
    reverse_list = list[::-1]
    for value in reverse_list:
        print(value)


if __name__ == "__main__":
    main()
