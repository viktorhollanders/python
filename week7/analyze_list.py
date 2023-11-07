def main():
    input_list = get_correct_data()
    list_data = get_data(input_list)
    print_output(list_data)


def get_correct_data() -> list:
    """Asks user repeatedly for input until valid."""

    user_input = input()

    while get_data(user_input) == None:
        user_input = input()

    return user_input


def get_data(user_input: list):
    """Returns a list of positive integers input by the user.

    Returns None if the input contains non-integers or integers < 0.
    """
    try:
        to_list = user_input.split(",")
        list_of_ints = [int(item) for item in to_list]

        for item in list_of_ints:
            if item < 0:
                raise ValueError
            return list_of_ints
    except ValueError:
        print("Incorrect input! Please try again.")
        return None


def print_output(input_data: list):
    get_min = min(input_data)
    get_max = max(input_data)
    get_avrage = avrage(input_data)

    original_list = input_data
    print(f"Input list: {original_list}")

    sorted_list = sort_list(input_data)
    print(f"Sorted list: {sorted_list}")

    get_composit = composit_list(input_data)
    print(f"Composite list: {get_composit}")

    print(f"Min: {get_min}, Max: {get_max}, Average: {round(get_avrage, 2)}")


def is_prime(n: int) -> bool:
    """Returns True if the given positive number is prime and False otherwise."""

    if n < 2:
        return False

    for i in range(
        2, int(n**0.5) + 1
    ):  # Feel free to improve this function if you like.
        if n % i == 0:
            return False

    return


def sort_list(a_list: list) -> list:
    a_list.sort()
    return a_list


def composit_list(a_list: list) -> list:
    for item in a_list:
        composit_numbers = []
        if item not in composit_numbers and is_prime(item):
            composit_numbers.append(item)
        return composit_numbers


def avrage(a_list) -> int:
    count = 0
    total_sum = 0

    for item in a_list:
        total_sum += item
        count += 1

    return total_sum / count


if __name__ == "__main__":
    main()
