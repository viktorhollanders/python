def main():
    user_input = get_user_input()
    integer_list = convert_to_int(user_input)
    missing_ints = find_missing_ints(integer_list)

    print(user_input)
    print(integer_list)
    print(missing_ints)


def get_user_input():
    get_input = input()
    input_list = get_input.split()
    return input_list


def convert_to_int(a_list: list[str]) -> list[int]:
    list_of_ints = []
    for i in a_list:
        if i.isdigit():
            to_int = int(i)
            list_of_ints.append(to_int)
    return list_of_ints


def find_missing_ints(a_list: list[int]) -> list[int]:
    missing_inst = []

    try:
        get_max = max(a_list)
        for i in range(0, get_max + 1):
            if i not in a_list:
                missing_inst.append(i)

        return missing_inst
    except ValueError:
        return missing_inst


if __name__ == "__main__":
    main()
