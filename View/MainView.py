class MainView:
    NUMBER_OF_OPTIONS: int = 2

    def display_main_menu(self):
        print("""Welcome to the chess center. Please choose one the following options"
        1 - Create new tournament
        2 - Display reports""")

    def display_options(self):
        print("Please, make your selection:\n")

    def display_message_error(self):
        print("Invalid answer, please try again")

    def get_choice(self) -> int:
        numero = -1
        self.display_options()
        while numero > self.NUMBER_OF_OPTIONS or numero <= 0:
            try:
                numero = int(input())
                if numero > self.NUMBER_OF_OPTIONS or numero <= 0:
                    self.display_message_error()
            except ValueError:
                self.display_message_error()
                numero = -1
        return numero
