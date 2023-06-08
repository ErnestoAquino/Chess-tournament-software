import Model


class ChessTournamentView:
    @staticmethod
    def display_message_success(name: str):
        print(f"The tournament {name} has been successfully created with the following information:")

    @staticmethod
    def display_message_tournament_creation():
        print("You have decided to create a tournament. Please enter the requested information in order to proceed "
              "with its creation.")

    @staticmethod
    def display_message_naming():
        print("Please, enter the name of the chess tournament:")

    @staticmethod
    def display_message_location():
        print("Please, enter the location of the chess tournament:")

    @staticmethod
    def display_message_description():
        print("Please enter the description of the tournament.")

    @staticmethod
    def display_players(players: [Model.Player]):
        print("Registered players:")
        for player in players:
            print(player.first_name)

    @staticmethod
    def display_tournament_information(tournament: Model.Tournament):
        print(f"Tournament name: {tournament.name}")
        print(f"Tournament location: {tournament.location}")
        print(f"Tournament description: {tournament.description}")

    @staticmethod
    def display_message_register_player():
        print("The tournament requires 4 players. "
              "To register a player, you need their first name, "
              "last name, date of birth, and their national chess player identifier.")

    @staticmethod
    def present_players(players: [Model.Player]):
        print("Registered Players:")
        for player in players:
            print(player.first_name)
