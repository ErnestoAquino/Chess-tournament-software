from tinydb import TinyDB
from tinydb import Query
import Model


class DataBaseManager:

    def __init__(self):
        self.data_base_players = TinyDB("Data/Tournaments/Players.json")
        self.data_base_tournaments = TinyDB("Data/Tournaments/Tournaments.json")
        self.data_base_temporary_tournament = TinyDB("Data/Tournaments/Temporary_Tournament.json")

    def save_tournament(self, tournament_to_save: Model.Tournament):
        data_base = self.data_base_tournaments
        tournaments_table = data_base.table("tournaments")
        rounds_table = data_base.table("rounds")
        matches_table = data_base.table("matches")
        players_table = data_base.table("players")

        tournament_data = {"name": tournament_to_save.name,
                           "location": tournament_to_save.location,
                           "start_date": tournament_to_save.start_date,
                           "end_date": tournament_to_save.end_datetime,
                           "number_of_rounds": tournament_to_save.number_of_rounds}
        print(tournament_data)
        tournament_id = tournaments_table.insert(tournament_data)
        for round_i in tournament_to_save.rounds:
            round_data = {"name": round_i.name,
                          "start_date": round_i.start_datetime,
                          "end_date": round_i.end_datetime,
                          "tournament_id": tournament_id}
            round_id = rounds_table.insert(round_data)
            for match in round_i.list_of_matches:
                match_data = {"white_player_first_name": match.white_player.first_name,
                              "white_player_last_name": match.white_player.last_name,
                              "white_player_date_of_birth": match.white_player.date_of_birth,
                              "white_player_chess_national_id": match.white_player.chess_national_id,
                              "white_player_score": match.white_player.score,
                              "black_player_first_name": match.black_player.first_name,
                              "black_player_last_name": match.black_player.last_name,
                              "black_player_date_of_birth": match.black_player.date_of_birth,
                              "black_player_chess_national_id": match.black_player.chess_national_id,
                              "black_player_score": match.black_player.score,
                              "result": match.result.name,
                              "round_id": round_id
                              }
                matches_table.insert(match_data)
        for player in tournament_to_save.players:
            player_data = {"first_name": player.first_name,
                           "last_name": player.last_name,
                           "date_of_birth": player.date_of_birth,
                           "chess_national_id": player.chess_national_id,
                           "score": player.score,
                           "tournament_id": tournament_id}
            players_table.insert(player_data)
