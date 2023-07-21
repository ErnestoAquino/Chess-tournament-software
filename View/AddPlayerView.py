import Model


class AddPlayerView:
    """
    This class is responsible for interacting with the user to add players to the database.
    """

    def __init__(self, number_of_players_to_add: int = 2):
        """
        Initialize the AddPlayerView with the AddPlayerController and other instance variables.
        """
        self.number_of_players_to_add = number_of_players_to_add
        self.players = []
        self.response = None
        self.add_more_player = True
        self.MESSAGE = ("To add a pair of players to the database, you will need their name, "
                        "last name, date of birth, and their national chess identification for each player. "
                        "Please have this information ready."
                        "Due to association rules, please note that you can only add an even number of players.")

    def get_players_to_save(self) -> [Model.Player]:
        """
        Prompt the user to enter information for two players and return the list of created players.

        Returns:
            List[Model.Player]: A list containing the two players created by the user.
        """
        print(self.MESSAGE)
        while self.add_more_player:
            for i in range(self.number_of_players_to_add):
                print(f"Player {i + 1}:\n")
                first_name = self.get_user_response("First Name:")
                last_name = self.get_user_response("Last Name:")
                date_of_birth = self.get_user_response("Date of Birth:")
                national_id = self.get_user_response("Chess National ID:")
                new_player = Model.Player(first_name, last_name, date_of_birth, national_id)
                self.players.append(new_player)
            more_player = self.get_yes_no_response()
            if more_player == "no":
                self.add_more_player = False
        return self.players

    def get_user_response(self, information_request: str) -> str:
        """
        Prompt the user to enter a response for the given information request and return the response.

        Args:
            information_request (str): The information the user needs to provide.

        Returns:
            str: The user's response.
        """
        self.response = str(input(information_request))
        while not self.response:
            self.response = str(input("Please enter a valid response\n"))
        return self.response.upper()

    def get_yes_no_response(self) -> str:
        """
        Prompt the user to enter a response of 'yes' or 'no' and return the response.

        Returns:
            str: The user's response ('yes' or 'no').
        """
        self.response = str(input("Would you like to add two more players?,\n"
                                  "Please respond with 'yes' or 'no'")).lower()
        while not (self.response.lower() == "yes" or self.response.lower() == "no"):
            self.response = str(input("Please respond with 'yes' or 'no'\n")).lower()
        if self.response == "no":
            self.add_more_player = False
        return self.response
