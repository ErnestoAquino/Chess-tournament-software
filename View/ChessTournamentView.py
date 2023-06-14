import Model


# noinspection PyMethodMayBeStatic
class ChessTournamentView:
    response: str = None
    number_of_options: int
    message_error: str = "Invalid answer, please try again"

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
        print(f"Name: {tournament.name}")
        print(f"Location: {tournament.location}")
        print(f"Description: {tournament.description}")

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
            self.response = str(input("Please enter a valid response"))
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
        print("What was the result of the match?")
        print("1. The white pieces won.")
        print("2. The black pieces won.")
        print("3. It was a draw.")

    def get_choice_result(self) -> int:
        numero = -1
        self.display_options()
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
        for player in players:
            print(f"Player: {player.first_name} Score: {player.score}")
