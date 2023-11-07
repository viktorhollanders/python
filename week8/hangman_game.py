def main():
    try:
        file = get_file()
    except FileNotFoundError:
        return
    word_list = get_file_data(file)
    secret_word = set_secret_word(word_list)
    hide_sw = ["-" for _ in secret_word]

    play_game(secret_word, hide_sw)


def get_file():
    """Opens a file with and returns its content"""
    user_input = input()
    return open(user_input, "r")


def get_file_data(file_data) -> list[str]:
    word_list = [word.strip() for word in file_data]
    return word_list


def set_secret_word(word_list: list[str]) -> str:
    sw_pos = int(input()) - 1
    return word_list[sw_pos]


def play_game(word: str, secret: list):
    for count in range(12):
        is_done = check_winner(secret)
        if is_done:
            break
        print_word(secret)
        char, a_bool = check_letter(word)
        print(f"Guess {count + 1}/12")

        if a_bool:
            print(f"Correct letter {char}!")
            secret = update_letter(char, word, secret)
        else:
            print(f"Incorrect letter {char}!")
        count += 1
    else:
        print_word(secret)
        print(f"You lost! The secret word was {word}")


def check_letter(word: list) -> tuple():
    """checks if a user input is in word 
       and returns a tuple with the char and True or Fasle
    """
    user_input = input()
    return (user_input, True) if user_input in word else (user_input, False)


def print_word(word):
    output = " ".join(word)
    print(f"Secret word: {output}")


def update_letter(char_input: str, word: list, hidden_word: list):
    for i in range(len(word)):
        if word[i] == char_input:
            hidden_word[i] = char_input
    return hidden_word


def check_winner(hidden):
    if "-" not in hidden:
        output = " ".join(hidden)
        print(f"Secret word: {output}")
        print("You won!")
        return True
    return False


if __name__ == "__main__":
    main()
