class Hangman:
    def __init__(self, word: str) -> None:
        self.word = word
        self.incorrect_guess = 0
        self.corect_word = ["_"] * len(word)

    def guess_letter(self, letter: str) -> bool:
        # if the letter exixts then return true
        if letter.upper() in self.word:
            self.update_word(letter)
            return True
        else:
            self.incorrect_guess += 1
            return False

    def update_word(self, letter: str):
        # for every letter in the word i want to update that word
        for index, char in enumerate(self.word.upper()):
            if char == letter:
                self.corect_word[index] = letter

    def __str__(self) -> str:
        joined_word = " ".join([item for item in self.corect_word])
        return f"{joined_word}\nNumber of incorrect guesses: {self.incorrect_guess}"



