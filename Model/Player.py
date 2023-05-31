
class Player:
    score: float = 0

    def __init__(self, first_name: str, last_name: str, date_of_bird: str):
        self.first_name = first_name.lower()
        self.last_name = last_name.upper()
        self.date_of_bird = date_of_bird

    def update_score(self, score: float):
        self.score += score
