'''
Day:            17
File:           conway_cubes.py
Author:         Rishabh Ranjan
Last Modified:  12/17/2020
'''

import copy

class Cube:
    neighbors = {}
    def __init__(self, coordinates, active):
        self.coordinates = coordinates
        self.active = active

    def populate_neighbors(self, cubes, expand):
        for i in range(self.coordinates[0] - 1, self.coordinates[0] + 2):
            for j in range(self.coordinates[1] - 1, self.coordinates[1] + 2):
                for k in range(self.coordinates[2] - 1, self.coordinates[2] + 2):
                    if len(self.coordinates) == 3:
                        if (expand or (not expand and (i, j, k) in cubes)) and (i, j, k) != self.coordinates:
                            if self.coordinates in Cube.neighbors:
                                Cube.neighbors[self.coordinates].add((i, j , k))
                            else:
                                Cube.neighbors[self.coordinates] = {(i, j, k)}
                    elif len(self.coordinates) == 4:
                        for l in range(self.coordinates[3] - 1, self.coordinates[3] + 2):
                            if (expand or (not expand and (i, j, k, l) in cubes)) and (i, j, k, l) != self.coordinates:
                                if self.coordinates in Cube.neighbors:
                                    Cube.neighbors[self.coordinates].add((i, j , k, l))
                                else:
                                    Cube.neighbors[self.coordinates] = {(i, j, k, l)}

def simulate_cubes(cubes):
    for cube in cubes.values():
        cube.populate_neighbors(cubes, True)
    for neighbor_list in Cube.neighbors.values():
        for coordinates in neighbor_list:
            if not coordinates in cubes:
                cubes[coordinates] = Cube(coordinates, False)
    for cube in cubes.values():
        cube.populate_neighbors(cubes, False)
    cubes_copy = copy.deepcopy(cubes)
    for cube in cubes.values():
        num_active_neighbors = 0
        for neighbor_coordinates in Cube.neighbors[cube.coordinates]:
            if cubes_copy[neighbor_coordinates].active:
                num_active_neighbors += 1
        if cube.active and num_active_neighbors != 2 and num_active_neighbors != 3:
            cube.active = False
        elif not cube.active and num_active_neighbors == 3:
            cube.active = True
    return cubes

def main():
    f = open('day_17_input.txt', 'r')
    initial_state = f.read().splitlines()
    f.close()
    cubes = {}
    for i in range(len(initial_state)):
        for j in range(len(initial_state[0])):
            cubes[(i, j, 0)] = Cube((i, j, 0), True if initial_state[i][j] == '#' else False)
    for i in range(6):
        cubes = simulate_cubes(cubes)
    count = 0
    for cube in cubes.values():
        if cube.active:
            count += 1
    print("Part 1 Answer: ", count)
    cubes = {}
    Cube.neighbors = {}
    for i in range(len(initial_state)):
        for j in range(len(initial_state[0])):
            cubes[(i, j, 0, 0)] = Cube((i, j, 0, 0), True if initial_state[i][j] == '#' else False)
    for i in range(6):
        cubes = simulate_cubes(cubes)
    count = 0
    for cube in cubes.values():
        if cube.active:
            count += 1
    print("Part 2 Answer: ", count)

if __name__ == '__main__':
    main()
