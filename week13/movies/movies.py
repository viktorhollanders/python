# Constants

VALID_OPTIONS = ["1", "2", "3"]
ACTIONS = [
    "Movies in alphabetical order",
    "Titles in given year",
    "Modify all ratings",
]


def open_file(filename):
    """
    Opens the file with the given file name.
    Returns the corresponding file stream, or None if the file cannot be opened.
    """
    try:
        file_stream = open(filename)
        return file_stream
    except FileNotFoundError:
        return None


def menu():
    print(f"\n{'*' * 31}")
    for option, action in zip(VALID_OPTIONS, ACTIONS):
        print(f"{option}. {action}")
    print(f"{'*' * 31}\n")


def sort_movies_by_title(list):
    """
    Sorts list in alphabetic order
    """
    sorted_list = sorted(list, key=lambda x: x[0])
    for item in sorted_list:
        title, rating, year = item
        print(f"{title:<50}{float(rating):>6.2f}{year:>6}")


def display_move_by_year(list, year):
    """
    Sorts the movies by year and prints them out
    """

    for item in list:
        if item[2] == year:
            print(f"{item[0]}")


def update_rating(list, rating):
    """
    Update the rating of the movies and return the
    updated list
    """
    updated_list = []

    for item in list:
        item[1] = float(item[1]) + rating
        updated_list.append(item)
    return updated_list


# main program
def main():
    file_input = input("Enter filename:\n")
    movie_data = open_file(file_input)

    if movie_data is None:
        print(f"\nFile {file_input} not found!")
        quit()

    menu()
    user_input = input("Enter your selection:\n")
    movie_list = [item.strip().split(";") for item in movie_data]

    while user_input in VALID_OPTIONS:
        movie_list = movie_list

        if user_input == VALID_OPTIONS[0]:
            sort_movies_by_title(movie_list)

        if user_input == VALID_OPTIONS[1]:
            by_year = input("Enter year:\n")
            display_move_by_year(movie_list, by_year)

        if user_input == VALID_OPTIONS[2]:
            rating = float(input("Enter modifier for ratings:\n"))
            update_rating(movie_list, rating)

        menu()
        user_input = input("Enter your selection:\n")


if __name__ == "__main__":
    main()
