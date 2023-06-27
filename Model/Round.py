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
