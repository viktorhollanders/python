from string import punctuation

PUN = punctuation


def main():
    sentence_1 = input()
    sentence_2 = input()

    a_sent_dict = string_to_dict(sentence_1)
    b_sent_dict = string_to_dict(sentence_2)

    if a_sent_dict == b_sent_dict:
        print(f"{sentence_1} is an anagram of {sentence_2}.")
    else:
        print(f"{sentence_1} is not an anagram of {sentence_2}.")


def string_to_dict(sentence: str) -> dict:
    sentence_lower = sentence.lower()
    anagram_dict = {}

    for letter in sentence_lower:
        if letter not in PUN and letter != " ":
            if letter in anagram_dict:
                anagram_dict[letter] += 1
            else:
                anagram_dict[letter] = 1

    return anagram_dict


if __name__ == "__main__":
    main()
