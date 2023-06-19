import random
from typing import List
from typing import Set
from typing import Tuple
import datetime
import Model


class Round:
    list_of_matches = []
    end_datetime: str

    def __init__(self, name: str):
        self.name = name
        self.list_of_matches = []
        self.start_datetime = str(datetime.datetime.now())

    def add_mach(self, match: Model.Match):
        self.list_of_matches.append(match)

    def write_end_datetime(self):
        self.end_datetime = str(datetime.datetime.now())

    def generate_matches(self, players: List[Model.Player], previous_matches: Set[Tuple[Model.Player, Model.Player]]) \
            -> List[Tuple[Model.Player, Model.Player]]:
        emparejamientos = []
        jugadores_disponibles = players[:]
        random.shuffle(jugadores_disponibles)

        for i in range(0, len(jugadores_disponibles), 2):
            player1 = jugadores_disponibles[i]
            player2 = jugadores_disponibles[i + 1]
            if (player1, player2) not in previous_matches and (player2, player1) not in previous_matches:
                emparejamientos.append((player1, player2))
                previous_matches.add((player1, player2))
        return emparejamientos

