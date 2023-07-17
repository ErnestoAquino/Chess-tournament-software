import random
from enum import Enum
import Model
from Model.Player import Player
from typing import Dict
from typing import Any


class Result(Enum):
    WIN = 1
    LOSS = 0
    DRAW = 0.5
    TO_BE_PLAYED = None


class Match:
    result: Result = Result.TO_BE_PLAYED

    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.white_player = random.choice([self.player1, self.player2])
        self.black_player = player1 if self.white_player == player2 else player2

    def print_color_players(self):
        print(f"{self.white_player.first_name} play with whites pieces")
        print(f"{self.black_player.first_name} play with black pieces")

    def set_result(self, result: Result):
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

    def to_dictionary(self):
        return {
            "player1": self.player1.to_dictionary(),
            "player2": self.player2.to_dictionary(),
            "white_player": self.white_player.to_dictionary(),
            "black_player": self.black_player.to_dictionary(),
            "result": self.result.name
        }

    @staticmethod
    def get_result(result_has_str: str) -> Result:
        try:
            return Result[result_has_str]
        except KeyError:
            return Result.TO_BE_PLAYED

    @classmethod
    def load_from_dictionary(cls, data: Dict[str, Any]) -> 'Match':
        player1 = Model.Player.load_from_dictionary(data["player1"])
        player2 = Model.Player.load_from_dictionary(data["player2"])
        match = Model.Match(player1, player2)
        match.white_player = Model.Player.load_from_dictionary(data["white_player"])
        match.black_player = Model.Player.load_from_dictionary(data["black_player"])
        match.result = Match.get_result(data["result"])
        return match
