class Question:
    def __init__(self, question, answer="") -> None:
        self.__question_str = question
        self.__answer_str = answer

    def __str__(self) -> str:
        """
        Return the correct answer
        """
        return f"Q: {self.__question_str} A: {self.__answer_str}"

    def set_answer(self, answer):
        """
        Sets the answer from teh multiple chois class
        """
        self.__answer_str = answer

    def get_question(self):
        return self.__question_str

    def check_answer(self, respomse) -> bool:
        return respomse.lower().strip() == self.__answer_str.lower().strip()
