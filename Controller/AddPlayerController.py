from tinydb import TinyDB
import View


class AddPlayerController:
    DATA_BASE = TinyDB("Data/Players/Players.json")
    players = []

    def __init__(self):
        self.add_player_view = View.AddPlayerView()

    def get_players_to_save(self):
        self.players = self.add_player_view.players_to_save()
        self.save_players()

    def save_players(self):
        local_players = self.DATA_BASE.table("Players")
        for player in self.players:
            local_players.insert({"first_name": player.first_name,
                                  "last_name": player.last_name,
                                  "date_of_birth": player.date_of_birth,
                                  "chess_national_id": player.chess_national_id,
                                  "score": player.score})
