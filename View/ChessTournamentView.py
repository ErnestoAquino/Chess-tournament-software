from prettytable import PrettyTable
# from colorama import init
from colorama import Fore
import Model


# noinspection PyMethodMayBeStatic
class ChessTournamentView:
    """
    This class is responsible for displaying information and interacting with the user related to chess tournaments.
    """

    options: str = f"{Fore.GREEN}What was the result of the match.{Fore.RESET}\n" \
                   f"{Fore.BLUE}1 - White pieces won.{Fore.RESET}\n" \
                   f"{Fore.BLUE}2 - Black pieces won.{Fore.RESET}\n" \
                   f"{Fore.BLUE}3 - It was a draw.{Fore.RESET}\n"
    response: str = None
    number_of_options: int
    message_error: str = f"{Fore.RED}Invalid answer, please try again{Fore.RESET}"

    def __init__(self, number_of_options: int = 3):
        """
        Initialize the ChessTournamentView with the number of options available for match results.

        Args:
            number_of_options (int, optional): The number of options available for match results. Default is 3.
        """
        self.number_of_options = number_of_options

    def display_message_success(self, name: str):
        """
        Display a success message when a tournament is created.

        Args:
            name (str): The name of the tournament that was successfully created.
        """
        print(f"The tournament {name.capitalize()} has been successfully created with the following information:")

    def display_message_tournament_creation(self):
        print("You have decided to create a tournament. Please enter the requested information in order to proceed "
              "with its creation.")

    def display_tournament_information(self, tournament: Model.Tournament):
        """
        Display the information of a chess tournament.

        Args:
            tournament (Model.Tournament): The tournament object containing the information to be displayed.
        """
        tournament_information = PrettyTable()
        tournament_information.field_names = ["Tournament Name", "Location", "Description"]
        tournament_information.add_row([tournament.name, tournament.location, tournament.description])
        print(tournament_information)

    def present_players(self, players: [Model.Player]):
        """
        Present the list of registered players.

        Args:
            players (List[Model.Player]): The list of players to be presented.

        Notes:
            This method prints the first name of each player in the provided list.
        """
        print("Registered Players:")
        for player in players:
            print(player.first_name)

    def get_user_response(self, information_request: str) -> str:
        """
        Get the user's response to the given information request.

        Args:
            information_request (str): The message requesting information from the user.

        Returns:
            str: The user's response in uppercase.

        Notes:
            This method keeps prompting the user for a response until a valid non-empty response is provided.
            It returns the user's response in uppercase.
        """
        self.response = str(input(information_request))
        while not self.response:
            self.response = str(input(self.message_error))
        return self.response.upper()

    def get_result_of_match(self) -> Model.Result:
        """
        Get the result of a chess match based on the user's choice.

        Output:
            Result: The result of the match represented as an enumeration of Model.Result.

        Returns:
            Result: An enumeration representing the result of the match, which can be Result.WIN,
            Result.LOSS, or Result.DRAW.
        """
        numero = self.get_choice_result()
        match numero:
            case 1:
                return Model.Result.WIN
            case 2:
                return Model.Result.LOSS
            case 3:
                return Model.Result.DRAW

    def display_options(self):
        """
        Display the available options for the result of a chess match.

        Output:
            Displays a table of options with their corresponding descriptions.
        """
        options = PrettyTable()
        options.field_names = [" ", "What was the result of the match"]
        options.add_row(["1", "White pieces won"])
        options.add_row(["2", "Black pieces won"])
        options.add_row(["3", "It was a draw"])
        print(options)

    def get_choice_result(self) -> int:
        """
        Get the user's choice for the result of a chess match.

        Returns:
            int: The user's choice as an integer, representing the result of the match.

        Output:
            Displays the available options for the match result.
        """
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
        """
        Display the scores of players in a chess tournament.

        Args:
            players (List[Model.Player]): A list of player objects containing the information to be displayed.

        Output:
            Displays a table with the ID, player's name, and score for each player in the list.
        """
        scores = PrettyTable()
        scores.field_names = ["ID", "Player", "Score"]
        for player in players:
            scores.add_row([player.chess_national_id, player.first_name, player.score])
        print(scores)

    def display_matches(self, list_of_matches: [Model.Match]):
        """
        Display a list of matches in a chess tournament.

        Args:
            list_of_matches (List[Model.Match]): A list of match objects containing the information to be
        displayed.

        Output:
            Displays the details of each match, including the players' names and the color of the
        pieces they are playing with.
        """
        for i, match in enumerate(list_of_matches):
            self.display_match(match, number_match=i)

    def display_match(self, match: Model.Match, number_match: int):
        """
        Display information about a single match in a chess tournament.

        Args:
            match (Model.Match): The match object containing the information to be displayed.
            number_match (int): The number of the match to be displayed.
        Output:
            Displays the match details, including the players' names and the color of the pieces they are playing with.
        """
        table_match = PrettyTable()
        table_match.field_names = [f"Match number {number_match + 1} -> ",
                                   f"{match.player1.first_name} VS "
                                   f"{match.player2.first_name}"]
        table_match.add_row([f"{match.white_player.first_name}", "Play with white pieces"])
        table_match.add_row([f"{match.black_player.first_name}", "Play with black pieces"])
        print(table_match)

    def display_round(self, round_to_show: Model.Round):
        """
        Display information about a round, including its name, start date, and matches.

        Args:
            round_to_show (Model.Round): The round object containing the information to be displayed.
        Output:
            Displays the name and start date of the round, the list of matches in the round, and a prompt for entering
            the chess matches results.
        """
        print(f"{Fore.MAGENTA}Name: {round_to_show.name}{Fore.RESET}")
        print(f"{Fore.MAGENTA}Start Date: {round_to_show.start_datetime}{Fore.RESET}")
        print(f"{Fore.MAGENTA}**** L I S T   O F   M A T C H E S ***{Fore.RESET}")
        self.display_matches(round_to_show.list_of_matches)
        print(f"{Fore.MAGENTA}*** Please enter the chess matches results ***{Fore.RESET}")
