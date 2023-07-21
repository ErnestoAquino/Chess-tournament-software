from typing import List
from Model import Player
from DataBaseManager import DataBaseManager
from View import AddPlayerView


class AddPlayerController:
    """
    The AddPlayerController class manages the process of adding and saving new players.
    """
    players: List[Player] = []

    def __init__(self):
        """
        Initializes an instance of the AddPlayerController class.

        The constructor creates an instance of the AddPlayerView to handle user input
        and an instance of the DataBaseManager to manage database interactions.
        """
        self.add_player_view = AddPlayerView()
        self.database_manager = DataBaseManager()

    def get_players_to_save(self):
        """
        Retrieves the players to be saved from the AddPlayerView.

        This method uses the AddPlayerView to prompt the user for player information,
        and then stores the entered players in the 'players' attribute.
        """
        self.players = self.add_player_view.get_players_to_save()
        self.save_players()

    def save_players(self):
        """
        Saves the list of players to the database using the DataBaseManager.

        This method calls the 'save_players' method of the DataBaseManager,
        passing the list of players to be saved. The database manager handles
        the process of storing the player data in the database.
        """
        self.database_manager.save_players(self.players)
