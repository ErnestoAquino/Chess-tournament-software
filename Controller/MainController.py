# import Model
import View
import Controller


class MainController:
    def __init__(self):
        self.chessTournamentController = Controller.ChessTournamentController
        self.mainView = View.MainView

    def start(self):
        self.mainView.display_main_menu()
