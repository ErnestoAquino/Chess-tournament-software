from typing import Dict
from typing import Any
import datetime
import Model


class Round:
    list_of_matches = []

    def __init__(self, name: str):
        self.name = name
        self.list_of_matches = []
        self.start_datetime = str(datetime.datetime.now())
        self.end_datetime = None
        self.finished = False

    def add_mach(self, match: Model.Match):
        self.list_of_matches.append(match)

    def write_end_datetime(self):
        self.end_datetime = str(datetime.datetime.now())
        self.set_finished()

    def is_finished(self) -> bool:
        return self.finished

    def set_finished(self):
        self.finished = True

    def to_dictionary(self) -> Dict:
        dictionary = {
            "name": self.name,
            "start_date": self.start_datetime,
            "finished": str(self.finished),
            "matches": [match.to_dictionary() for match in self.list_of_matches]
        }
        if self.end_datetime is not None:
            dictionary["end_datetime"] = self.end_datetime
        return dictionary

    @classmethod
    def load_from_dictionary(cls, data: Dict[str, Any]) -> 'Round':
        round = Model.Round(data["name"])
        round.start_datetime = data["start_date"],
        if data["finished"] == "True":
            round.set_finished()
        for data_match in data["matches"]:
            match = Model.Match.load_from_dictionary(data_match)
            round.add_mach(match)
        return round
