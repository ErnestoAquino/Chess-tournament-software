import random
from enum import Enum
from Model.Player import Player


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
        self.white_player = random.choice([player1, player2])
        self.black_player = player1 if self.white_player == player2 else player2

    def set_result_test(self, result: Result):
        match result:
            case Result.WIN:
                self.player1.update_score(result.value)
                self.result = result
            case Result.LOSS:
                self.player2.update_score(1)
                self.result = result
            case Result.DRAW:
                self.player1.update_score(result.value)
                self.player2.update_score(result.value)
                self.result = result

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
