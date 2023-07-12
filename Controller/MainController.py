import View
import Controller
import DataBaseManager


class MainController:

    def __init__(self):
        self.chess_tournament_controller = Controller.ChessTournamentController()
        self.add_player_controller = Controller.AddPlayerController()
        self.reports_controller = Controller.ReportsController()
        self.main_view = View.MainView()
        self.database_manager = DataBaseManager.DataBaseManager()

    def start(self):
        if self.database_manager.check_unfinished_tournament() and self.main_view.get_yes_or_no_choice() == "yes":
            # Todo Write code to load unfinished tournament.
            self.database_manager.load_unfinished_tournament()
            print("Here is the code to resume the unfinished tournament")
        else:
            self.database_manager.delete_unfinished_tournament()
            choice = self.main_view.get_choice()
            match choice:
                case 1:
                    self.chess_tournament_controller.start_tournament()
                case 2:
                    self.reports_controller.start()
                case 3:
                    self.add_player_controller.get_players_to_save()
