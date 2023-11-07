def main():
    user_input = get_user_input().strip()
    # get user input

    file_data = open_file(user_input)
    inflation_data = get_data(file_data)
    print_output(inflation_data)


def get_user_input():
    user_input = input()
    return user_input


def open_file(user_input):
    try:
        file_data = open(user_input, "r")
        return file_data
    except FileNotFoundError:
        print("")
        return ""


def get_data(file: str) -> list:
    tuple_list = []
    for line in file:
        to_list = line.strip().split()
        tuple_list.append(create_tuple_list(to_list))

    return tuple_list


def create_tuple_list(a_list: list) -> tuple:
    return (a_list[0], float(a_list[1]))


def get_years(a_list: list[tuple[str, str]]) -> str:
    list_of_years = []
    for i in a_list:
        year, num = i

        year = year[:4]
        if year not in list_of_years:
            list_of_years.append(year[:4])

    return list_of_years

def get_first(a_list: list[tuple[str, str]], year: str) -> float:
    list_ofNumbers = []

    for i in a_list:
        years, num = i

        if year in years:
            list_ofNumbers.append(num)

    return list_ofNumbers[0]

def get_last(a_list: list[tuple[str, str]], year: str) -> float:
    list_ofNumbers = []

    for i in a_list:
        years, num = i

        if year in years:
            list_ofNumbers.append(num)

    return list_ofNumbers[-1]




def print_output(inflation_data):
    for item in inflation_data:
        print(item)

    years = get_years(inflation_data)
    for year in years:
        min_number = get_first(inflation_data, year)
        max_number = get_last(inflation_data, year)
        print((int(year), min_number, max_number))

    for year in years:
        min_number = get_first(inflation_data, year)
        max_number = get_last(inflation_data, year)

        inflation = (
            ((float(max_number) - float(min_number)) / float(min_number))
        ) * 100
        print((int(year), round(inflation, 2)))


if __name__ == "__main__":
    main()
