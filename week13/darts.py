# Constants
STARTING_SCORE = 301
WINNING_SCORE = 0
ONE = "1"
TWO = "2"


def main():
    player1_total_score = STARTING_SCORE
    player2_total_score = STARTING_SCORE

    while player1_total_score != 0 or player2_total_score != 0:
        player1_score = get_player_input(ONE)
        player1_total_score = update_score(ONE, player1_score, player1_total_score)

        if player1_total_score == WINNING_SCORE:
            declare_winner(ONE)
            break

        player2_score = get_player_input(TWO)
        player2_total_score = update_score(TWO, player2_score, player2_total_score)

        if player2_total_score == WINNING_SCORE:
            declare_winner(TWO)
            break


def validate_input(input):
    """
    Validates the player input
    """
    try:
        return int(input)
    except ValueError:
        print("Invalid input!")
        return None


def get_player_input(player):
    """
    Gets the player input
    """
    user_input = input(f"Input points for Player {player}: \n")
    while validate_input(user_input) is None:
        user_input = input(f"Input points for Player {player}: \n")
    return int(user_input)


def update_score(player, player_score, total_score):
    if player_score > total_score:
        print(f"Player {player} remaining points: {total_score}")
        return total_score
    else:
        total_score = total_score - player_score
        print(f"Player {player} remaining points: {total_score}")

    return total_score


def declare_winner(player):
    print(f"Player {player} won!")


if __name__ == "__main__":
    main()
