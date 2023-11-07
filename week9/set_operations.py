from string import punctuation

UI = False


def main():
    filename1 = input("Enter the name of the first file:\n" if UI else "")
    filename2 = input("Enter the name of the second file:\n" if UI else "")

    data1 = open_file(filename1)
    data2 = open_file(filename2)

    set_a = create_set(data1)
    set_b = create_set(data2)

    print_sets(set_a, set_b)


def open_file(filename):
    with open(filename) as file:
        words = []
        for line in file:
            words.extend(line.split())

    return words


def create_set(file):
    return {item.strip(punctuation) for item in file}


def print_sets(set_a, set_b):
    common_words = set_a & set_b
    uniqe_words = set_a ^ set_b
    only_in_a = set_a - set_b

    print(f"\nThe two files have {len(common_words)} words in common.")
    display_result(common_words)

    print(
        f"\nThere are {len(uniqe_words)} words that are only in either file but not both."
    )
    display_result(uniqe_words)

    print(f"\nThere are {len(only_in_a)} words that only appear in the first file.")
    display_result(only_in_a)


def display_result(a_set: set):
    sorted_list = sorted(a_set)

    print("These words are as follows:")
    if len(sorted_list) < 2:
        print("".join(sorted_list))
    else:
        print(", ".join(sorted_list[:-1]), end=" ")
        print(f"and {sorted_list[-1]}.")


if __name__ == "__main__":
    main()
