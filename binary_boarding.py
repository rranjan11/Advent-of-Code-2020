'''
Day:            5
File:           binary_boarding.py
Author:         Rishabh Ranjan
Last Modified:  12/6/2020
'''

def find_seat_id(boarding_passes):
    max = 0
    id_list = []
    for boarding_pass in boarding_passes:
        id = int("0b" + boarding_pass.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2)
        id_list.append(id)
        if id > max:
            max = id
    id_list.sort()
    my_id = None
    next_id = id_list[0]
    for id in id_list:
        if id != next_id:
            my_id = next_id
            break
        next_id = id + 1
    return max, my_id

def main():
    f = open('day_5_input.txt', 'r')
    boarding_passes = f.read().splitlines()
    f.close()
    max_id, my_id = find_seat_id(boarding_passes)
    print("Part 1 Answer: ", max_id)
    print("Part 2 Answer: ", my_id)

if __name__ == '__main__':
    main()
