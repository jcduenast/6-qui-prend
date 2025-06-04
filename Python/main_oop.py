from classes.game import Game
from classes.player import Player


game = Game(4)

for player in game.players:
    print(player.cards_array)
print("Game:")
print(game.print_state())

