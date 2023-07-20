from DataBaseManager import DataBaseManager
import View


class ReportsController:
    """
    This class handles the presentation of reports to the user.

    Attributes:
        reports_view (View.ReportsView): An instance of ReportsView for displaying reports.
        database_manager (DataBaseManager): An instance of DataBaseManager for retrieving data from the database.
    """

    def __init__(self):
        """
        Initialize the ReportsController with ReportsView and DataBaseManager instances.
        """
        self.reports_view = View.ReportsView()
        self.database_manager = DataBaseManager()

    def start(self):
        """
        Start the presentation of reports by letting the user choose from different options.

        The user is presented with a menu to select the type of report they want to see.
        """
        user_choice = self.reports_view.get_choice(number_of_options=5,
                                                   options_to_show=self.reports_view.MESSAGE_OPTIONS)
        self.reports_view.check_if_folder_exist()
        match user_choice:
            case 1:
                self.present_report_all_players()
            case 2:
                self.present_report_all_tournaments()
            case 3:
                self.present_report_one_tournament()
            case 4:
                self.present_report_tournament_players()
            case 5:
                self.present_report_all_round_from_tournament()

    def present_report_all_players(self):
        """
        Presents a report with all players in alphabetical order.

        This method retrieves all players in alphabetical order, sends it to the view to display the report.
        If an error occurs while retrieving the data, it will be caught and an error message will be displayed.

        Raises:
            Exception: If there is an error while retrieving player information from the database.
        """
        try:
            players_to_show = self.database_manager.get_all_players_alphabetical_order()
            self.reports_view.display_players(players_to_show)
        except Exception as e:
            print(f"Error occurred while retrieving players: {e}")

    def present_report_all_tournaments(self):
        """
        Presents a report with all tournaments available.

        This method retrieves tournament information from the database and sends it to the view to display the report.
        If an error occurs while retrieving the data, it will be caught and an error message will be displayed.

        Raises:
            Exception: If there is an error while retrieving tournament information from the database.
        """
        try:
            tournaments_to_show = self.database_manager.get_all_tournaments()
            self.reports_view.display_tournaments(tournaments_to_show)
        except Exception as e:
            print(f"Error occurred while retrieving tournaments: {e}")

    def present_report_one_tournament(self):
        """
        Presents a report with detailed information about a selected tournament.

        The user selects a tournament from the available tournaments, and this method retrieves
        detailed information about that tournament from the database and sends it to the view to display the report.
        If an error occurs while retrieving the data, it will be caught and an error message will be displayed.

        Raises:
            Exception: If there is an error while retrieving tournament information from the database.
        """
        try:
            available_tournaments = self.database_manager.get_all_tournaments()
            user_choice = self.reports_view.show_available_tournaments(available_tournaments)
            selected_tournament = self.database_manager.get_one_tournament(id_tournament=user_choice)
            self.reports_view.display_one_tournament(selected_tournament)
        except Exception as e:
            print(f"Error occurred while retrieving tournaments: {e}")

    def present_report_tournament_players(self):
        """
         Presents a report with players participating in a selected tournament.

         The user selects a tournament from the available tournaments, and this method retrieves
         information about players participating in that tournament from the database
         and sends it to the view to display the report.
         If an error occurs while retrieving the data, it will be caught and an error message will be displayed.

         Raises:
             Exception: If there is an error while retrieving players' tournament information from the database.
         """
        try:
            available_tournaments = self.database_manager.get_all_tournaments()
            user_choice = self.reports_view.show_available_tournaments(available_tournaments)
            players = self.database_manager.get_players_from(id_tournament=user_choice)
            tournament_name = self.database_manager.get_name_tournament(id_tournament=user_choice)
            self.reports_view.display_players_alphabetical_order(players, tournament_name)
        except Exception as e:
            print(f"Error occurred while retrieving players tournament: {e}")

    def present_report_all_round_from_tournament(self):
        """
        Presents a report with all rounds and all matches from a selected tournament.

        The user selects a tournament from the available tournaments, and this method retrieves
        information about all rounds from that tournament from the database
        and sends it to the view to display the report.
        If an error occurs while retrieving the data, it will be caught and an error message will be displayed.

        Raises:
            Exception: If there is an error while retrieving tournament or rounds information from the database.
        """
        try:
            available_tournament = self.database_manager.get_all_tournaments()
            user_choice = self.reports_view.show_available_tournaments(available_tournament)
            selected_tournament = self.database_manager.get_one_tournament(id_tournament=user_choice)
            rounds_of_tournament = self.database_manager.get_rounds_from(id_tournament=user_choice)
            self.reports_view.display_rounds_from_tournament(selected_tournament, rounds_of_tournament)
        except Exception as e:
            print(f"Error occurred while retrieving tournament or rounds information: {e}")
