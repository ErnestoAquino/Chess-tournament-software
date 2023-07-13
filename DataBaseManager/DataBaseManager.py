from tinydb import TinyDB
from tinydb import Query
from typing import Union
from typing import List
import Model


class DataBaseManager:
    tournament_temporary_id = None

    def __init__(self):
        self.data_base_players = TinyDB("Data/Players/Players.json")
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
        self.delete_unfinished_tournament()

    def checkpoint_creation_tournament(self, tournament: Model.Tournament):
        data_base = self.data_base_temporary_tournament
        tournaments_table = data_base.table("tournaments")
        tournament_data = {
            "name": tournament.name,
            "location": tournament.location,
            "start_date": tournament.start_date
        }
        self.tournament_temporary_id = tournaments_table.insert(tournament_data)

    def checkpoint_add_tournament_description(self, description: str):
        tournament_found = \
            self.data_base_temporary_tournament.table("tournaments").get(doc_id=self.tournament_temporary_id)
        if tournament_found:
            tournament_found["description"] = description
            self.data_base_temporary_tournament.table("tournaments").update(tournament_found)

    def check_unfinished_tournament(self) -> bool:
        tournament_table = self.data_base_temporary_tournament.table("tournaments")
        tournament_result = tournament_table.all()
        if len(tournament_result) == 0:
            return False
        else:
            return True

    def update_result_match(self, round_id: int, number_of_match: int, result: Model.Result):
        match_table = self.data_base_temporary_tournament.table("matches")
        matches = match_table.search(Query().round_id == round_id)
        print("================================================================================")
        print(f"round id = {round_id}")
        print(f"number of match = {number_of_match + 1}")
        print(f"result {result.name}")
        if number_of_match < len(matches):
            desired_match = matches[number_of_match]
            print(f"antes de actualizar: {desired_match['result']}")
            desired_match["result"] = result.name
            match_table.update(desired_match, doc_ids=[desired_match.doc_id])
            print(matches[number_of_match]["white_player_first_name"])
            print(f"despues: {matches[number_of_match]['result']}")
        else:
            print("No encontre el partido")
        print("================================================================================")

    def update_end_datetime_round(self, round_id: int, datetime: str):
        rounds_table = self.data_base_temporary_tournament.table("rounds")
        desired_round = rounds_table.get(doc_id=round_id)
        if desired_round:
            print("================================================================================")
            desired_round["end_datetime"] = datetime
            rounds_table.update(desired_round)
            print(desired_round["end_datetime"])
            print("================================================================================")
        else:
            print("No he encontrado el round")

    def update_score_player(self, id_player: str):
        pass

    def checkpoint_match(self, match: Model.Match, round_id: int):
        match_table = self.data_base_temporary_tournament.table("matches")
        match_data = {
            "white_player_first_name": match.white_player.first_name,
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
        match_table.insert(match_data)

    def checkpoint_players(self, players_to_save: Union[List[Model.Player], Model.Tournament]):
        players_table = self.data_base_temporary_tournament.table("players")
        players_table.truncate()
        if isinstance(players_to_save, List):
            for player in players_to_save:
                player_data = {
                    "first_name": player.first_name,
                    "last_name": player.last_name,
                    "date_of_birth": player.date_of_birth,
                    "chess_national_id": player.chess_national_id,
                    "score": player.score,
                    "tournament_id": self.tournament_temporary_id
                }
                players_table.insert(player_data)
        if isinstance(players_to_save, Model.Tournament):
            for player in players_to_save.players:
                player_data = {
                    "first_name": player.first_name,
                    "last_name": player.last_name,
                    "date_of_birth": player.date_of_birth,
                    "chess_national_id": player.chess_national_id,
                    "score": player.score,
                    "tournament_id": self.tournament_temporary_id
                }
                players_table.insert(player_data)

    def checkpoint_round(self, rounds_to_save: List[Model.Round]):
        rounds_table = self.data_base_temporary_tournament.table("rounds")
        rounds_table.truncate()
        for round in rounds_to_save:
            round_data = {
                "name": round.name,
                "start_date": round.start_datetime,
                "tournament_id": self.tournament_temporary_id
            }
            round_id = rounds_table.insert(round_data)
            for match in round.list_of_matches:
                self.checkpoint_match(match, round_id)

    def delete_unfinished_tournament(self):
        tournament_table = self.data_base_temporary_tournament.table("tournaments")
        rounds_table = self.data_base_temporary_tournament.table("rounds")
        matches_table = self.data_base_temporary_tournament.table("matches")
        players_table = self.data_base_temporary_tournament.table("players")
        tournament_table.truncate()
        rounds_table.truncate()
        matches_table.truncate()
        players_table.truncate()
        self.data_base_temporary_tournament.close()

    def load_unfinished_tournament(self):
        tournament: Model.Tournament
        tournament_data = self.data_base_temporary_tournament.table("tournaments").all()[0]
        name = tournament_data.get("name", None)
        location = tournament_data.get("location", None)
        start_date = tournament_data.get("start_date", None)
        if all(item is not None for item in [name, location, start_date]):
            tournament = Model.Tournament(name, location)
            print(f"Unfinished tournament name = {tournament.name}")
            print(f"Unfinished tournament location = {tournament.location}")
            print(f"Unfinished tournament start date: = {tournament.start_date}")

