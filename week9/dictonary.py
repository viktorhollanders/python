def main():
    dictionary = {}

    add_word(dictionary)
    while more():
        add_word(dictionary)

    display_result(dictionary)


def add_word(dictionary: dict) -> None:
    """Asks the user for a word and definition and stores it in the dictionary."""
    word = input()
    definition = input()
    dictionary[word] = definition


def more() -> bool:
    """Checks if the user wants to add more words."""
    aks_to_add = input().lower()

    if aks_to_add == "y":
        return True
    return False


def display_result(dictionary: dict) -> None:
    """Prints the words in alphabetical order, along with the definitions."""
    key_val_list = []

    for key, val in dictionary.items():
        key_val_list.append((key, val))

    key_val_list.sort()

    for key, val in key_val_list:
        print()
        print(f"{key}:")
        print(f"    {val}")


if __name__ == "__main__":
    main()
