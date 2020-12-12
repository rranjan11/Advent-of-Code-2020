'''
Day:            11
File:           seating_system.py
Author:         Rishabh Ranjan
Last Modified:  12/12/2020
'''

def simulate_seating_old(layout):
    while True:
        layout_copy = layout.copy()
        for i in range(len(layout)):
            for j in range(len(layout[0])):
                adjacent_seats_occupied = 0
                if i - 1 >= 0 and layout[i - 1][j] == '#':
                    adjacent_seats_occupied += 1
                if i - 1 >= 0 and j + 1 < len(layout[0]) and layout[i - 1][j + 1] == '#':
                    adjacent_seats_occupied += 1
                if j + 1 < len(layout[0]) and layout[i][j + 1] == '#':
                    adjacent_seats_occupied += 1
                if i + 1 < len(layout) and j + 1 < len(layout[0]) and layout[i + 1][j + 1] == '#':
                    adjacent_seats_occupied += 1
                if i + 1 < len(layout) and layout[i + 1][j] == '#':
                    adjacent_seats_occupied += 1
                if i + 1 < len(layout) and j - 1 >= 0 and layout[i + 1][j - 1] == '#':
                    adjacent_seats_occupied += 1
                if j - 1 >= 0 and layout[i][j - 1] == '#':
                    adjacent_seats_occupied += 1
                if i - 1 >= 0 and j - 1 >= 0 and layout[i - 1][j - 1] == '#':
                    adjacent_seats_occupied += 1
                if layout[i][j] == 'L' and adjacent_seats_occupied == 0:
                    layout_copy[i] = layout_copy[i][:j] + '#' + layout_copy[i][j + 1:]
                elif layout[i][j] == '#' and adjacent_seats_occupied >= 4:
                    layout_copy[i] = layout_copy[i][:j] + 'L' + layout_copy[i][j + 1:]
        if layout_copy == layout:
            return layout
        layout = layout_copy.copy()

def simulate_seating_new(layout):
    while True:
        layout_copy = layout.copy()
        for i in range(len(layout)):
            for j in range(len(layout[0])):
                adjacent_seats_occupied = 0
                seat_seen = False
                for k in range(1, i + 1):
                    if seat_seen:
                        break
                    if layout[i - k][j] == 'L':
                        seat_seen = True
                    elif layout[i - k][j] == '#':
                        seat_seen = True
                        adjacent_seats_occupied += 1
                seat_seen = False
                for k in range(1, min(i + 1, len(layout[0]) - j)):
                    if seat_seen:
                        break
                    if layout[i - k][j + k] == 'L':
                        seat_seen = True
                    elif layout[i - k][j + k] == '#':
                        seat_seen = True
                        adjacent_seats_occupied += 1
                seat_seen = False
                for k in range(1, len(layout[0]) - j):
                    if seat_seen:
                        break
                    if layout[i][j + k] == 'L':
                        seat_seen = True
                    elif layout[i][j + k] == '#':
                        seat_seen = True
                        adjacent_seats_occupied += 1
                seat_seen = False
                for k in range(1, min(len(layout) - i, len(layout[0]) - j)):
                    if seat_seen:
                        break
                    if layout[i + k][j + k] == 'L':
                        seat_seen = True
                    elif layout[i + k][j + k] == '#':
                        seat_seen = True
                        adjacent_seats_occupied += 1
                seat_seen = False
                for k in range(1, len(layout) - i):
                    if seat_seen:
                        break
                    if layout[i + k][j] == 'L':
                        seat_seen = True
                    elif layout[i + k][j] == '#':
                        seat_seen = True
                        adjacent_seats_occupied += 1
                seat_seen = False
                for k in range(1, min(len(layout) - i, j + 1)):
                    if seat_seen:
                        break
                    if layout[i + k][j - k] == 'L':
                        seat_seen = True
                    elif layout[i + k][j - k] == '#':
                        seat_seen = True
                        adjacent_seats_occupied += 1
                seat_seen = False
                for k in range(1, j + 1):
                    if seat_seen:
                        break
                    if layout[i][j - k] == 'L':
                        seat_seen = True
                    elif layout[i][j - k] == '#':
                        seat_seen = True
                        adjacent_seats_occupied += 1
                seat_seen = False
                for k in range(1, min(i + 1, j + 1)):
                    if seat_seen:
                        break
                    if layout[i - k][j - k] == 'L':
                        seat_seen = True
                    elif layout[i - k][j - k] == '#':
                        seat_seen = True
                        adjacent_seats_occupied += 1
                if layout[i][j] == 'L' and adjacent_seats_occupied == 0:
                    layout_copy[i] = layout_copy[i][:j] + '#' + layout_copy[i][j + 1:]
                elif layout[i][j] == '#' and adjacent_seats_occupied >= 5:
                    layout_copy[i] = layout_copy[i][:j] + 'L' + layout_copy[i][j + 1:]
        if layout_copy == layout:
            return layout
        layout = layout_copy.copy()

def main():
    f = open('day_11_input.txt', 'r')
    layout = f.read().splitlines()
    f.close()
    layout_old = simulate_seating_old(layout)
    count = 0
    for row in layout_old:
        for seat in row:
            if seat == '#':
                count += 1
    print("Part 1 Answer: ", count)
    layout_new = simulate_seating_new(layout)
    count = 0
    for row in layout_new:
        for seat in row:
            if seat == '#':
                count += 1
    print("Part 2 Answer: ", count)

if __name__ == '__main__':
    main()
