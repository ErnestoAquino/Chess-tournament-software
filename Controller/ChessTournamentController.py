
import DataBaseManager
import Model
import View


class ChessTournamentController:
    """
        Controller class for managing a chess tournament.
    """
    response: str = None

    def __init__(self):
        """
        Initializes the ChessTournamentController.
        """
        self.tournament = None
        self.chess_tournament_view = View.ChessTournamentView()
        self.data_base_manager = DataBaseManager.DataBaseManager()

    def create_tournament(self, name: str, location: str):
        """
        Creates a new tournament with the given name and location.

        Args:
            name (str): The name of the tournament.
            location (str): The location of the tournament.

        Returns:
            None
        """
        self.tournament = Model.Tournament(name=name, location=location)
        self.save_tournament_progress()

    def prepared_tournament(self):
        """
        Prepares the tournament by gathering required information from the user.
        """
        self.chess_tournament_view.display_message_tournament_creation()
        tournament_name = self.chess_tournament_view.get_user_response(information_request="Tournament Name: ")
        tournament_location = self.chess_tournament_view.get_user_response(
            information_request="Tournament Location: ")
        self.create_tournament(tournament_name, tournament_location)
        tournament_description = self.chess_tournament_view.get_user_response(information_request="Tournament "
                                                                                                  "Description: ")
        self.tournament.write_description(tournament_description)
        self.save_tournament_progress()

    def start_tournament(self):
        self.prepared_tournament()
        self.chess_tournament_view.display_tournament_information(self.tournament)
        self.tournament.load_players()
        self.save_tournament_progress()
        self.create_the_rounds()
        self.finalize_the_tournament()

    def present_round(self, round_to_show: Model.Round):
        """
        "Presents a round of the tournament to the user for entering the result of each match in the round."

        Args:
            round_to_show (Model.Round): The round to present.
        """
        self.chess_tournament_view.display_round(round_to_show)
        for i, match in enumerate(round_to_show.list_of_matches):
            self.chess_tournament_view.display_match(match, number_match=i)
            if match.result == Model.Result.TO_BE_PLAYED:
                result = self.chess_tournament_view.get_result_of_match()
                match.set_result(result)
                self.save_tournament_progress()
        round_to_show.write_end_datetime()
        self.tournament.current_round += 1
        self.save_tournament_progress()

    def create_round(self, number_of_round: int):
        """
        Creates a new round for the tournament.

        Args:
            number_of_round (int): The number of the round to create.
        """
        self.tournament.sort_players()
        new_round = Model.Round(name=f"Round {number_of_round}")
        self.tournament.sort_players()
        try:
            pairings = self.tournament.generate_matches()
            for match in pairings:
                match.player1.id_played.append(match.player2.chess_national_id)
                match.player2.id_played.append(match.player1.chess_national_id)
                new_round.add_mach(match)
        except ValueError as error:
            print("Error", str(error))
        self.tournament.rounds.append(new_round)
        self.save_tournament_progress()

    def create_the_rounds(self):
        """
        Creates all the rounds for the tournament.
        """
        self.create_first_round()
        self.present_round(round_to_show=self.tournament.rounds[0])
        self.save_tournament_progress()
        for round_number in range(2, self.tournament.number_of_rounds + 1):
            self.create_round(round_number)
            self.present_round(self.tournament.rounds[round_number - 1])
            self.save_tournament_progress()
            print(len(self.tournament.rounds[round_number - 1].list_of_matches))

    def create_first_round(self):
        """
        Creates the first round of the tournament.

        Note:
            The first round, shuffle the players randomly.
        """
        self.tournament.shuffle_players()
        first_round = Model.Round(name="Round 1")
        for i in range(0, len(self.tournament.players), 2):
            player1 = self.tournament.players[i]
            player2 = self.tournament.players[i + 1]
            player1.id_played.append(player2.chess_national_id)
            player2.id_played.append(player1.chess_national_id)
            match = Model.Match(player1, player2)
            first_round.add_mach(match)
        self.tournament.rounds.append(first_round)
        self.tournament.current_round += 1
        self.save_tournament_progress()

    def save_tournament(self):
        self.data_base_manager.save_tournament(self.tournament)
        self.data_base_manager.delete_unfinished_tournament()

    def build_interrupted_tournament(self):
        tournament_information = self.data_base_manager.load_unfinished_tournament()
        print(tournament_information)
        self.tournament = Model.Tournament.load_from_dictionary(tournament_information)

    def resume_tournament(self):
        self.build_interrupted_tournament()
        current_round_index = self.tournament.current_round - 1
        current_round = self.tournament.rounds[current_round_index]
        self.present_round(current_round)
        self.save_tournament_progress()
        for round_number in range(len(self.tournament.rounds) + 1, self.tournament.number_of_rounds + 1):
            self.create_round(round_number)
            self.present_round(self.tournament.rounds[round_number - 1])
            self.save_tournament_progress()
        self.finalize_the_tournament()

    def finalize_the_tournament(self):
        """
        Finalizes the tournament.

        Note:
             Players are sorted by points, presented to the user, the tournament end date is recorded,
             and it is saved to the database.
        """
        self.tournament.sort_players()
        self.chess_tournament_view.display_scores(self.tournament.players)
        self.tournament.write_end_date()
        self.save_tournament()

    def delete_unfinished_tournament(self):
        self.data_base_manager.delete_unfinished_tournament()

    def save_tournament_progress(self):
        self.data_base_manager.make_check_point_tournament(self.tournament.to_dictionary())
