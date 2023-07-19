from typing import Dict
from typing import Any
from typing import List


class Player:
    """
    Represents a player in a chess tournament.

    Attributes:
        score (float): Player's score.
        played_players (List[Player]): List of players the player has played against.
        id_played (List[str]): List of IDs of players the player has played against.
        first_name (str): Player's first name.
        last_name (str): Player's last name.
        date_of_birth (str): Player's date of birth.
        chess_national_id (str): Player's chess national ID.
    """
    score: float = 0
    played_players: List["Player"] = []
    id_played: List[str] = []

    def __init__(self, first_name: str,
                 last_name: str,
                 date_of_birth: str,
                 chess_national_id: str,
                 score: float = 0):
        """
        Initializes a Player instance.

        Args:
            first_name (str): Player's first name.
            last_name (str): Player's last name.
            date_of_birth (str): Player's date of birth.
            chess_national_id (str): Player's chess national ID.
            score (float, optional): Player's score. Defaults to 0.
        """
        self.first_name = first_name.lower()
        self.last_name = last_name.upper()
        self.date_of_birth = date_of_birth
        self.chess_national_id = chess_national_id
        self.score = score
        self.played_players = []
        self.id_played = []

    def update_score(self, score: float) -> None:
        """
        Updates the player's score.

        Args:
            score (float): Score to be added to the player's current score.
        """
        self.score += score

    def print_opponents(self) -> None:
        """
        Prints the opponents the player has played against.
        """
        if len(self.played_players) != 0:
            for player in self.played_players:
                print(f"I have fought with: {player.first_name}")
                print(f"{len(self.played_players)} len of players")

    def print_id_opponents(self) -> None:
        """
        Prints the IDs of the opponents the player has played against.
        """
        for id in self.id_played:
            print(f"{id}")

    def to_dictionary(self) -> Dict[str, Any]:
        """
        Converts the player object to a dictionary.

        Returns:
            dict: Dictionary representation of the player.
        """
        dictionary: Dict[str, Any] = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "chess_national_id": self.chess_national_id,
            "score": self.score,
        }
        if self.played_players:
            dictionary["played_players"] = self.players_to_dictionary(self.played_players)
        return dictionary

    @classmethod
    def load_from_dictionary(cls, data: Dict[str, Any]) -> "Player":
        """
        Creates a player object from a dictionary.

        Args:
            data (dict): Dictionary containing the player data.

        Returns:
            Player: Player object created from the dictionary.
        """
        player = cls(
            data["first_name"],
            data["last_name"],
            data["date_of_birth"],
            data["chess_national_id"]
        )
        for key, value in data.items():
            if key == "played_players":
                players_data = value
                players = [Player.load_from_dictionary(player_data) for player_data in players_data]
                setattr(player, key, players)
            else:
                setattr(player, key, value)
        return player

    @classmethod
    def players_to_dictionary(cls, players: List["Player"]) -> List[Dict[str, Any]]:
        """
        Converts a list of player objects to a list of dictionaries.

        Args:
            players (List[Player]): List of player objects.

        Returns:
            List[dict]: List of dictionaries representing the player objects.
        """
        players_list = []
        for player in players:
            dictionary = {
                "first_name": player.first_name,
                "last_name": player.last_name,
                "date_of_birth": player.date_of_birth,
                "chess_national_id": player.chess_national_id,
                "score": player.score,
            }
            players_list.append(dictionary)
        return players_list
