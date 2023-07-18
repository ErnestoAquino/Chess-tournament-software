from typing import Dict
from typing import Any
from typing import List
import datetime
import Model


class Round:
    """
      Represents a round in a tournament.

      Attributes:
          list_of_matches (List[Model.Match]): List of matches in the round.
          name (str): Name of the round.
          start_datetime (str): Start datetime of the round.
          end_datetime (str): End datetime of the round.
          finished (bool): Indicates if the round has finished.
      """
    list_of_matches: List[Model.Match] = []

    def __init__(self, name: str):
        """
        Initializes a Round instance.

        Args:
            name (str): Name of the round.
        """
        self.name = name
        self.list_of_matches = []
        self.start_datetime = str(datetime.datetime.now())
        self.end_datetime = None
        self.finished = False

    def add_mach(self, match: Model.Match) -> None:
        """
        Adds a match to the round.

        Args:
            match (Match): Match to be added.
        """
        self.list_of_matches.append(match)

    def write_end_datetime(self) -> None:
        """
        Writes the end datetime of the round.
        """
        self.end_datetime = str(datetime.datetime.now())
        self.set_finished()

    def is_finished(self) -> bool:
        """
        Checks if the round has finished.

        Returns:
            bool: True if the round has finished, False otherwise.
        """
        return self.finished

    def set_finished(self) -> None:
        """
        Sets the round as finished.
        """
        self.finished = True

    def to_dictionary(self) -> Dict[str, Any]:
        """
        Converts the round object to a dictionary.

        Returns:
            dict: Dictionary representation of the round.
        """
        dictionary = {
            "name": self.name,
            "start_datetime": self.start_datetime,
            "finished": str(self.finished),
            "matches": [match.to_dictionary() for match in self.list_of_matches]
        }
        if self.end_datetime is not None:
            dictionary["end_datetime"] = self.end_datetime
        return dictionary

    @classmethod
    def load_from_dictionary(cls, data: Dict[str, Any]) -> 'Round':
        """
        Creates a round object from a dictionary.

        Args:
            data (dict): Dictionary containing the round data.

        Returns:
            Round: Round object created from the dictionary.
        """
        round = cls(data["name"])
        round.start_datetime = data["start_datetime"]
        if data["finished"] == "True":
            round.set_finished()
        for data_match in data["matches"]:
            match = Model.Match.load_from_dictionary(data_match)
            round.add_mach(match)
        return round
