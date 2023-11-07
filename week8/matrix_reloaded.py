# Mister Anderson welcom to my MATRIX
def main():
    tuple_of_lists = get_input()
    create_the_matrix(tuple_of_lists)


def get_input():
    count = 0

    list_a = []
    list_b = []

    while count < 12:
        user_input = input()
        user_input_int = int(user_input)

        if count < 6:
            list_a.append(user_input_int)
        if count >= 6:
            list_b.append(user_input_int)
        count += 1

    return (list_a, list_b)


def create_the_matrix(list_tuple: tuple[list]) -> list[list]:
    list_a, list_b = list_tuple

    list_a = create_matrix_parts(list_a)
    list_b = create_matrix_parts(list_b)

    sum_of_AB = []
    for i in range(0, 2):
        line = []
        for j in range(0, 3):
            resault = list_a[i][j] + list_b[i][j]
            line.append(resault)
        sum_of_AB.append(line)
    print(list_a)
    print(list_b)
    print(sum_of_AB)


def create_matrix_parts(int_list: list) -> list[list]:
    fist = int_list[:3]
    last = int_list[3:]
    int_list.clear()
    int_list.append(fist)
    int_list.append(last)
    return int_list


if __name__ == "__main__":
    main()
