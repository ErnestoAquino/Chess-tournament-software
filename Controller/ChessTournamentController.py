import Model


class ChessTournamentController:
    def __init__(self):
        self.tournament = None

    def create_tournament(self, name: str, location: str):
        self.tournament = Model.Tournament(name = name, location = location)

    def register_player(self,
                        first_name: str,
                        last_name: str,
                        date_of_bird: str,
                        chess_national_id: str):
        player = Model.Player(first_name = first_name,
                              last_name = last_name,
                              date_of_bird = date_of_bird,
                              chess_national_id = chess_national_id)
        self.tournament.add_player(player)

    def start_tournament(self):
        pass
