'''
Day:            15
File:           rambunctious_recitation.py
Author:         Rishabh Ranjan
Last Modified:  12/16/2020
'''

def memory_game(starting_nums, final_turn):
    turns = {}
    for i in range(len(starting_nums)):
        turns[starting_nums[i]] = i + 1
    previous_num = starting_nums[len(starting_nums) - 1]
    previous_num_turn = turns[previous_num]
    unique = True
    current_num = 0
    for i in range(len(starting_nums) + 1, final_turn + 1):
        current_num = 0
        if not unique:
            current_num = i - 1 - previous_num_turn
        if current_num in turns:
            unique = False
            previous_num_turn = turns[current_num]
        else:
            unique = True
        turns[current_num] = i
        previous_num = current_num
    return current_num

def main():
    f = open('day_15_input.txt', 'r')
    starting_nums = list(map(int, f.read().split(',')))
    f.close()
    print("Part 1 Answer: ", memory_game(starting_nums, 2020))
    print("Part 2 Answer: ", memory_game(starting_nums, 30000000))

if __name__ == '__main__':
    main()
