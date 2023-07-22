import random
import itertools
from typing import Dict
from typing import Any
from typing import List
from typing import Set
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

    def generate_matches(self) -> List[Model.Match]:
        """
        Generates pairings (matches) between players for a tournament.

        Returns:
            List[Model.Match]: A list of Model.Match objects representing the generated pairings.

        Raises:
            ValueError: If there are not enough players to generate fair pairings.

        Note:
            Pairings are generated in a way that ensures each player faces an opponent they have not played before.
            If there are not enough players to generate a fair set of matches, a ValueError is raised.
        """
        pairings: List[Model.Match] = []
        paired_players: Set[tuple] = set()
        players_with_pair: Set[Model.Player] = set()

        # Check if there are enough players to generate fair pairings
        num_players = len(self.players)
        if num_players < 2:
            raise ValueError("At least 2 players are required to generate fair pairings.")

        for player in self.players:
            possible_pairs = itertools.combinations(self.players, 2)

            # Generate all possible combinations of 2 players (possible pairings)
            for pair in possible_pairs:
                # Check if both players in the pairing have not faced each other before,
                # and if the current player matches the first player in the pairing.
                if (pair[1].chess_national_id not in pair[0].id_played and
                    pair[0].chess_national_id not in pair[1].id_played and

                        player == pair[0] and
                        pair not in paired_players and
                        pair[0] not in players_with_pair and
                        pair[1] not in players_with_pair):
                    paired_players.add(pair)
                    player1, player2 = pair

                    # Create a match between the two players and add it to the pairings list
                    match = Model.Match(player1, player2)
                    pairings.append(match)

                    # Update sets to keep track of paired players
                    players_with_pair.add(pair[0])
                    players_with_pair.add(pair[1])

        # If the number of matches is less than half the number of players,
        # reorganize the players to generate more pairings
        while len(pairings) < (len(self.players) / 2):
            last_player = self.players.pop()
            self.players.insert(0, last_player)

            # Recursively call itself to generate more pairings with the newly organized players list
            pairings = self.generate_matches()

        return pairings
