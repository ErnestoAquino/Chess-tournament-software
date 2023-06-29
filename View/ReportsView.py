import Model


class ReportsView:
    MESSAGE_OPTION = """Please choose one of the following options:
                        1. List of all players in alphabetical order
                        2. List all tournaments\n"""
    ERROR_MESSAGE = "Please enter a valid response\n"

    def get_choice(self, number_of_options: int) -> int:
        numero = -1
        print(self.MESSAGE_OPTION)
        while numero > number_of_options or numero <= 0:
            try:
                numero = int(input())
                if numero > number_of_options or numero <= 0:
                    print(self.ERROR_MESSAGE)
            except ValueError:
                print(self.ERROR_MESSAGE)
                numero = -1
        return numero

    def display_players(self, players: [Model.Player]):
        pass
