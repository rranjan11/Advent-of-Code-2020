'''
Day:            3
File:           toboggan_trajectory.py
Author:         Rishabh Ranjan
Last Modified:  12/3/2020
'''

def count_trees(grid, right, down):
    num_trees = 0
    curr_pos = 0
    for i in range(0, len(grid), down):
        if grid[i][curr_pos] == '#':
            num_trees += 1
        curr_pos = (curr_pos + right) % (len(grid[0]))
    return num_trees

def main():
    f = open('day_3_input.txt', 'r')
    grid = []
    for x in f:
        grid.append(x.rstrip('\n'))
    f.close()
    print("Part 1 Answer: ", count_trees(grid, 3, 1))
    print("Part 2 Answer: ", count_trees(grid, 1, 1)*count_trees(grid, 3, 1)*count_trees(grid, 5, 1)*count_trees(grid, 7, 1)*count_trees(grid, 1, 2))

if __name__ == '__main__':
    main()
