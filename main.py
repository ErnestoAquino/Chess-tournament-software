import Controller
import Model
import View


def get_yes_no_response() -> str:
    response = str(input("Please respond with 'yes' or 'no'"))
    while not (response.lower() == "yes" or response.lower() == "no"):
        response = str(input("Please respond with 'yes' or 'no'"))
    return response.upper()


def main():
    # response = get_yes_no_response()
    # print(f"La respuesta fue: {response}")
    # add_player_controller = Controller.AddPlayerController()
    # add_player_controller.get_players_to_save()
    # player_view = View.AddPlayerView()
    # players = player_view.players_to_save()
    # for player in players:
    #     print(player.first_name)
    controller = Controller.MainController()
    controller.start()
    # new_tournament = Model.Tournament(name = "Reyes", location = "Mexico")
    # new_tournament.load_players()
    # new_tournament.shuffle_players()
    # first_round = Model.Round(name = "Round 1")
    # for i in range(0, len(new_tournament.players), 2):
    #     match = Model.Match(player1 = new_tournament.players[i], player2 = new_tournament.players[i + 1])
    #     new_tournament.players[i].played_players.append(new_tournament.players[i + 1])
    #     new_tournament.players[i + 1].played_players.append(new_tournament.players[i])
    #     first_round.add_mach(match)
    # new_tournament.rounds.append(first_round)
    # print(len(new_tournament.rounds[0].list_of_matches))
    # for i in new_tournament.players:
    #     print(f"{i.first_name}")
    #     i.test_print_opponents()
    # new_tournament.sort_players()
    #
    # new_tournament.shuffle_players()
    # new_round = Model.Round(name = "Round 2")
    # print(len(new_round.list_of_matches))
    # for i in range(0, len(new_tournament.players), 2):
    #     print(f"Macht numero {i}")
    #     match = Model.Match(player1 = new_tournament.players[i], player2 = new_tournament.players[i + 1])
    #     new_tournament.players[i].played_players.append(new_tournament.players[i + 1])
    #     new_tournament.players[i + 1].played_players.append(new_tournament.players[i])
    #     new_round.add_mach(match)
    #     print(len(new_round.list_of_matches))
    # new_tournament.rounds.append(new_round)
    # print(len(new_tournament.rounds[1].list_of_matches))
    # for i in new_tournament.players:
    #     print(f"{i.first_name}")
    #     i.test_print_opponents()
    #
    # new_tournament.shuffle_players()
    # terser_round = Model.Round(name = "Round 3")
    # print(len(terser_round.list_of_matches))
    # for i in range(0, len(new_tournament.players), 2):
    #     print(f"Macht numero {i}")
    #     match = Model.Match(player1 = new_tournament.players[i], player2 = new_tournament.players[i + 1])
    #     terser_round.add_mach(match)
    #     print(len(terser_round.list_of_matches))
    # new_tournament.rounds.append(terser_round)
    # for r in new_tournament.rounds:
    #     print("-----------------------------------------------------")
    #     for m in r.list_of_matches:
    #         print(f"{m.player1.first_name} VS {m.player2.first_name}")

    # self.tournament.add_round(first_round)
    # player1 = Model.Player(first_name = "Ernesto",
    #                        last_name = "Aquino",
    #                        date_of_birth = "03/08/1980",
    #                        chess_national_id = "WE234")
    # player2 = Model.Player(first_name = "Amandine",
    #                        last_name = "Aquino",
    #                        date_of_birth = "05/12/1980",
    #                        chess_national_id = "DF094")

    # print("BEFORE MATCH")
    # print(f"{player1.first_name} has {player1.score} pts")
    # print(f"{player2.first_name} has {player2.score} pts")
    # match = Model.Match(player1 = player1, player2 = player2)
    # match.print_color_players()
    # print("AFTER MATCH")
    # match.set_result(Model.Result.WIN)
    # print(f"{player1.first_name} has {player1.score} pts")
    # print(f"{player2.first_name} has {player2.score} pts")
    # match.set_result(Model.Result.WIN)
    # print(f"{player1.first_name} has {player1.score} pts")
    # print(f"{player2.first_name} has {player2.score} pts")
    # match.set_result(Model.Result.DRAW)
    # print(f"{player1.first_name} has {player1.score} pts")
    # print(f"{player2.first_name} has {player2.score} pts")

    # player3 = Model.Player(first_name = "Anna-Gabrielle",
    #                        last_name = "La Nena",
    #                        date_of_birth = "29/08/2013",
    #                        chess_national_id = "WE023",)
    # player4 = Model.Player(first_name = "Pinpon",
    #                        last_name = "Sin puentes",
    #                        date_of_birth = "12/12/2012",
    #                        chess_national_id = "LK094")
    # new_tournament = Model.Tournament(name = "Kings",location = "France")
    # new_tournament.add_player(player1)
    # new_tournament.add_player(player2)
    # new_tournament.add_player(player3)
    # new_tournament.add_player(player4)
    # for player in new_tournament.players:
    #     print(player.first_name)
    # print("SHUFFLE PLAYERS")
    # new_tournament.shuffle_players()
    # for player in new_tournament.players:
    #     print(player.first_name)
    # print("Creation del primer round")
    # new_tournament.create_first_round()
    # for r in new_tournament.rounds:
    #     print(r.name)
    #     print(r.start_datetime)
    #     for match in r.list_of_matches:
    #         print(f"Match: {match.player1.first_name} VS {match.player2.first_name}")
    #         match.print_color_players()


if __name__ == '__main__':
    main()
