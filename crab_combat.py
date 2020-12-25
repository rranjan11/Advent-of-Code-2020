# WIP

'''
Day:            22
File:           crab_combat.py
Author:         Rishabh Ranjan
Last Modified:  12/25/2020
'''

def combat(player_1_deck, player_2_deck):
    while True:
        player_1_card = player_1_deck.pop(0)
        player_2_card = player_2_deck.pop(0)
        if player_1_card > player_2_card:
            player_1_deck.append(player_1_card)
            player_1_deck.append(player_2_card)
        elif player_2_card > player_1_card:
            player_2_deck.append(player_2_card)
            player_2_deck.append(player_1_card)
        if not player_1_deck:
            return player_2_deck
        elif not player_2_deck:
            return player_1_deck
    return []

def recursive_combat(player_1_deck, player_2_deck):
    previous_states = set()
    while True:
        # print(previous_states)
        # print([player_1_deck, player_2_deck])
        if (tuple(player_1_deck), tuple(player_2_deck)) in previous_states:
            return 1, player_1_deck
        previous_states.add((tuple(player_1_deck), tuple(player_2_deck)))
        player_1_card = player_1_deck.pop(0)
        player_2_card = player_2_deck.pop(0)
        winner = 0
        if len(player_1_deck) >= player_1_card and len(player_2_deck) >= player_2_card:
            winner, winning_deck = recursive_combat(player_1_deck.copy(), player_2_deck.copy())
        else:
            winner = 1 if player_1_card > player_2_card else 2
        if winner == 1:
            player_1_deck.append(player_1_card)
            player_1_deck.append(player_2_card)
        elif winner == 2:
            player_2_deck.append(player_2_card)
            player_2_deck.append(player_1_card)
        if not player_1_deck:
            # print(2, player_2_card)
            return 2, player_2_deck
        elif not player_2_deck:
            # print(1, player_1_deck)
            return 1, player_1_deck
    return 0, []

def main():
    l1 = [[[3, 4], [4, 5]], [[5, 6], [6, 7]]]
    print([[3, 4], [4, 5]] in l1)
    f = open('day_22_input.txt', 'r')
    input = f.read().splitlines()
    f.close()
    parsing_player_1 = False
    parsing_player_2 = False
    player_1_deck = []
    player_2_deck = []
    for line in input:
        if line == "Player 1:":
            parsing_player_1 = True
            continue
        if line == "Player 2:":
            parsing_player_2 = True
            continue
        if line == "":
            parsing_player_1 = False
            parsing_player_2 = False
        if parsing_player_1:
            player_1_deck.append(int(line))
        elif parsing_player_2:
            player_2_deck.append(int(line))
    # winning_deck = combat(player_1_deck.copy(), player_2_deck.copy())
    # score = 0
    # for i in range(len(winning_deck)):
    #     score += (len(winning_deck) - i) * winning_deck[i]
    # print(score)
    winner, winning_deck = recursive_combat(player_1_deck, player_2_deck)
    score = 0
    for i in range(len(winning_deck)):
        score += (len(winning_deck) - i) * winning_deck[i]
    print("score:", score)


if __name__ == '__main__':
    main()
