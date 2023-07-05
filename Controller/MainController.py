import View
import Controller


class MainController:

    def __init__(self):
        self.chess_tournament_controller = Controller.ChessTournamentController()
        self.add_player_controller = Controller.AddPlayerController()
        self.reports_controller = Controller.ReportsController()
        self.main_view = View.MainView()

    def start(self):
        self.main_view.display_main_menu()
        choice = self.main_view.get_choice()
        match choice:
            case 1:
                self.chess_tournament_controller.start_tournament()
            case 2:
                self.reports_controller.start()
            case 3:
                self.add_player_controller.get_players_to_save()
