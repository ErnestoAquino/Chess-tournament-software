import random
from enum import Enum
import Model
from Model.Player import Player
from typing import Dict
from typing import Any


class Result(Enum):
    """
    Enumeration representing the result of a match.

    Values:
        WIN: The white player won the match.
        LOSS: The white player lost the match.
        DRAW: The match ended in a draw.
        TO_BE_PLAYED: The match has yet to be played.
    """
    WIN = 1
    LOSS = 0
    DRAW = 0.5
    TO_BE_PLAYED = None


class Match:
    """
    Represents a match between two players.

    Attributes:
        result (Result): Result of the match.
        player1 (Player): First player in the match.
        player2 (Player): Second player in the match.
        white_player (Player): Player assigned as white pieces.
        black_player (Player): Player assigned as black pieces.
    """
    result: Result = Result.TO_BE_PLAYED

    def __init__(self, player1: Player, player2: Player):
        """
        Initializes a Match instance.

        Args:
            player1 (Player): First player in the match.
            player2 (Player): Second player in the match.
        """
        self.player1 = player1
        self.player2 = player2
        self.white_player = random.choice([self.player1, self.player2])
        self.black_player = player1 if self.white_player == player2 else player2

    def print_color_players(self) -> None:
        """
         Prints the players assigned to each color.
         """
        print(f"{self.white_player.first_name} play with whites pieces")
        print(f"{self.black_player.first_name} play with black pieces")

    def set_result(self, result: Result) -> None:
        """
         Sets the result of the match and updates player scores accordingly.

         Args:
             result (Result): Result of the match.
         """
        match result:
            case Result.WIN:
                self.white_player.update_score(result.value)
                self.result = result
            case Result.LOSS:
                self.black_player.update_score(1)
                self.result = result
            case Result.DRAW:
                self.white_player.update_score(result.value)
                self.black_player.update_score(result.value)
                self.result = result

    def to_dictionary(self) -> Dict[str, Any]:
        """
        Converts the match object to a dictionary.

        Returns:
            dict: Dictionary representation of the match.
        """
        return {
            "player1": self.player1.to_dictionary(),
            "player2": self.player2.to_dictionary(),
            "white_player": self.white_player.to_dictionary(),
            "black_player": self.black_player.to_dictionary(),
            "result": self.result.name
        }

    @staticmethod
    def get_result(result_has_str: str) -> Result:
        """
        Gets the `Result` enum value based on a string representation.

        Args:
            result_has_str (str): String representation of the result.

        Returns:
            Result: Result enum value.
        """
        try:
            return Result[result_has_str]
        except KeyError:
            return Result.TO_BE_PLAYED

    @classmethod
    def load_from_dictionary(cls, data: Dict[str, Any]) -> 'Match':
        """
        Creates a match object from a dictionary.

        Args:
            data (dict): Dictionary containing the match data.

        Returns:
            Match: Match object created from the dictionary.
        """
        player1 = Model.Player.load_from_dictionary(data["player1"])
        player2 = Model.Player.load_from_dictionary(data["player2"])
        white_player = Model.Player.load_from_dictionary(data["white_player"])
        black_player = Model.Player.load_from_dictionary(data["black_player"])
        result = Match.get_result(data["result"])
        match = cls(player1, player2)
        match.white_player = white_player
        match.black_player = black_player
        match.result = result

        return match
