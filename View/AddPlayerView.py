import Controller
import Model


class AddPlayerView:
    MESSAGE: str = ("To add a pair of players to the database, you will need their name, "
                    "last name, date of birth, and their national chess identification for each player. "
                    "Please have this information ready."
                    "Due to association rules, please note that you can only add an even number of players.")
    PLAYERS_TO_ADD: int = 2
    players = []
    response: str = None
    add_more_player: bool = True

    # def __init__(self):
    # self.add_player_controller = Controller.AddPlayerController()

    def players_to_save(self) -> [Model.Player]:
        print(self.MESSAGE)
        while self.add_more_player:
            for i in range(self.PLAYERS_TO_ADD):
                print(f"Player {i + 1}:\n")
                first_name = self.get_user_response("First Name:")
                last_name = self.get_user_response("Last Name:")
                date_of_birth = self.get_user_response("Date of Birth:")
                national_id = self.get_user_response("Chess National ID:")
                new_player = Model.Player(first_name,
                                          last_name,
                                          date_of_birth,
                                          national_id)
                self.players.append(new_player)
            more_player = self.get_yes_no_response()
            if more_player == "no":
                self.add_more_player = False
        return self.players

    def get_user_response(self, information_request: str) -> str:
        self.response = str(input(information_request))
        while not self.response:
            self.response = str(input("Please enter a valid response\n"))
        return self.response.upper()

    def get_yes_no_response(self) -> str:
        self.response = str(input("Would you like to add two more players?,\n"
                                  "Please respond with 'yes' or 'no'")).lower()
        while not (self.response.lower() == "yes" or self.response.lower() == "no"):
            self.response = str(input("Please respond with 'yes' or 'no'\n")).lower()
        if self.response == "no":
            self.add_more_player = False
        return self.response
