from tinydb import TinyDB
import View
import Model


class ReportsController:
    DATA_BASE = TinyDB("Data/Players/Players.json")
    players = []

    def __init__(self):
        self.reports_view = View.ReportsView()

    def get_all_players(self):
        local_players = self.DATA_BASE.table("Players")
        results = local_players.all()
        for result in results:
            player = Model.Player(first_name = result["first_name"],
                                  last_name = result["last_name"],
                                  date_of_birth = result["date_of_birth"],
                                  chess_national_id = result["chess_national_id"],
                                  score = result["score"])
            self.players.append(player)

    def order_players_alphabetically(self):
        self.players = sorted(self.players, key = lambda x: x.last_name, reverse = True)

