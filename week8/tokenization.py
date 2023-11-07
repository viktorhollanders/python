# open file
# get data from file
# split data


# count the words
# count the tokens words + ocurances . , ! ?
def main():
    file_data = get_data()
    if file_data == None:
        return ""
    word_list = extract_data(file_data)
    word_and_token_count = count(word_list)

    # unpack the word count and token rount returned by the count functions
    word_count, token_count = word_and_token_count

    print(word_count)
    print_word(word_list)
    print(token_count + word_count)
    print_token(word_list)


def get_data():
    try:
        user_input = input().strip()
        file_data = open(user_input, "r")

        return file_data
    except FileNotFoundError:
        return 


def extract_data(file: str) -> list[str]:
    token_list = []
    for word in file:
        words = word.strip().split()
        token_list.extend(words)

    return token_list


def count(a_list: list):
    word_count = 0
    token_count = 0
    symbols = ".,!?"

    for word in a_list:
        word_count += 1
        for token in word:
            if token in symbols:
                token_count += 1

    return (word_count, token_count)


def print_word(word_list: list) -> str:
    for word in word_list:
        print(word)


def print_token(word_list: list) -> str:
    for word in word_list:
        QUESTIONMARK = "?"
        DOT = "."
        COMMA = ","
        EXLEMATION = "!"

        if word[-1] == QUESTIONMARK:
            print(word[:-1])
            print(QUESTIONMARK)
        if word[-1] == DOT:
            print(word[:-1])
            print(DOT)
        if word[-1] == COMMA:
            print(word[:-1])
            print(COMMA)
            
        if word[-1] == EXLEMATION:
            print(word[:-1])
            print(EXLEMATION)
        if (
            word[-1] != QUESTIONMARK
            and word[-1] != DOT
            and word[-1] != COMMA
            and word[-1] != EXLEMATION
        ):
            print(word)


if __name__ == "__main__":
    main()
