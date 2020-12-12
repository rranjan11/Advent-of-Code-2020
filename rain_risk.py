'''
Day:            12
File:           rain_risk.py
Author:         Rishabh Ranjan
Last Modified:  12/12/2020
'''

def navigate_old(instructions):
    x_pos = 0
    y_pos = 0
    angle = 0
    for line in instructions:
        action = line[0]
        value = int(line[1:])
        if action == 'N':
            y_pos += value
        elif action == 'S':
            y_pos -= value
        elif action == 'E':
            x_pos += value
        elif action == 'W':
            x_pos -= value
        elif action == 'L':
            angle = (angle + value) % 360
        elif action == 'R':
            angle = (angle - value) % 360
        elif action == 'F':
            if angle == 0:
                x_pos += value
            elif angle == 90:
                y_pos += value
            elif angle == 180:
                x_pos -= value
            elif angle == 270:
                y_pos -= value
    return abs(x_pos) + abs(y_pos)

def navigate_new(instructions):
    x_pos = 0
    y_pos = 0
    waypoint_x = 10
    waypoint_y = 1
    for line in instructions:
        action = line[0]
        value = int(line[1:])
        if action == 'N':
            waypoint_y += value
        elif action == 'S':
            waypoint_y -= value
        elif action == 'E':
            waypoint_x += value
        elif action == 'W':
            waypoint_x -= value
        elif action == 'L':
            if value == 90:
                temp_y = waypoint_y
                waypoint_y = waypoint_x
                waypoint_x = -temp_y
            elif value == 180:
                waypoint_x = -waypoint_x
                waypoint_y = -waypoint_y
            elif value == 270:
                temp_x = waypoint_x
                waypoint_x = waypoint_y
                waypoint_y = -temp_x
        elif action == 'R':
            if value == 90:
                temp_x = waypoint_x
                waypoint_x = waypoint_y
                waypoint_y = -temp_x
            elif value == 180:
                waypoint_x = -waypoint_x
                waypoint_y = -waypoint_y
            elif value == 270:
                temp_y = waypoint_y
                waypoint_y = waypoint_x
                waypoint_x = -temp_y
        elif action == 'F':
            x_pos += (value * waypoint_x)
            y_pos += (value * waypoint_y)
    return abs(x_pos) + abs(y_pos)

def main():
    f = open('day_12_input.txt', 'r')
    instructions = f.read().splitlines()
    f.close()
    print("Part 1 Answer: ", navigate_old(instructions))
    print("Part 2 Answer: ", navigate_new(instructions))

if __name__ == '__main__':
    main()
