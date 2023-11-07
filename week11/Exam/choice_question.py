from question import Question


class ChoiceQuestion(Question):
    def __init__(self, question) -> None:
        super().__init__(question, "")
        self.question = question
        self.choices = []

    def add_choice(self, choice, a_bool=False):
        self.choices.append(choice)
        if a_bool:
            super().set_answer(len(self.choices))

    def get_question(self):
        """
        Gets the index and item from the choise list loop over them and print the index + 1 becase of the lists zero indexing. On the last one we dont print a new line.
        """
        output = f"{self.question}"
        for index, choice in enumerate(self.choices):
            output += f"\n{index + 1}. {choice}"

        return output

    def check_answer(self, answer):
        """
        Checks if the answe is correct and return true if the are and false otherwise
        """
        return int(answer) == int(self._Question__answer_str)

    def __str__(self):
        return f"Q: {self.question} A: {self._Question__answer_str}"
