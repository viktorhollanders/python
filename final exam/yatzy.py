from typing import List

MAX_DICE_RESULT = 6  # Assume a standard 6-sided die.


def get_counts(dice_results: List[int]) -> List[int]:
    """Counts how often each value appears.

    Returns a list of counts
    for each possible outcome on a die roll,
    where the first count in the list
    (at position 0 in the output list)
    indicates how many 1's appear
    in the given list of dice results,
    the second count (at position 1)
    indicates how many 2's appear, and so on.
    The count list is as long as there are sides on the dice.

    For example, if the dice list is [3, 3, 4, 4, 1],
    then the count list is [1, 0, 2, 2, 0, 0],
    indicating that the number 1 appears once,
    the numbers 3 and 4 appear twice each,
    but the numbers 2, 5 and 6 never appear.
    """

    counts = [dice_results.count(value) for value in range(1, MAX_DICE_RESULT + 1)]
    return counts


def check_yatzy(numbers):
    """
    checks if user has
    """
    for number in numbers:
        if number == 5:
            return 50


def check_three(numbers):
    """
    checks if user has three of a kind
    """
    for index, number in enumerate(numbers):
        if number >= 3:
            return 3 * (index + 1)


def check_two(numbers):
    """
    checks if the user has two of a kind and returns the higher pair if there is more than one pair
    """
    result = 0
    for index, number in enumerate(numbers):
        if number >= 2:
            current_number = 2 * (index + 1)
            if current_number > result:
                result = current_number
            else:
                continue

    return result


def main():
    user_input = input().split()
    dice_result = [int(result) for result in user_input]

    if len(dice_result) != 5:
        return

    while len(dice_result) == 5:
        value_counts = get_counts(dice_result)

        three = check_three(value_counts)
        pairs = check_two(value_counts)

        if check_yatzy(value_counts):
            print(50)

        elif three >= 0:
            print(three)
        elif pairs > 0:
            print(pairs)
        else:
            print(0)

        user_input = input().split()
        dice_result = [int(result) for result in user_input]


if __name__ == "__main__":
    main()
