from colorama import init
from colorama import Fore


class MainView:
    NUMBER_OF_OPTIONS: int = 3

    MESSAGE_UNFINISHED_TOURNAMENT = ("There is an unfinished tournament.\n"
                                     "Do you want to resume it?:\n"
                                     "Please respond with 'yes' or 'no'.\n")
    OPTION_MENU = ("1 - Create new tournament.\n"
                   "2 - Display reports.\n"
                   "3 - Add new player.")
    WELCOME_MESSAGE = "Welcome to the chess center, please choose one the following options:"
    RESPONSE_INSTRUCTION = "Please respond with 'yes' or 'no'."
    OPTIONS_MESSAGE = "Please, make your selection:"
    ERROR_MESSAGE = "Invalid answer, please try again."
    response: str = None

    def get_choice(self) -> int:
        numero = -1
        print(self.apply_color(self.WELCOME_MESSAGE, Fore.GREEN))
        print(self.apply_color(self.OPTION_MENU, Fore.LIGHTBLUE_EX))
        print(self.apply_color(self.OPTIONS_MESSAGE, Fore.GREEN))
        while numero > self.NUMBER_OF_OPTIONS or numero <= 0:
            try:
                numero = int(input())
                if numero > self.NUMBER_OF_OPTIONS or numero <= 0:
                    print(self.apply_color(self.ERROR_MESSAGE, Fore.LIGHTRED_EX))
            except ValueError:
                print(self.apply_color(self.ERROR_MESSAGE, Fore.LIGHTRED_EX))
                numero = -1
        return numero

    def get_yes_or_no_choice(self) -> str:
        self.response = str(input(self.apply_color(self.MESSAGE_UNFINISHED_TOURNAMENT, Fore.GREEN)))
        while not (self.response.lower() == "yes" or self.response.lower() == "no"):
            self.response = str(input(self.apply_color(self.RESPONSE_INSTRUCTION, Fore.LIGHTRED_EX))).lower()
        return self.response

    @staticmethod
    def apply_color(text: str, color: Fore) -> str:
        init()
        colored_text = f"{color}{text}{Fore.RESET}"
        return colored_text
