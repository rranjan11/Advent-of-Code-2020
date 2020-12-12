'''
Day:            10
File:           adapter_array.py
Author:         Rishabh Ranjan
Last Modified:  12/12/2020
'''

def count_differences(joltage_list):
    joltage_list.append(0)
    joltage_list.append(max(joltage_list) + 3)
    joltage_list.sort()
    num_ones = 0
    num_threes = 0
    differences = []
    for i in range(1, len(joltage_list)):
        differences.append(joltage_list[i] - joltage_list[i - 1])
        if joltage_list[i] - joltage_list[i - 1] == 1:
            num_ones += 1
        elif joltage_list[i] - joltage_list[i - 1] == 3:
            num_threes += 1
    return num_ones, num_threes, differences

def num_distinct_arrangements(differences):
    ones_start = 0
    ones_end = 0
    ones_started = False
    product = 1
    for i in range(len(differences)):
        if differences[i] == 1:
            if not ones_started:
                ones_start = i
                ones_started = True
            if i == len(differences) - 1 or differences[i + 1] == 3:
                ones_end = i + 1
                ones_started = False
                if ones_end - ones_start == 2:
                    product *= 2
                elif ones_end - ones_start == 3:
                    product *= 4
                elif ones_end - ones_start == 4:
                    product *= 7
    return product

def main():
    f = open('day_10_input.txt', 'r')
    joltage_list = list(map(int, f.read().splitlines()))
    f.close()
    num_ones, num_threes, differences = count_differences(joltage_list)
    print("Part 1 Answer: ", num_ones * num_threes)
    print("Part 2 Answer: ", num_distinct_arrangements(differences))

if __name__ == '__main__':
    main()
