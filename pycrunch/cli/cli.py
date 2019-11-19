class Cli:

    def __init__(self):
        self.options = ['NFL', 'NBA', 'MLB']

    def start(self):
        print("\nChoose a sport:")
        self.show_options()
        self.get_choice()

    def show_options(self):
        for i, option in enumerate(self.options, start=1):
            print(f"{i}) {option}")

    def get_choice(self):
        choice = input()
        print(f"Your choice was: {choice}")
