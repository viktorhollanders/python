# Constants
TWO = 2


def open_file(file_name):
    try:
        file = open(file_name)
        file_stream = file.readlines()
        return file_stream
    except FileNotFoundError:
        return None


def create_competitors_dict(file) -> dict:
    """
    create a dictionary with the name of players and
    their total score
    """
    competitors_dict = dict()
    for line in file:
        list_of_line_items = line.strip().split()
        name = " ".join(list_of_line_items[:-1])

        if name in competitors_dict:
            competitors_dict[name].append(float(list_of_line_items[2]))
        else:
            competitors_dict[name] = [float(list_of_line_items[2])]
    return competitors_dict


def create_average_score_list(competitors_dict: dict) -> list:
    """
    Create a list of the players average score
    """
    winner_list = []
    for name, scores in competitors_dict.items():
        average = sum(scores) / len(scores)
        winner_list.append([name, average])
    return winner_list


def print_results(winner: list, competitors_dict: dict) -> None:
    """
    Prints the results from the competition.
    It there is a player with more than one score
    the function will also print a defined winner.
    """

    has_two = False
    for name, scores in competitors_dict.items():
        # checks if the score is grater than two
        if len(scores) >= TWO:
            has_two = True

        # converts the scores to a string
        score = " ".join([str(score) for score in scores])
        print(f"{name:<20}Throws: {score}")

    if has_two:
        name, score = winner
        print(f"{name}: {score:.2f}")


def main():
    user_input = input()
    file = open_file(user_input)

    competitors_dict = create_competitors_dict(file)
    winner_list = create_average_score_list(competitors_dict)

    winner = max(winner_list, key=lambda p: p[1])
    print_results(winner, competitors_dict)


if __name__ == "__main__":
    main()
