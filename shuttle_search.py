'''
Day:            13
File:           shuttle_search.py
Author:         Rishabh Ranjan
Last Modified:  12/16/2020
'''

import math

def find_earliest_bus(bus_ids, earliest_time):
    bus_times = bus_ids.copy()
    for i in range(len(bus_ids)):
        while bus_times[i] < earliest_time:
            bus_times[i] += bus_ids[i]
    return bus_ids[bus_times.index(min(bus_times))] * (min(bus_times) - earliest_time)

def timestamp_matching_list(bus_ids, bus_positions):
    current_base = 1
    current_num = 0
    for i in range(len(bus_ids)):
        while current_num % bus_ids[i] != (bus_ids[i] - bus_positions[i]) % bus_ids[i]:
            current_num += current_base
        current_base = math.lcm(current_base, bus_ids[i])
    return current_num

def main():
    f = open('day_13_input.txt', 'r')
    input = f.read().splitlines()
    f.close()
    earliest_time = int(input[0])
    bus_ids = input[1].split(',')
    bus_positions = []
    for i in range(len(bus_ids)):
        if bus_ids[i].isnumeric():
            bus_positions.append(i)
    while 'x' in bus_ids:
        bus_ids.remove('x')
    bus_ids = list(map(int, bus_ids))
    print("Part 1 Answer: ", find_earliest_bus(bus_ids, earliest_time))
    print("Part 2 Answer: ", timestamp_matching_list(bus_ids, bus_positions))

if __name__ == '__main__':
    main()
