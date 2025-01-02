class Leaderboard:
    def __init__(self):
        self.scores = {}

    def update(self, winner):
        if winner not in self.scores:
            self.scores[winner] = 0
        self.scores[winner] += 1

    def display(self):
        leaderboard_text = "\n".join([f"{player}: {score}" for player, score in self.scores.items()])
        return leaderboard_text
