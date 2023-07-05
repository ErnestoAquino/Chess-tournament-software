from jinja2 import Environment
from jinja2 import FileSystemLoader
from typing import Dict
from typing import List
import Model


class ReportsView:
    MESSAGE_OPTIONS = "Please choose one of the following options:\n"\
                    "1. List of all players in alphabetical order.\n"\
                    "2. List all tournaments.\n"\
                    "3. Name and dates of a given tournament.\n"\
                    "4. List of tournaments players in alphabetical order.\n"\
                    "5. List of all tournaments rounds, and all matches in the round.\n"
    ERROR_MESSAGE = "Please enter a valid response\n"
    env = Environment(loader=FileSystemLoader("."))

    def get_choice(self, number_of_options: int, options_to_show: str) -> int:
        numero = -1
        print(options_to_show)
        while numero > number_of_options or numero <= 0:
            try:
                numero = int(input())
                if numero > number_of_options or numero <= 0:
                    print(self.ERROR_MESSAGE)
            except ValueError:
                print(self.ERROR_MESSAGE)
                numero = -1
        return numero

    def display_players(self, players: [Model.Player]):
        template = self.env.get_template("Templates/report_all_players.html")
        players_to_show = []

        for player in players:
            new_player = {
                "first_name": player.first_name,
                "last_name": player.last_name,
                "chess_national_id": player.chess_national_id,
                "date_of_birth": player.date_of_birth
            }
            players_to_show.append(new_player)
        html_output = template.render(players=players_to_show)
        with open("report_all_players_output.html", "w") as file:
            file.write(html_output)
        print(html_output)

    def display_tournaments(self, tournaments: []):
        template = self.env.get_template("Templates/report_all_tournaments.html")
        tournaments_to_show = []

        for tournament in tournaments:
            new_tournament = {"name": tournament["name"]}
            tournaments_to_show.append(new_tournament)
        html_output = template.render(tournaments=tournaments_to_show)
        with open("report_all_tournaments_output.html", "w") as file:
            file.write(html_output)
        print(html_output)

    def display_one_tournament(self, tournament_to_show: Dict):
        template = self.env.get_template("Templates/report_one_tournament.html")
        html_output = template.render(tournament=tournament_to_show)
        with open("report_one_tournament_output.html", "w") as file:
            file.write(html_output)
        print(html_output)

    def display_players_alphabetical_order(self, players: List[Dict], tournament_name: str):
        template = self.env.get_template("Templates/report_players.html")
        html_output = template.render(players=players, tournament_name=tournament_name)
        with open("report_players_output.html", "w") as file:
            file.write(html_output)
        print(html_output)

    def display_rounds_from_tournament(self, tournament: Dict, rounds_to_show: List[Dict]):
        template = self.env.get_template("Templates/report_rounds_of_tournament.html")
        html_output = template.render(tournament=tournament, rounds=rounds_to_show)
        with open("report_rounds_of_tournament_output.html", "w") as file:
            file.write(html_output)
        print(html_output)

    def show_available_tournaments(self, tournaments: []) -> int:
        print("Please, select a tournament:\n")
        for i, tournament in enumerate(tournaments, 1):
            print(f"{i} - {tournament['name']}")
        user_choice = self.get_choice(number_of_options=len(tournaments),options_to_show="")
        return user_choice
