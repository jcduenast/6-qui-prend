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

def get_players_input(num_players, players_cards, players_point_cards):
    cards_played = []
    for i in range(0, num_players):
        print("Jugador", i+1, "¿Qué harás?")
        print(players_cards[i])
        print("[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")
        print("Cartas de puntos:", players_point_cards[i])
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
    players_point_cards = []
    for i in range(0, num_players):
        players_cards.append([deck.pop()])
        players_point_cards.append([])
    for i in range(1, 10):
        for j in range (0, num_players):
            players_cards[j].append(deck.pop())
    for i in range(num_players):
        players_cards[i].sort()
    return players_cards, players_point_cards

def get_player_row_selection(rows, player_id):
    for row in rows:
        print(row, get_card_points(row))
    player_input = ""
    invalid_input = True
    while invalid_input:
        player_input = input()
        if player_input.isdigit():
            index = int(player_input)   # está en [0,4)
            if index >= 0 and index < 4:
                invalid_input = False
        else:
            print("Please enter a number between 0 and 3")
        pass
    return int(player_input)

def process_turn(rows, players_selections, players_point_cards):
    sorted_list_indexes = sorted(range(len(players_selections)), key=lambda k: players_selections[k])
    # add them to the stacks
    # for card in range(len(players_selections)):
    for player_id in sorted_list_indexes:   # vamos a buscarle sitio a la carta de cada jugador en orden
        shortest_distance = 104
        closest_row = -1
        for r in range(4):
            distance = players_selections[player_id] - rows[r][-1]
            if distance > 0:     # la carta es mayor y puede ir acá
                if distance < shortest_distance:    # debe ir en esta fila
                    closest_row = r                 # esta es la nueva fila más cercana
                    shortest_distance = distance    # ahora debe superar esta distancia (ser más cercano)
        if closest_row == -1:       # no se le encontró fila, hay que reiniciar una y sumar los puntos al jugador corresponidente
            print("No hay fila para la carta", players_selections[player_id], ". El jugador", player_id+1, "pierde puntos.")
            print("Jugador", player_id+1, "¿qué fila te quieres tragar?")
            selected_row = get_player_row_selection(rows, player_id)
            while len(rows[selected_row]) != 0:
                players_point_cards[player_id].append(rows[selected_row].pop())
            rows[selected_row].append(players_selections[player_id])
        else:                       # Sí se le encontró fila, hay que agregarla
            rows[closest_row].append(players_selections[player_id])  # agregarla a la fila y se termina el ciclo, seguir con el siguiente jugador
            if len(rows[closest_row]) == 6:
                print("La fila", closest_row+1, "debe ser procesada. El jugador", player_id+1, "se la come toda.")
                for i in range(5):
                    players_point_cards[player_id].append(rows[closest_row].pop(0))
    return

def get_card_points(list_of_cards):
    # # multiplos de 5 se llevan 3 puntos
    # # multiplos de 10 se llevan 5 puntos
    # # el 55 da 7 puntos
    sum = 0
    for card in list_of_cards:
        sum += 1
        if card == 55:
            sum += 6
        elif card %10 == 0:
            sum += 4
        elif card %5 == 0:
            sum += 2
    return sum



rows, deck = start_game()
running = True
num_players = 3
players_cards, players_point_cards = get_players_cards(deck, num_players)

# ## Test of points per card
# list_test = list(range(1, 105))
# for card in list_test:
#     print("Carta", card, "gives", get_card_points([card]), "points")
    

# # run the game:
for turn in range(0,10):
    print("Turn #", turn+1)
    print_state(rows, deck)
    players_selections = get_players_input(num_players, players_cards, players_point_cards)
    process_turn(rows, players_selections, players_point_cards)

print_state(rows, deck)