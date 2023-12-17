class Player:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.goals = 0

    def add_goals(self, goals: str) -> int:
        self.goals = int(goals)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, Goals: {self.goals}"
