import Model


class Player:
    score: float = 0
    played_players = []
    id_played = []

    def __init__(self, first_name: str,
                 last_name: str,
                 date_of_birth: str,
                 chess_national_id: str,
                 score: float = 0):
        self.first_name = first_name.lower()
        self.last_name = last_name.upper()
        self.date_of_birth = date_of_birth
        self.chess_national_id = chess_national_id
        self.score = score
        self.played_players = []
        self.id_played = []

    def update_score(self, score: float):
        self.score += score

    def test_print_opponents(self):
        if len(self.played_players) != 0:
            for player in self.played_players:
                print(f"Ya he  combatido a: {player.first_name}")

    def test_print_id_opponents(self):
        for id in self.id_played:
            print(f"{id}")