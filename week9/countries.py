def main():
    countries = {}

    add_to_dict(countries)

    show_resault(countries)
    while again():
        show_resault(countries)


def open_file():
    while True:
        file_name = input()

        try:
            with open(file_name, "r") as file:
                content = file.readlines()
                return content
        except FileNotFoundError:
            print(f"File {file_name} not found!")


def add_to_dict(countries):
    data = open_file()
    for word in data:
        strip_word = word.strip()
        word_len = len(strip_word)

        countries[strip_word] = int(word_len)


def again():
    """Checks if the user wants to see more countries."""
    see_more = input().lower()

    if see_more == "y":
        return True
    return False


def show_resault(countries: dict):
    countrie_len = int(input())
    output = []

    for country, length in countries.items():
        if length == countrie_len:
            output.append(country)
    if countrie_len in countries.values():
        print(", ".join(output))
    else:
        print(f"No country name of length {countrie_len} exists.")


if __name__ == "__main__":
    main()
