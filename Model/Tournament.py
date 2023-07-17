import random
from tinydb import TinyDB
from typing import Dict
from typing import Any
import datetime
import Model
import DataBaseManager


class Tournament:
    DATA_BASE = TinyDB("Data/Players/Players.json")
    players = []
    rounds = []
    description: str
    number_of_rounds: int
    current_round: int = 0

    def __init__(self, name: str, location: str, number_of_rounds=4):
        self.name = name.capitalize()
        self.location = location.capitalize()
        self.start_date = str(datetime.datetime.now().date())
        self.number_of_rounds = number_of_rounds
        self.end_datetime = None
        self.database_manager = DataBaseManager.DataBaseManager()

    def add_player(self, player: Model.Player):
        self.players.append(player)

    def write_end_date(self):
        self.end_datetime = str(datetime.datetime.now().date())

    def write_description(self, description: str):
        self.description = description

    def add_round(self, round: Model.Round):
        self.rounds.append(round)

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
        self.players = self.database_manager.load_all_players()

    def shuffle_players(self):
        random.shuffle(self.players)

    def sort_players(self):
        self.players = sorted(self.players, key=lambda x: x.score, reverse=True)

    def to_dictionary(self) -> Dict[str, Any]:
        dictionary = {
            "name": self.name,
            "location": self.location,
            "number_of_rounds": self.number_of_rounds,
            "start_date": self.start_date,
            "current_round": self.current_round,
            "rounds": [round.to_dictionary() for round in self.rounds],
            "players": [player.to_dictionary() for player in self.players]
        }
        if self.end_datetime is not None:
            dictionary["end_datetime"] = self.end_datetime
        return dictionary

    @classmethod
    def load_from_dictionary(cls, data: Dict[str, Any]) -> 'Tournament':
        tournament = cls(data["name"], data["location"], data["number_of_rounds"])
        tournament.start_date = data["start_date"]
        tournament.current_round = data["current_round"]
        if "end_datetime" in data:
            tournament.end_datetime = data["end_datetime"]
        tournament.players = [Model.Player.load_from_dictionary(player_data) for player_data in data["players"]]
        tournament.rounds = [Model.Round.load_from_dictionary(round_data) for round_data in data["rounds"]]
        return tournament
