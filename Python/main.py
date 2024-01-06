import random

def get_deck():
    deck = list(range(1, 105))
    random.shuffle(deck)
    return deck

def start_game():
    deck = get_deck()
    rows = [[],[],[],[]]
    for r in rows:
        r.append(deck.pop())
    return [rows, deck]

def print_state(rows, deck):
    for r in rows:
        print(r)

def get_players_input(num_players, players_cards):
    cards_played = []
    for i in range(0, num_players):
        print("Jugador", i+1, "¿Qué harás?")
        print(players_cards[i])
        print("[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")
        player_input = ""
        is_valid_input = False
        index = 0
        while(not is_valid_input):
            player_input = input()
            if(player_input.isdigit()):
                index = int(player_input)
                if(index>=len(players_cards[i])):
                    print("Invalid selection, please enter a number between 0 and", len(players_cards[i])-1)
                else:
                    is_valid_input = True
            else:
                print("Please enter a number between 0 and", len(players_cards[i])-1)
        
        print("Selección:", players_cards[i][index])
        cards_played.append(players_cards[i].pop(index))
    return cards_played

def get_players_cards(deck, num_players):
    players_cards = []
    for i in range(0, num_players):
        players_cards.append([deck.pop()])
    for i in range(1, 10):
        for j in range (0, num_players):
            players_cards[j].append(deck.pop())
    return players_cards

def process_turn(rows, players_selections):
    # order players cards keeping track of the owner
    # add them to the stacks
    # for card in range(len(players_selections)):
    for card in players_selections:
        shortest_distance = 104
        closest_row = -1
        for i in range(4):
            distance = card-rows[i][-1]
            # print("last card of row", i, "is", rows[i][-1])     # This seems to work just fine
            if(distance > 0):   # la carta es mayor al último elemento de esa fila
                # print("the card of the player,", card, "could go here, 'cause is higher")
                if(distance < shortest_distance):
                    # print("The distance is:", distance)
                    closest_row = i
                    shortest_distance = distance
        if (closest_row==-1):   # la última carta de todas las filas es mayor a la carta jugada
            print("No se pudo encontrar una fila para la carta :'c")
            pass                # por ahora dejar así. Debería perder puntos ese jugador y se reinicia la fila
        else:                   # se encontró dónde poner la carta
            rows[closest_row].append(card)  # agregarla a la fila y se termina el ciclo, seguir con el siguiente jugador

    return

rows, deck = start_game()
running = True
num_players = 3
players_cards = get_players_cards(deck, num_players)


for turn in range(0,10):
    print("Turn #", turn+1)
    print_state(rows, deck)
    players_selections = get_players_input(num_players, players_cards)
    process_turn(rows, players_selections)

print_state(rows, deck)