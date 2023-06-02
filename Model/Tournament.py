import datetime
import Model


class Tournament:
    players = []
    rounds = []
    end_datetime: str
    description: str
    number_of_rounds: int
    current_round: int = 0

    def __init__(self, name: str, location: str, number_of_rounds=4):
        self.name = name
        self.location = location
        self.start_date = datetime.datetime.now().date()
        self.number_of_rounds = number_of_rounds

    def add_player(self, player: Model.Player):
        self.players.append(player)

    def write_end_date(self):
        self.end_datetime = str(datetime.datetime.now().date())

    def write_description(self, description: str):
        self.description = description
