def create_tuple(address_list):
    tuple_list = []

    for item in address_list:
        split_list = item.split()
        if len(split_list) > 1:
            address = split_list[0]
            number = split_list[1]
            tuple_list.append((address, number))

    return tuple_list


address_list = []
user_input = input()

while user_input.lower() != "q":
    if len(user_input) > 1:
        address_list.append(user_input)
    user_input = input()


# create a tuple from a list
output = create_tuple(address_list)


print(address_list)
print(output)

# put the list into a tuple conatining name and number
