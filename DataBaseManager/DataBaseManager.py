from tinydb import TinyDB
from tinydb import Query
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

    def get_all_players_alphabetical_order(self) -> List[Model.Player]:
        """
        Retrieves all players from the database and returns them in alphabetical order based on last names.

        Returns:
            List[Model.Player]: A list of Player objects sorted in alphabetical order based on last names.
        Raises:
            Exception: If there is an issue with accessing the database or retrieving the players.
        """
        recovered_players: List[Model.Player] = []
        try:
            players_table = self.data_base_players.table("Players")
            results = players_table.all()
            for result in results:
                player = Model.Player.load_from_dictionary(result)
                recovered_players.append(player)
        except Exception as e:
            # Handle the case where the database does not exist or is empty
            print(f"Error occurred while retrieving players: {e}")
            raise Exception("Failed to retrieve players from the database.")
        recovered_players = sorted(recovered_players, key=lambda x: x.last_name, reverse=False)
        return recovered_players

    def get_all_tournaments(self) -> List[Dict[str, Any]]:
        """
        Retrieves information about all tournaments from the database.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries, each containing information about a tournament.
        Raises:
            Exception: If there is an issue with accessing the database or retrieving the tournament information.
        """
        tournament_information: List[Dict[str, Any]] = []
        try:
            table_tournaments = self.data_base_tournaments.table("tournaments")
            results = table_tournaments.all()
            for result in results:
                new_tournament = {
                    "name": result["name"],
                    "location": result["location"],
                    "start_date": result["start_date"],
                    "end_date": result["end_date"],
                    "number_of_rounds": result["number_of_rounds"]
                }
                tournament_information.append(new_tournament)
        except Exception as e:
            # Handle the case where the database does not exist or is empty
            print(f"Error occurred while retrieving tournament information: {e}")
            raise Exception("Failed to retrieve tournament information from the database.")
        return tournament_information

    def get_one_tournament(self, id_tournament: int) -> Dict[str, Any]:
        """Get information about a specific tournament from the database.

        Args:
            id_tournament (int): The ID of the tournament to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the information of the tournament.

        Raises:
            Any Exception: If an error occurs while trying to retrieve the tournament information.
        """
        try:
            results = self.data_base_tournaments.table("tournaments")
            selected_tournament = results.get(doc_id=id_tournament)
            return selected_tournament
        except Exception as e:
            # Handle the case where the database does not exist or is empty
            print(f"Error occurred while retrieving tournament information: {e}")
            raise Exception("Failed to retrieve tournament information from the database.")

    def get_players_from(self, id_tournament: int) -> List[Dict[str, Any]]:
        """
        Retrieves the list of players participating in the tournament with the given ID from the database.

        Parameters:
            id_tournament (int): The ID of the tournament to retrieve players from.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing player information.

        Raises:
            Exception: If there is an error while retrieving player information from the database.
        """
        try:
            table_players = self.data_base_tournaments.table("players")
            players_in_tournament = table_players.search(Query().tournament_id == id_tournament)
            recovered_players = sorted(players_in_tournament, key=lambda player: player["last_name"], reverse=False)
            return recovered_players
        except Exception as e:
            # Handle the case where the database does not exist or is empty
            print(f"Error occurred while retrieving players information: {e}")
            raise Exception("Failed to retrieve players information from the database.")

    def get_name_tournament(self, id_tournament: int) -> str:
        """
        Retrieves the name of the tournament with the given ID from the database.

        Parameters:
            id_tournament (int): The ID of the tournament to retrieve.

        Returns:
            str: The name of the selected tournament.

        Raises:
            Exception: If there is an error while retrieving the tournament name from the database.
        """
        try:
            table_tournaments = self.data_base_tournaments.table("tournaments")
            selected_tournament = table_tournaments.get(doc_id=id_tournament)
            return selected_tournament["name"]
        except Exception as e:
            # Handle the case where the database does not exist or is empty
            print(f"Error occurred while retrieving tournament name information: {e}")
            raise Exception("Failed to retrieve tournament name information from the database.")

    def get_rounds_from(self, id_tournament: int) -> List[Dict[str, Any]]:
        """
        Retrieve the rounds for a given tournament ID, along with their match information.

         Args:
             id_tournament (int): The ID of the tournament for which to retrieve rounds.

         Returns:
             List[Dict[str, Any]]: A list of dictionaries representing the rounds and their matches
                                   for the given tournament.
         """
        try:
            table_rounds = self.data_base_tournaments.table("rounds")
            recovered_rounds = table_rounds.search(Query().tournament_id == id_tournament)
            for round_data in recovered_rounds:
                round_data["matches"] = []
                matches = self.get_matches_from(id_round=round_data.doc_id)

                if matches is not None:
                    for match in matches:
                        match_data = {
                            "white_payer": match["white_player_first_name"] + " " + match["white_player_last_name"],
                            "white_player_id": match["white_player_chess_national_id"],
                            "black_player": match["black_player_first_name"] + " " + match["black_player_last_name"],
                            "black_player_id": match["black_player_chess_national_id"],
                            "result": match["result"]
                        }
                        round_data["matches"].append(match_data)

            return recovered_rounds
        except Exception as e:
            # Handle the case where the database does not exist or is empty
            print(f"Error occurred while retrieving tournament name information: {e}")
            raise Exception("Failed to retrieve tournament name information from the database.")

    def get_matches_from(self, id_round: int) -> Optional[List[Dict]]:
        """
        Retrieve the matches from the database for a given round ID.

        Args:
            id_round (int): The ID of the round for which to retrieve matches.

        Returns:
            Optional[List[Dict]]: A list of dictionaries representing the matches for the given round,
                                  or None if no matches are found or an error occurs during retrieval.
        """
        try:
            table_matches = self.data_base_tournaments.table("matches")
            recovered_matches = table_matches.search(Query().round_id == id_round)
            return recovered_matches
        except Exception as e:
            # Handle the case where the database does not exist or is empty
            print(f"Error occurred while retrieving matches information: {e}")
            return None
