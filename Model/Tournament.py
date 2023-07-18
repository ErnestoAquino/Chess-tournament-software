import random
from typing import Dict
from typing import Any
from typing import List
import datetime
import Model
import DataBaseManager


class Tournament:
    """
    Represents a tournament.

    Attributes:
        players (List[Model.Player]): List of players participating in the tournament.
        rounds (List[Model.Round]): List of rounds in the tournament.
        description (str): Description of the tournament.
        number_of_rounds (int): Number of rounds in the tournament.
        current_round (int): Current round of the tournament.
    """
    players: List[Model.Player] = []
    rounds: List[Model.Round] = []
    description: str
    number_of_rounds: int
    current_round: int = 0

    def __init__(self, name: str, location: str, number_of_rounds=4):
        """
        Initializes a Tournament instance.

        Args:
            name (str): Name of the tournament.
            location (str): Location of the tournament.
            number_of_rounds (int, optional): Number of rounds in the tournament. Defaults to 4.
        """
        self.name = name.capitalize()
        self.location = location.capitalize()
        self.start_date = str(datetime.datetime.now().date())
        self.number_of_rounds = number_of_rounds
        self.end_datetime = None
        self.database_manager = DataBaseManager.DataBaseManager()

    def write_end_date(self) -> None:
        """
        Writes the end date of the tournament.
        """
        self.end_datetime = str(datetime.datetime.now().date())

    def write_description(self, description: str) -> None:
        """
        Writes the description of the tournament.

        Args:
            description (str): Description of the tournament.
        """
        self.description = description

    def add_round(self, round: Model.Round) -> None:
        """
        Adds a round to the tournament.

        Args:
            round (Model.Round): Round to be added.
        """
        self.rounds.append(round)

    def load_players(self) -> None:
        """
        Loads all players from the Players.json file database
        """
        self.players = self.database_manager.load_all_players()

    def shuffle_players(self) -> None:
        """
        Shuffles the order of the players.
        """
        random.shuffle(self.players)

    def sort_players(self) -> None:
        """
        Sorts the players based on their score in descending order.
        """
        self.players = sorted(self.players, key=lambda x: x.score, reverse=True)

    def to_dictionary(self) -> Dict[str, Any]:
        """
        Converts the tournament object to a dictionary.

        Returns:
            dict: Dictionary representation of the tournament.
        """
        dictionary = {
            "name": self.name,
            "location": self.location,
            "number_of_rounds": self.number_of_rounds,
            "start_date": self.start_date,
            "current_round": self.current_round,
            "rounds": [round.to_dictionary() for round in self.rounds],
            "players": [player.to_dictionary() for player in self.players]
        }
        if hasattr(self, 'description'):
            dictionary["description"] = self.description
        if self.end_datetime is not None:
            dictionary["end_datetime"] = self.end_datetime
        return dictionary

    @classmethod
    def load_from_dictionary(cls, data: Dict[str, Any]) -> 'Tournament':
        """
        Creates a tournament object from a dictionary.

        Args:
            data (dict): Dictionary containing the tournament data.

        Returns:
            Tournament: Tournament object created from the dictionary.
        """
        tournament = cls(data["name"], data["location"], data["number_of_rounds"])
        tournament.start_date = data["start_date"]
        tournament.current_round = data["current_round"]
        if "end_datetime" in data:
            tournament.end_datetime = data["end_datetime"]
        tournament.players = [Model.Player.load_from_dictionary(player_data) for player_data in data["players"]]
        tournament.rounds = [Model.Round.load_from_dictionary(round_data) for round_data in data["rounds"]]
        return tournament
