from jinja2 import Environment
from jinja2 import FileSystemLoader
from typing import Dict
from typing import List
from typing import Any
import os
import Model


class ReportsView:
    MESSAGE_OPTIONS = "Please choose one of the following options:\n" \
                      "1. List of all players in alphabetical order.\n" \
                      "2. List all tournaments.\n" \
                      "3. Name and dates of a given tournament.\n" \
                      "4. List of tournaments players in alphabetical order.\n" \
                      "5. List of all tournaments rounds, and all matches in the round.\n"
    REPORT_FOLDER = "Reports_Output"
    env = Environment(loader=FileSystemLoader("."))

    def display_players(self, players: [Model.Player]):
        """
        Display a list of players in alphabetical order.

        Args:
            players (List[Model.Player]): A list of player objects to display.

        Notes:
            This method generates an HTML report of all players and saves it to a file
            named "report_all_players_output.html".
            The template used for rendering is "Templates/report_all_players.html".
        """
        self.check_if_folder_exist()
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
        self.save_report_as_html_file(rendered_template=html_output,
                                      output_file_name="report_all_players_output.html")

    def display_tournaments(self, tournaments: List[Dict[str, Any]]):
        """
        Display a list of tournaments.

        Args:
            tournaments (List[Dict[str, Any]]): A list of dictionaries, each representing a tournament, with the "name"
            key representing the name of the tournament.

        Notes:
            This method generates an HTML report of all tournaments and saves it to a file
            named "report_all_tournaments_output.html".
            The template used for rendering is "Templates/report_all_tournaments.html".
        """
        self.check_if_folder_exist()
        template = self.env.get_template("Templates/report_all_tournaments.html")
        tournaments_to_show = []

        for tournament in tournaments:
            new_tournament = {"name": tournament["name"]}
            tournaments_to_show.append(new_tournament)
        html_output = template.render(tournaments=tournaments_to_show)
        self.save_report_as_html_file(rendered_template=html_output,
                                      output_file_name="report_all_tournaments_output.html")

    def display_one_tournament(self, tournament_to_show: Dict[str, Any]):
        """
        Display information about a single tournament.

        Args:
            tournament_to_show (Dict[str, Any]): A dictionary containing the information of the tournament to display.

        Notes:
            This method generates an HTML report for a single tournament using the provided information and saves it to
            a file named "report_one_tournament_output.html".
            The template used for rendering is "Templates/report_one_tournament.html".
        """
        self.check_if_folder_exist()
        template = self.env.get_template("Templates/report_one_tournament.html")
        html_output = template.render(tournament=tournament_to_show)
        self.save_report_as_html_file(rendered_template=html_output,
                                      output_file_name="report_one_tournament_output.html")

    def display_players_alphabetical_order(self, players: List[Dict], tournament_name: str):
        """
        Display a list of players in alphabetical order for a specific tournament.

        Args:
            players (List[Dict]): A list of dictionaries containing player information.
            tournament_name (str): The name of the tournament for which the players are displayed.

        Notes:
            This method generates an HTML report with a list of players in alphabetical order
            for a specific tournament.
            The template used for rendering is "Templates/report_players.html".
            The rendered report is saved to a file
            named "report_players_output.html" in the "Reports_Output" folder.
        """
        self.check_if_folder_exist()
        template = self.env.get_template("Templates/report_players.html")
        html_output = template.render(players=players, tournament_name=tournament_name)
        self.save_report_as_html_file(rendered_template=html_output,
                                      output_file_name="report_players_output.html")

    def display_rounds_from_tournament(self, tournament: Dict, rounds_to_show: List[Dict]):
        """
        Display the rounds and matches of a specific tournament.

        Args:
            tournament (Dict): A dictionary containing tournament information.
            rounds_to_show (List[Dict]): A list of dictionaries containing rounds and their corresponding matches.

        Notes:
            This method generates an HTML report with the rounds and matches of a specific tournament.
            The template used for rendering is "Templates/report_rounds_of_tournament.html". The rendered report
            is saved to a file named "report_rounds_of_tournament_output.html" in the "Reports_Output" folder.
        """
        self.check_if_folder_exist()
        template = self.env.get_template("Templates/report_rounds_of_tournament.html")
        html_output = template.render(tournament=tournament, rounds=rounds_to_show)
        self.save_report_as_html_file(rendered_template=html_output,
                                      output_file_name="report_rounds_of_tournament_output.html")

    def show_available_tournaments(self, tournaments: List[Dict]) -> int:
        """
        Display the available tournaments and prompt the user to select one.

        Args:
            tournaments (List[Dict]): A list of dictionaries representing the available tournaments.

        Returns:
            int: The user's choice, which corresponds to the index of the selected tournament in the list.

        Notes:
            This method lists the available tournaments and prompts the user to select one by entering the number
            associated with the desired tournament. The numbering starts from 1. The selected index is returned as an
            integer.
        """
        print("Please, select a tournament:\n")
        for i, tournament in enumerate(tournaments, 1):
            print(f"{i} - {tournament['name']}")
        user_choice = self.get_choice(number_of_options=len(tournaments), options_to_show="")
        return user_choice

    def save_report_as_html_file(self, rendered_template: Any, output_file_name: str):
        """
        Save the rendered HTML template as an HTML file.

        Args:
            rendered_template (Any): The rendered template content to be saved.
            output_file_name (str): The name of the output HTML file.
        """
        report_output_path = os.path.join(self.REPORT_FOLDER, output_file_name)
        with open(report_output_path, "w") as file:
            file.write(rendered_template)
        print(rendered_template)

    def check_if_folder_exist(self):
        """
        Create the report folder if it doesn't exist.
        """
        if not os.path.exists(self.REPORT_FOLDER):
            os.mkdir(self.REPORT_FOLDER)

    @staticmethod
    def get_choice(number_of_options: int, options_to_show: str) -> int:
        """
        Get the user's choice from the available options.

        Args:
            number_of_options (int): The number of options available to the user.
            options_to_show (str): The options to display to the user.

        Returns:
            int: The user's choice.
        """
        numero = -1
        print(options_to_show)
        while numero > number_of_options or numero <= 0:
            try:
                numero = int(input())
                if numero > number_of_options or numero <= 0:
                    print("Please enter a valid response.")
            except ValueError:
                print("Please enter a valid response")
                numero = -1
        return numero
