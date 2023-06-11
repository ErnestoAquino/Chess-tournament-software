import View
import Controller


class MainController:

    def __init__(self):
        self.chess_tournament_controller = Controller.ChessTournamentController()
        self.main_view = View.MainView()

    def start(self):
        self.main_view.display_main_menu()
        choice = self.main_view.get_choice()
        match choice:
            case 1:
                self.chess_tournament_controller.start_tournament()
            case 2:
                print("Under construction")
            case 3:
                print("Under construction")
