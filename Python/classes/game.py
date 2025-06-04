from classes.player import Player
import random

class Game():
    deck = []
    players = []
    board = [[],[],[],[]]

    def __init__ (self, player_count):
        self.deck = self.get_deck()
        for row in self.board:
            # pop element from deck (already shuffled) and append
            row.append(self.deck.pop())
        self.board.sort(key=lambda x: x[-1])

        # Add players
        for i in range(player_count):
            self.players.append(Player( "Player"+str(i+1),self.draw_player_cards()))

    def get_deck(self):
        deck = list(range(1, 105))
        random.shuffle(deck)
        return deck

    def print_state(self):
        for i in range(len(self.board)):
            print("Row ", i+1, self.board[i])

    def draw_player_cards(self):
        player_cards = []
        for i in range(10):
            player_cards.append(self.deck.pop())
        player_cards.sort()
        return player_cards