import random

from tinydb import TinyDB
import datetime
import Model


class Tournament:
    DATA_BASE = TinyDB("Data/Players/Players.json")
    players = []
    rounds = []
    end_datetime: str
    description: str
    number_of_rounds: int
    current_round: int = 0

    def __init__(self, name: str, location: str, number_of_rounds=4):
        self.name = name.capitalize()
        self.location = location.capitalize()
        self.start_date = datetime.datetime.now().date()
        self.number_of_rounds = number_of_rounds

    def add_player(self, player: Model.Player):
        self.players.append(player)

    def write_end_date(self):
        self.end_datetime = str(datetime.datetime.now().date())

    def write_description(self, description: str):
        self.description = description

    def add_match(self, match: Model.Match):
        self.rounds.append(match)

    def save_players(self):
        local_players = self.DATA_BASE.table("Players")
        for player in self.players:
            local_players.insert({"first_name": player.first_name,
                                  "last_name": player.last_name,
                                  "date_of_birth": player.date_of_birth,
                                  "chess_national_id": player.chess_national_id,
                                  "score": player.score})

    def load_players(self):
        local_players = self.DATA_BASE.table("Players")
        results = local_players.all()
        for result in results:
            player = Model.Player(first_name = result["first_name"],
                                  last_name = result["last_name"],
                                  date_of_birth = result["date_of_birth"],
                                  chess_national_id = result["chess_national_id"],
                                  score = result["score"])
            self.players.append(player)

    def shuffle_players(self):
        random.shuffle(self.players)

    def create_first_round(self):
        self.shuffle_players()
        first_round = Model.Round(name = "Round 1")
        for i in range(0, len(self.players), 2):
            match = Model.Match(player1 = self.players[i], player2 = self.players[i + 1])
            first_round.add_mach(match)
        self.rounds.append(first_round)

    def start(self):
        self.shuffle_players()
        self.create_first_round()
