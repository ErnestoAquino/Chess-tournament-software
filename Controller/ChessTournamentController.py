from typing import List
from typing import Set
import itertools
import DataBaseManager
import Model
import View


class ChessTournamentController:
    NUMBER_CHESS_PLAYERS: int
    response: str = None

    def __init__(self, number_chess_players: int = 4):
        self.tournament = None
        self.NUMBER_CHESS_PLAYERS = number_chess_players
        self.chess_tournament_view = View.ChessTournamentView()
        self.data_base_manager = DataBaseManager.DataBaseManager()

    def create_tournament(self, name: str, location: str):
        self.tournament = Model.Tournament(name=name, location=location)
        self.data_base_manager.checkpoint_creation_tournament(self.tournament)

    # Todo This methode can be deleted

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

    def prepared_tournament(self):
        self.chess_tournament_view.display_message_tournament_creation()
        tournament_name = self.chess_tournament_view.get_user_response(information_request="Tournament Name: ")
        tournament_location = self.chess_tournament_view.get_user_response(
            information_request="Tournament Location: ")
        self.create_tournament(tournament_name, tournament_location)
        tournament_description = self.chess_tournament_view.get_user_response(information_request="Tournament "
                                                                                                  "Description: ")
        self.data_base_manager.checkpoint_add_tournament_description(tournament_description)
        self.tournament.write_description(tournament_description)

    def start_tournament(self):
        self.prepared_tournament()
        self.chess_tournament_view.display_tournament_information(self.tournament)
        self.tournament.load_players()
        self.data_base_manager.checkpoint_players(self.tournament)
        self.chess_tournament_view.display_scores(self.tournament.players)
        self.create_the_rounds()
        self.tournament.sort_players()
        self.chess_tournament_view.display_scores(self.tournament.players)
        self.tournament.write_end_date()
        self.save_tournament()

    def present_round(self, round_to_show: Model.Round):
        self.chess_tournament_view.display_round(round_to_show)
        for i, match in enumerate(round_to_show.list_of_matches):
            self.chess_tournament_view.display_match(match, number_match=i)
            result = self.chess_tournament_view.get_result_of_match()
            match.set_result(result)
            self.data_base_manager.update_result_match(self.tournament.current_round,
                                                       number_of_match=i,
                                                       result=result)
        round_to_show.write_end_datetime()
        self.data_base_manager.update_end_datetime_round(round_id=self.tournament.current_round,
                                                         datetime=round_to_show.end_datetime)
        self.data_base_manager.checkpoint_players(self.tournament)
        self.tournament.current_round += 1

    def create_first_round(self):
        self.tournament.shuffle_players()
        first_round = Model.Round(name="Round 1")
        for i in range(0, len(self.tournament.players), 2):
            player1 = self.tournament.players[i]
            player2 = self.tournament.players[i + 1]
            player1.played_players.append(player2)
            player2.played_players.append(player1)
            match = Model.Match(player1, player2)
            first_round.add_mach(match)
        self.tournament.rounds.append(first_round)
        self.tournament.current_round += 1
        self.data_base_manager.checkpoint_round(self.tournament.rounds)
        self.data_base_manager.checkpoint_players(self.tournament)

    def generate_matches(self, previous_matches: Set[frozenset]) \
            -> List[Model.Match]:
        self.tournament.sort_players()
        pairings = []
        available_players = self.tournament.players[:]
        for i in range(0, len(available_players), 2):
            player1 = available_players[i]
            player2 = available_players[i + 1]
            if not any({player1, player2} == match or {player2, player1} == match for match in previous_matches):
                pairings.append(Model.Match(player1, player2))
                previous_matches.add(frozenset({player1, player2}))
        return pairings

    def generate_matches_test(self) -> List[Model.Match]:
        self.tournament.sort_players()
        pairings = []
        paired_players = []
        players_with_pair = []

        for i, player in enumerate(self.tournament.players):
            for j, pair in enumerate(itertools.combinations(self.tournament.players, 2)):
                if pair[1] not in pair[0].played_players and pair[0] not in pair[1].played_players and \
                        player == pair[0] and pair not in paired_players and pair[0] not in players_with_pair \
                        and pair[1] not in players_with_pair:
                    paired_players.append(pair)
                    player1 = pair[0]
                    player2 = pair[1]
                    pairings.append(Model.Match(player1, player2))
                    players_with_pair.append(pair[0])
                    players_with_pair.append(pair[1])

        possibles_chess_games = itertools.combinations(self.tournament.players, 2)
        for possible_game in possibles_chess_games:
            player1, player2 = possible_game
            print(player1.first_name, player2.first_name)
        return pairings

    def create_round(self, number_of_round: int):
        self.tournament.sort_players()
        new_round = Model.Round(name=f"Round {number_of_round}")
        pairings = self.generate_matches_test()
        for match in pairings:
            match.player1.played_players.append(match.player2)
            match.player2.played_players.append(match.player1)
            new_round.add_mach(match)
        self.tournament.rounds.append(new_round)

    def create_the_rounds(self):
        self.create_first_round()
        self.present_round(round_to_show=self.tournament.rounds[0])
        for round_number in range(2, self.tournament.number_of_rounds + 1):
            self.create_round(round_number)
            self.present_round(self.tournament.rounds[round_number - 1])
            print(len(self.tournament.rounds[round_number - 1].list_of_matches))
            self.print_played_player()

    def print_played_player(self):
        for player in self.tournament.players:
            print(f"{player.first_name}")
            player.test_print_opponents()

    def save_tournament(self):
        self.data_base_manager.save_tournament(self.tournament)

    def load_interrupted_tournament(self):
        pass
