from tinydb import TinyDB
from tinydb import Query
from typing import Dict
from typing import List
from DataBaseManager import DataBaseManager
import View
import Model


class ReportsController:
    DATA_BASE_PLAYERS = TinyDB("Data/Players/Players.json")
    DATA_BASE_TOURNAMENTS = TinyDB("Data/Tournaments/Tournaments.json")
    players = []
    tournaments_information = []

    def __init__(self):
        self.reports_view = View.ReportsView()
        self.database_manager = DataBaseManager()

    def get_all_tournaments(self):
        local_tournaments = self.DATA_BASE_TOURNAMENTS.table("tournaments")
        results = local_tournaments.all()

        for result in results:
            new_tournament = {
                "name": result["name"],
                "location": result["location"],
                "start_date": result["start_date"],
                "end_date": result["end_date"],
                "number_of_rounds": result["number_of_rounds"]
            }
            self.tournaments_information.append(new_tournament)

    def get_one_tournament(self, id_tournament: int):
        results = self.DATA_BASE_TOURNAMENTS.table("tournaments")
        tournament = results.get(doc_id=id_tournament)
        return tournament

    def get_players_from(self, id_tournament: int):
        local_players = self.DATA_BASE_TOURNAMENTS.table("players")
        player_query = Query()
        players_in_tournament = local_players.search(player_query.tournament_id == id_tournament)
        ordered_players = sorted(players_in_tournament, key=lambda player: player["last_name"], reverse=False)
        return ordered_players

    def get_name_tournament(self, id_tournament: int) -> str:
        tournaments_table = self.DATA_BASE_TOURNAMENTS.table("tournaments")
        tournament = tournaments_table.get(doc_id=id_tournament)
        return tournament["name"]

    def get_rounds_from(self, id_tournament: int) -> List[Dict]:
        rounds_table = self.DATA_BASE_TOURNAMENTS.table("rounds")
        round_query = Query()
        rounds = rounds_table.search(round_query.tournament_id == id_tournament)
        for round_i in rounds:
            print(f"{round_i['name']} - {round_i['start_date']} to {round_i['end_date']}")
            matches = self.get_matches_from(id_round=round_i.doc_id)
            for match in matches:
                print(f"{match['white_player']} played whites pieces  VS \
                        {match['black_player']} played with black pieces. Result: {match['result']} white player.")
        return rounds

    def test_get_rounds_from(self, id_tournament: int) -> List[Dict]:
        rounds_table = self.DATA_BASE_TOURNAMENTS.table("rounds")
        round_query = Query()
        rounds = rounds_table.search(round_query.tournament_id == id_tournament)
        for round_i in rounds:
            print(f"{round_i['name']} - {round_i['start_date']} to {round_i['end_date']}")
            round_i['matches'] = []
            matches = self.get_matches_from(id_round=round_i.doc_id)
            for match in matches:
                match_data = {
                    "white_payer": match["white_player_first_name"] + " " + match["white_player_last_name"],
                    "white_player_id": match["white_player_chess_national_id"],
                    "black_player": match["black_player_first_name"] + " " + match["black_player_last_name"],
                    "black_player_id": match["black_player_chess_national_id"],
                    "result": match["result"]
                }
                round_i["matches"].append(match_data)
                print(f"{match['white_player_first_name']} played whites pieces  VS \
                        {match['black_player_first_name']} played with black pieces. Result: {match['result']} white "
                      f"player.")
        return rounds

    def get_matches_from(self, id_round: int) -> List[Dict]:
        matches_table = self.DATA_BASE_TOURNAMENTS.table("matches")
        match_query = Query()
        match_of_round = matches_table.search(match_query.round_id == id_round)
        return match_of_round

    def present_report_all_players(self):
        players_to_show = self.database_manager.get_all_players_alphabetical_order()
        self.reports_view.display_players(players_to_show)

    def present_report_all_tournaments(self):
        self.get_all_tournaments()
        self.reports_view.display_tournaments(self.tournaments_information)

    def present_report_one_tournament(self):
        self.get_all_tournaments()
        user_choice = self.reports_view.show_available_tournaments(self.tournaments_information)
        tournament = self.get_one_tournament(id_tournament=user_choice)
        self.reports_view.display_one_tournament(tournament)

    def present_report_tournament_players(self):
        self.get_all_tournaments()
        user_choice = self.reports_view.show_available_tournaments(self.tournaments_information)
        players = self.get_players_from(id_tournament=user_choice)
        tournament_name = self.get_name_tournament(id_tournament=user_choice)
        self.reports_view.display_players_alphabetical_order(players, tournament_name)

    def present_report_all_round_from_tournament(self):
        self.get_all_tournaments()
        user_choice = self.reports_view.show_available_tournaments(self.tournaments_information)
        tournament = self.get_one_tournament(id_tournament=user_choice)
        rounds = self.test_get_rounds_from(id_tournament=user_choice)
        self.reports_view.display_rounds_from_tournament(tournament, rounds)

    def start(self):
        user_choice = self.reports_view.get_choice(number_of_options=5,
                                                   options_to_show=self.reports_view.MESSAGE_OPTIONS)
        self.reports_view.check_if_folder_exist()
        match user_choice:
            case 1:
                self.present_report_all_players()
            case 2:
                self.present_report_all_tournaments()
            case 3:
                self.present_report_one_tournament()
            case 4:
                self.present_report_tournament_players()
            case 5:
                self.present_report_all_round_from_tournament()
