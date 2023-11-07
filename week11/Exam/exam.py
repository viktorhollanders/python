class Exam:
    def __init__(self) -> None:
        self.points = 0
        self.number_of_questions = 0
        self.question_list = []

    def add_question(self, question):
        """
        Adds the questions to the exam question list and updates the number of questions
        """
        self.number_of_questions += 1
        self.question_list.append(question)

    def get_points(self):
        """
        Reeturns the point of the exam
        """
        return self.points

    def get_num_questions(self):
        """
        Get the number of qurestions in the exam
        """
        return len(self.question_list)

    def take(self):
        """
        This functions initalizes take exam and updates the points if the question is aswerd corectly
        """
        for question in self.question_list:
            print(question.get_question())
            user_answer = input()
            answer = question.check_answer(user_answer)
            print(f"{answer}\n")
            if answer:
                self.points += 1

    def __str__(self) -> str:
        output = ""
        for question in self.question_list:
            if output != "":
                output += "\n"
            output += f"{question}"
        return output
