from player import Player


class Team:
    def __init__(self, team_name: str) -> None:
        self.team_name = team_name
        self.players = []
        self.most_goals = []

    def add_player(self, player: Player) -> None:
        self.players.append(player)

    def most_goals_player(self):
        most_goals = max(self.players, key=lambda p: p.goals)
        return most_goals

    def __add__(self, other):
        new_team = Team(f"{self.team_name}+{other.team_name}")
        players = self.players + other.players
        for player in players:
            new_team.add_player(player)
        return new_team

    def __str__(self) -> str:
        output = f"{self.team_name}:"

        sorted_by_goals = sorted(self.players, key=lambda p: p.goals, reverse=True)
        for player in sorted_by_goals:
            output += f"\n\t{player}"
        return output
