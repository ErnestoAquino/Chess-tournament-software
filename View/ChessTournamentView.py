from prettytable import PrettyTable
from colorama import init
from colorama import Fore
import Model


# noinspection PyMethodMayBeStatic
class ChessTournamentView:
    options: str = f"{Fore.GREEN}What was the result of the match.{Fore.RESET}\n" \
                   f"{Fore.BLUE}1 - White pieces won.{Fore.RESET}\n" \
                   f"{Fore.BLUE}2 - Black pieces won.{Fore.RESET}\n" \
                   f"{Fore.BLUE}3 - It was a draw.{Fore.RESET}\n"
    response: str = None
    number_of_options: int
    message_error: str = f"{Fore.RED}Invalid answer, please try again{Fore.RESET}"

    def __init__(self, number_of_options: int = 3):
        self.number_of_options = number_of_options

    # @staticmethod
    def display_message_success(self, name: str):
        print(f"The tournament {name.capitalize()} has been successfully created with the following information:")

    def display_message_tournament_creation(self):
        print("You have decided to create a tournament. Please enter the requested information in order to proceed "
              "with its creation.")

    def display_message_naming(self):
        print("Please, enter the name of the chess tournament:")

    def display_message_location(self):
        print("Please, enter the location of the chess tournament:")

    def display_message_description(self):
        print("Please enter the description of the tournament.")

    def display_players(self, players: [Model.Player]):
        print("Registered players:")
        for player in players:
            print(player.first_name)

    def display_tournament_information(self, tournament: Model.Tournament):
        tournament_information = PrettyTable()
        tournament_information.field_names = ["Tournament Name", "Location", "Description"]
        tournament_information.add_row([tournament.name, tournament.location, tournament.description])
        print(tournament_information)

    def display_message_register_player(self):
        print("The tournament requires 4 players. "
              "To register a player, you need their first name, "
              "last name, date of birth, and their national chess player identifier.")

    def present_players(self, players: [Model.Player]):
        print("Registered Players:")
        for player in players:
            print(player.first_name)

    def get_user_response(self, information_request: str) -> str:
        self.response = str(input(information_request))
        while not self.response:
            self.response = str(input(self.message_error))
        return self.response.upper()

    def get_result_of_match(self) -> Model.Result:
        numero = self.get_choice_result()
        match numero:
            case 1:
                return Model.Result.WIN
            case 2:
                return Model.Result.LOSS
            case 3:
                return Model.Result.DRAW

    def display_options(self):
        options = PrettyTable()
        options.field_names = [" ", "What was the result of the match"]
        options.add_row(["1", "White pieces won"])
        options.add_row(["2", "Black pieces won"])
        options.add_row(["3", "It was a draw"])
        print(options)

    def get_choice_result(self) -> int:
        numero = -1
        print(self.options)
        while numero > self.number_of_options or numero <= 0:
            try:
                numero = int(input())
                if numero > self.number_of_options or numero <= 0:
                    print(self.message_error)
            except ValueError:
                print(self.message_error)
                numero = -1
        return numero

    def display_scores(self, players: [Model.Player]):
        scores = PrettyTable()
        scores.field_names = ["ID", "Player", "Score"]
        for player in players:
            scores.add_row([player.chess_national_id, player.first_name, player.score])
        print(scores)

    def display_matches(self, list_of_matches: [Model.Match]):
        for i, match in enumerate(list_of_matches):
            self.display_match(match, number_match=i)

    def display_match(self, match: Model.Match, number_match: int):
        table_match = PrettyTable()
        table_match.field_names = [f"Match number {number_match + 1} -> ",
                                   f"{match.player1.first_name} VS "
                                   f"{match.player2.first_name}"]
        table_match.add_row([f"{match.white_player.first_name}", "Play with white pieces"])
        table_match.add_row([f"{match.black_player.first_name}", "Play with black pieces"])
        print(table_match)

    def display_round(self, round_to_show: Model.Round):
        print(f"{Fore.MAGENTA}Name: {round_to_show.name}{Fore.RESET}")
        print(f"{Fore.MAGENTA}Start Date: {round_to_show.start_datetime}{Fore.RESET}")
        print(f"{Fore.MAGENTA}**** L I S T   O F   M A T C H E S ***{Fore.RESET}")
        self.display_matches(round_to_show.list_of_matches)
        print(f"{Fore.MAGENTA}*** Please enter the chess matches results ***{Fore.RESET}")
