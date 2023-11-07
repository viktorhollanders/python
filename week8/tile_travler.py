from typing import Tuple


# Constants
NORTH = "n"
EAST = "e"
SOUTH = "s"
WEST = "w"

STARTING_LOCATION = (1, 1)
FINAL_DESTINATION = (3, 1)
coins = 0
has_visited = False


def main():
    play()


def play():
    location = STARTING_LOCATION
    while location != FINAL_DESTINATION:
        location = play_one_move(location)

    print(f"Victory! Total coins {coins}.")
    play_again_input = input("Play again (y/n):\n").lower()
    play_again(play_again_input)


def play_again(user_input):
    if user_input == "y":
        reset_game()
        main()
    else:
        return ""


def reset_game():
    global STARTING_LOCATION
    global FINAL_DESTINATION
    global coins
    global has_visited

    STARTING_LOCATION = (1, 1)
    FINAL_DESTINATION = (3, 1)
    coins = 0
    has_visited = False


def play_one_move(location: Tuple[int]) -> Tuple[int]:
    """Plays one move of the game.

    Returns updated location.
    """
    global has_visited

    coin_room = is_coin_room(location)

    valid_directions = find_directions(location)
    # this if statmentas fyst after the else statment
    # but it still pased the test for project 1 ask why
    if coin_room and not has_visited:
        get_coin()
    direction = get_direction(valid_directions)

    if direction in valid_directions:
        location = move(direction, location)
        has_visited = False
    else:
        print("Not a valid direction!")

    return location


def find_directions(location: Tuple[int]) -> Tuple[str]:
    """Returns valid directions as a string given the supplied location."""

    if location == (1, 1):
        valid_directions = (NORTH,)
    elif location == (1, 2):
        valid_directions = NORTH, EAST, SOUTH
    elif location == (1, 3):
        valid_directions = EAST, SOUTH
    elif location == (2, 1):
        valid_directions = (NORTH,)
    elif location == (2, 2):
        valid_directions = SOUTH, WEST
    elif location == (2, 3):
        valid_directions = EAST, WEST
    elif location == (3, 2):
        valid_directions = NORTH, SOUTH
    elif location == (3, 3):
        valid_directions = SOUTH, WEST

    return valid_directions


def get_direction(valid_directions: Tuple[str]) -> str:
    print_directions(valid_directions)
    return input("Direction:\n").lower()


def print_directions(available_directions: Tuple[str]) -> None:
    print("You can travel: ", end="")

    one_done_already = False
    for direction in available_directions:
        if one_done_already:
            print(" or ", end="")

        if direction == NORTH:
            print("(N)orth", end="")
        elif direction == EAST:
            print("(E)ast", end="")
        elif direction == SOUTH:
            print("(S)outh", end="")
        elif direction == WEST:
            print("(W)est", end="")

        one_done_already = True

    print(".")


def move(direction: str, location: Tuple[int]) -> Tuple[int]:
    """Returns updated location given the direction."""

    x, y = location

    if direction == NORTH:
        y += 1
    elif direction == SOUTH:
        y -= 1
    elif direction == EAST:
        x += 1
    elif direction == WEST:
        x -= 1

    return x, y


def is_coin_room(current_room):
    coin_rooms = [(1, 2), (2, 2), (2, 3), (3, 2)]

    if current_room in coin_rooms:
        return True
    return False


def get_coin():
    global coins
    global has_visited
    user_input = input("Pull a lever (y/n):\n").lower()
    if user_input == "y":
        coins += 1
        print(f"You received 1 coin, your total is now {coins}.")
        has_visited = True
        return
    else:
        has_visited = True
        return


if __name__ == "__main__":
    main()

# create a reset game function
