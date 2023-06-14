import Model
import View


class ChessTournamentController:
    NUMBER_CHESS_PLAYERS: int
    response: str = None

    def __init__(self, number_chess_players: int = 4):
        self.tournament = None
        self.NUMBER_CHESS_PLAYERS = number_chess_players
        self.chess_tournament_view = View.ChessTournamentView()

    def create_tournament(self, name: str, location: str):
        self.tournament = Model.Tournament(name=name, location=location)

    def register_player(self,
                        first_name: str,
                        last_name: str,
                        date_of_birth: str,
                        chess_national_id: str):
        player = Model.Player(first_name=first_name,
                              last_name=last_name,
                              date_of_birth=date_of_birth,
                              chess_national_id=chess_national_id)
        self.tournament.add_player(player)

    def start_tournament(self):
        self.chess_tournament_view.display_message_tournament_creation()
        tournament_name = self.chess_tournament_view.get_user_response(information_request="Tournament Name: ")
        tournament_location = self.chess_tournament_view.get_user_response(information_request="Tournament Location: ")
        self.create_tournament(name=tournament_name, location=tournament_location)
        tournament_description = self.chess_tournament_view.get_user_response(information_request="Tournament "
                                                                                                  "Description: ")
        self.tournament.write_description(tournament_description)
        self.chess_tournament_view.display_message_success(tournament_name)
        self.tournament.load_players()
        # self.chess_tournament_view.present_players(self.tournament.players)
        self.chess_tournament_view.display_scores(self.tournament.players)
        self.tournament.start()
        self.present_rounds()
        self.chess_tournament_view.display_scores(self.tournament.players)
        # self.chess_tournament_view.display_tournament_information(self.tournament)
        # self.register_players(number_of_players=self.NUMBER_CHESS_PLAYERS)
        # self.chess_tournament_view.present_players(players=self.tournament.players)
        # self.tournament.save_players()

    def register_players(self, number_of_players: int):
        self.chess_tournament_view.display_message_register_player()
        for i in range(number_of_players):
            print(f"Player number {i + 1} registration:")
            first_name = self.chess_tournament_view.get_user_response(information_request="First Name: ")
            last_name = self.chess_tournament_view.get_user_response(information_request="Last Name: ")
            date_of_birth = self.chess_tournament_view.get_user_response(information_request="Date of Birth: ")
            national_id = self.chess_tournament_view.get_user_response(information_request="Chess National ID: ")
            player = Model.Player(first_name,
                                  last_name,
                                  date_of_birth,
                                  national_id)
            self.tournament.add_player(player)

    def present_rounds(self):
        for round in self.tournament.rounds:
            print(f"Round {round.name}")
            print(f"Star Date: {round.start_datetime}")
            for match in round.list_of_matches:
                print(f"Match {match.player1.first_name} VS {match.player2.first_name}")
                match.print_color_players()
                print("---------------")
                result = self.chess_tournament_view.get_result_of_match()
                match.set_result(result)
