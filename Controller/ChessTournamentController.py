import Model
import View


class ChessTournamentController:
    NUMBER_CHESS_PLAYERS: int
    response: str = None

    def __init__(self, number_chess_players: int = 4):
        self.tournament = None
        self.NUMBER_CHESS_PLAYERS = number_chess_players

    def create_tournament(self, name: str, location: str):
        self.tournament = Model.Tournament(name = name, location = location)

    def register_player(self,
                        first_name: str,
                        last_name: str,
                        date_of_birth: str,
                        chess_national_id: str):
        player = Model.Player(first_name = first_name,
                              last_name = last_name,
                              date_of_birth = date_of_birth,
                              chess_national_id = chess_national_id)
        self.tournament.add_player(player)

    def start_tournament(self):
        View.ChessTournamentView.display_message_tournament_creation()
        tournament_name = self.get_user_response(information_request = "Tournament Name: ")
        tournament_location = self.get_user_response(information_request = "Tournament Location: ")
        self.create_tournament(name = tournament_name, location = tournament_location)
        tournament_description = self.get_user_response(information_request = "Tournament Description: ")
        self.tournament.write_description(tournament_description)
        View.ChessTournamentView.display_message_success(tournament_name)
        View.ChessTournamentView.display_tournament_information(self.tournament)
        self.register_players(number_of_players = self.NUMBER_CHESS_PLAYERS)
        View.ChessTournamentView.present_players(players = self.tournament.players)

    def register_players(self, number_of_players: int):
        View.ChessTournamentView.display_message_register_player()
        for i in range(number_of_players):
            print(f"Player number {i + 1} registration:")
            first_name = self.get_user_response(information_request = "First Name: ")
            last_name = self.get_user_response(information_request = "Last Name: ")
            date_of_birth = self.get_user_response(information_request = "Date of Birth: ")
            national_id = self.get_user_response(information_request = "Chess National ID: ")
            player = Model.Player(first_name,
                                  last_name,
                                  date_of_birth,
                                  national_id)
            self.tournament.add_player(player)

    def get_user_response(self, information_request: str):
        self.response = str(input(information_request))
        while not self.response:
            self.response = str(input("Please, enter a valid response\n"))
        return self.response
