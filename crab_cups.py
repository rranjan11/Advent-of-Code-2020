# WIP

'''
Day:            23
File:           crab_cups.py
Author:         Rishabh Ranjan
Last Modified:  12/25/2020
'''

def move_cups(cups, current_cup):
    # print(cups)
    cups_to_move = []
    for j in range(3):
        cups_to_move.append(cups.pop((cups.index(current_cup) + 1) % len(cups)))
    # print(cups_to_move)
    destination_cup = current_cup - 1 if current_cup > 1 else len(cups) + len(cups_to_move)
    while destination_cup in cups_to_move:
        destination_cup = destination_cup - 1 if destination_cup > 1 else len(cups) + len(cups_to_move)
    for cup in cups_to_move:
        cups.insert(cups.index(destination_cup) + 1, cup)
        destination_cup = cup
    return cups, cups[(cups.index(current_cup) + 1) % len(cups)]

def main():
    f = open('day_23_input.txt', 'r')
    cups = list(map(int, list(f.read())[:-1]))
    f.close()
    cups_2 = cups.copy()
    current_cup = cups[0]
    for i in range(100):
        cups, current_cup = move_cups(cups, current_cup)
    print(cups)
    for i in range(10, 1000001):
        cups_2.append(i)
    current_cup = cups_2[0]
    # print(cups_2)
    for i in range(10000000):
        if i % 1000 == 0:
            print(i)
        cups_2, current_cup = move_cups(cups_2, current_cup)
    print(cups_2[(cups_2.index(1) + 1) % len(cups_2)] * cups_2[(cups_2.index(1) + 2) % len(cups_2)])

if __name__ == '__main__':
    main()
