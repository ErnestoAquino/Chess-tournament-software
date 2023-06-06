import View
import Controller


class MainController:
    NUMBER_OF_OPTIONS: int = 2

    def __init__(self):
        self.chessTournamentController = Controller.ChessTournamentController
        self.main_view = View.MainView()

    def start(self):
        self.main_view.display_main_menu()
        choice = self.get_choice()
        match choice:
            case 1:
                chess_tournament_controller = Controller.ChessTournamentController()

            case 2:
                print("Under construction")

    def get_choice(self) -> int:
        numero = -1
        self.main_view.display_options()
        while numero > self.NUMBER_OF_OPTIONS or numero <= 0:
            try:
                numero = int(input())
                if numero > self.NUMBER_OF_OPTIONS or numero <= 0:
                    self.main_view.display_message_error()
            except ValueError:
                self.main_view.display_message_error()
                numero = -1
        return numero
