class Player:
    cards_array = []
    name = "player"

    def __init__(self, name, cards_array):
        self.cards_array = cards_array
        self.name = name
        
    def get_player_cli_input(self):
        str = ''
        for i in range(len(self.cards_array)):
            str += str(self.cards_array[i])

    def get_ai_input(self):
        pass
