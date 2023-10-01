#!/usr/bin/env python3


def main():
    # implement your code here
    user_input = input().split(" ")
    bags = number_of_bags(user_input[0])
    bag_status = find_item(bags, user_input[1])
    print(display_bag_status(bag_status))


def number_of_bags(user_input):
    bag_list = []
    bag_list = input().split(" ")
    return bag_list


def find_item(list_of_items: list, item):
    return list_of_items.index(item) + 1


def display_bag_status(item_index):
    if item_index == 1:
        return "fyrst"
    elif item_index == 2:
        return "naestfyrst"
    else:
        return f"{item_index} fyrst"


if __name__ == "__main__":
    main()
