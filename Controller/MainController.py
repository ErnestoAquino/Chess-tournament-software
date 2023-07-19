import View
import Controller
import DataBaseManager


class MainController:
    """
    Main controller for the chess tournament program.

    Attributes:
        chess_tournament_controller (ChessTournamentController):
            Controller for managing chess tournaments.
        add_player_controller (AddPlayerController):
            Controller for adding players to the database.
        reports_controller (ReportsController):
            Controller for generating reports.
        main_view (MainView):
            View for displaying the main menu.
        database_manager (DataBaseManager):
            Manager for interacting with the database.
    """

    def __init__(self):
        """
        Initializes the MainController with its required components.
        """
        self.chess_tournament_controller = Controller.ChessTournamentController()
        self.add_player_controller = Controller.AddPlayerController()
        self.reports_controller = Controller.ReportsController()
        self.main_view = View.MainView()
        self.database_manager = DataBaseManager.DataBaseManager()

    def start(self):
        """
        Starts the chess tournament application.

        If there is an unfinished tournament in the database, the user is prompted
        to resume it. Otherwise, the user is presented with the main menu to choose
        from different options like starting a new tournament, viewing reports, or
        adding players.
        """
        if self.database_manager.check_unfinished_tournament() and self.main_view.get_yes_or_no_choice() == "yes":
            self.chess_tournament_controller.resume_tournament()
        else:
            self.chess_tournament_controller.delete_unfinished_tournament()
            choice = self.main_view.get_choice()
            match choice:
                case 1:
                    self.chess_tournament_controller.start_tournament()
                case 2:
                    self.reports_controller.start()
                case 3:
                    self.add_player_controller.get_players_to_save()
