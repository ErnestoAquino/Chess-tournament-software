import Model

# juan = Model.Player(first_name="Juanito",
#                     last_name="Perez",
#                     date_of_bird="03/09/1990",
#                     chess_national_id = "AB234")
#
# pepe = Model.Player(first_name="Chalino",
#                     last_name="Manuelito",
#                     date_of_bird="09/12/2000",
#                     chess_national_id = "AB765")
#
# print("SCORE BEFORE MATCH")
# print(f"score of {juan.first_name} is {juan.score}")
# print(f"score of {pepe.first_name} is {pepe.score}")
# first_match = Model.Match(player1=juan, player2=pepe)
# first_match.set_result_test(Model.Result.WIN)
# print("SCORE AFTER FIRST MATCH")
# print(f"score of {juan.first_name} is {juan.score}")
# print(f"score of {pepe.first_name} is {pepe.score}")
# second_match = Model.Match(player1=juan, player2=pepe)
# second_match.set_result_test(Model.Result.WIN)
# print("SCORE AFTER SECOND MATCH")
# print(f"score of {juan.first_name} is {juan.score}")
# print(f"score of {pepe.first_name} is {pepe.score}")
# third_match = Model.Match(player1=juan, player2=pepe)
# third_match.set_result_test(Model.Result.LOSS)
# print("SCORE AFTER THIRD MATCH")
# print(f"score of {juan.first_name} is {juan.score}")
# print(f"score of {pepe.first_name} is {pepe.score}")
# fourth_match = Model.Match(player1=juan, player2=pepe)
# fourth_match.set_result_test(Model.Result.DRAW)
# print("SCORE AFTER FOURTH MATCH")
# print(f"score of {juan.first_name} is {juan.score}")
# print(f"score of {pepe.first_name} is {pepe.score}")
#
# roundOne = Model.Round(name="Round 1")
# roundOne.add_mach(first_match)
# roundOne.add_mach(second_match)
# roundOne.add_mach(third_match)
# roundOne.add_mach(fourth_match)
# for match in roundOne.list_of_matches:
#     print(match.result.name)
# print(roundOne.start_datetime)
# roundOne.write_end_datetime()
# print(roundOne.end_datetime)
# print("TEST TOURNAMENT")
# new_tournament = Model.Tournament(name = "Torneo San Benito", location = "Oaxaca")
# print(new_tournament.start_date)


def main():
    print("Tournament Creation")
    new_tournament = Model.Tournament(name = "Torneo San Benito", location = "Mexico")
    print(new_tournament.start_date)


if __name__ == '__main__':
    main()
