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
