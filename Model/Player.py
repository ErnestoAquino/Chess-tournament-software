
class Player:
    score: float = 0

    def __init__(self, first_name: str,
                 last_name: str,
                 date_of_birth: str,
                 chess_national_id: str):
        self.first_name = first_name.lower()
        self.last_name = last_name.upper()
        self.date_of_birth = date_of_birth
        self.chess_national_id = chess_national_id

    def update_score(self, score: float):
        self.score += score
