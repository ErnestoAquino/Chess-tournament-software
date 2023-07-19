from tinydb import TinyDB
from typing import Any
from typing import Optional
from typing import Dict
from typing import List
import Model


class DataBaseManager:
    tournament_temporary_id = None

    def __init__(self):
        """
        Initializes a new instance of the DataBaseManager class.

        Creates connections to the player, tournament and cache databases.
        """
        self.data_base_players = TinyDB("Data/Players/Players.json")
        self.data_base_tournaments = TinyDB("Data/Tournaments/Tournaments.json")
        self.data_base_cache = TinyDB("Data/Tournaments/Cache.json")

    def save_players(self, players_to_save: List[Model.Player]):
        """
        Save a list of players to the database.

        Args:
            players_to_save (List[Model.Player]): A list of Player objects to be saved.

        Raises:
            DataError: If there is an issue with the database operation.
        """
        players_table = self.data_base_players.table("Players")
        try:
            for player in players_to_save:
                player_data = {"first_name": player.first_name,
                               "last_name": player.last_name,
                               "date_of_birth": player.date_of_birth,
                               "chess_national_id": player.chess_national_id,
                               "score": player.score}
                players_table.insert(player_data)
        except Exception as e:
            print(f"Error occurred while saving players: {e}")

    def load_all_players(self) -> [Model.Player]:
        """
        Loads all players from the player database.

        Returns:
            List[Model.Player]: A list of all the players.
        """
        recovered_players = []
        local_players = self.data_base_players.table("Players")
        try:
            results = local_players.all()
        except Exception as e:
            # Handle the case where the table does not exist or is empty
            print(f"Error: {e}")
            return recovered_players

        for result in results:
            player = Model.Player(first_name=result["first_name"],
                                  last_name=result["last_name"],
                                  date_of_birth=result["date_of_birth"],
                                  chess_national_id=result["chess_national_id"],
                                  score=result["score"])
            recovered_players.append(player)
        return recovered_players

    def save_tournament(self, tournament_to_save: Model.Tournament):
        """
        Saves the tournament to the tournament database.

        Args:
            tournament_to_save (Model.Tournament): The tournament object to be saved.
        """
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

    def check_unfinished_tournament(self) -> bool:
        """
        Checks if there is an unfinished tournament in the cache.

        Returns:
            bool: True if there is an unfinished tournament, False otherwise.
        """
        tournament_table = self.data_base_cache.table("tournaments")
        tournament_result = tournament_table.all()
        if len(tournament_result) == 0:
            return False
        else:
            return True

    def make_check_point_tournament(self, data: [str, Any]) -> None:
        """
        Makes a checkpoint of the tournament by saving the data to the cache.

        Args:
            data ([str, Any]): The tournament data to be saved.
        """
        data_base = self.data_base_cache
        tournaments_table = data_base.table("tournaments")
        try:
            tournaments_table.truncate()
        except AttributeError:
            print("Error: The tournaments table is empty.")
        self.tournament_temporary_id = tournaments_table.insert(data)

    def load_unfinished_tournament(self) -> Optional[Dict[str, Any]]:
        """
        Loads the unfinished tournament data from the cache.

        Returns:
            Optional[Dict[str, Any]]: The tournament data if available, None otherwise.
        """
        tournament_table = self.data_base_cache.table("tournaments")
        tournament_list = tournament_table.all()
        if tournament_list:
            tournament_data = tournament_list[0]
            self.tournament_temporary_id = tournament_data.doc_id
            return tournament_data
        else:
            return None

    def delete_unfinished_tournament(self):
        """
        Deletes the unfinished tournament data from the cache.
        """
        tournament_table = self.data_base_cache.table("tournaments")
        tournament_table.truncate()
