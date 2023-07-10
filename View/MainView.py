class MainView:
    NUMBER_OF_OPTIONS: int = 3
    MESSAGE_UNFINISHED_TOURNAMENT = "There is an unfinished tournament. Do you want to resume it?:\n" \
                                    "Please respond with 'yes' or 'no'\n"
    OPTIONS_MESSAGE = "Please, make your selection:\n"
    ERROR_MESSAGE = "Invalid answer, please try again"
    MENU = ("""Welcome to the chess center. Please choose one the following options"
    1 - Create new tournament
    2 - Display reports
    3 - Add new player """)
    response: str = None

    def get_choice(self) -> int:
        numero = -1
        print(self.MENU)
        print(self.OPTIONS_MESSAGE)
        while numero > self.NUMBER_OF_OPTIONS or numero <= 0:
            try:
                numero = int(input())
                if numero > self.NUMBER_OF_OPTIONS or numero <= 0:
                    print(self.ERROR_MESSAGE)
            except ValueError:
                print(self.ERROR_MESSAGE)
                numero = -1
        return numero

    def get_yes_or_no_choice(self) -> str:
        self.response = str(input(self.MESSAGE_UNFINISHED_TOURNAMENT))
        print(self.response.lower())
        while not (self.response.lower() == "yes" or self.response.lower() == "no"):
            self.response = str(input("Please respond with 'yes' or 'no'\n")).lower()
        return self.response
