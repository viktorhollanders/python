def open_file(file_name):
    try:
        with open(file_name) as file:
            file_stream = file.readlines()
            return file_stream
    except FileNotFoundError:
        return None


def display_result(results):
    for result in results:
        team1, team2, score1, score2 = result
        score = f"{score1}:{score2}"
        print(f"{team1:>13}{score:^5}{team2:<13}")


def show_standings(games):
    show_standing = input("Show standings? (y/n): ").lower()

    if show_standing != "y":
        return
    print("show")


def main() -> None:
    file_input = input("Enter filename: ")
    file_stream = open_file(file_input)
    games = [game.strip().split(";") for game in file_stream]

    display_result(games)
    show_standings(games)


if __name__ == "__main__":
    main()
