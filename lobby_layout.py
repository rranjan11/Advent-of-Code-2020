'''
Day:            24
File:           lobby_layout.py
Author:         Rishabh Ranjan
Last Modified:  12/25/2020
'''

def flip_tiles(tiles_split):
    color = {}
    for tile in tiles_split:
        num_east = tile.count('e')
        num_west = tile.count('w')
        num_north_east = tile.count("ne")
        num_south_east = tile.count("se")
        num_north_west = tile.count("nw")
        num_south_west = tile.count("sw")
        coordinates = (num_north_east - num_south_west + num_east - num_west, num_north_west - num_south_east + num_west - num_east)
        if coordinates in color:
            color[coordinates] = 1 if color[coordinates] == 0 else 0
        else:
            color[coordinates] = 1
    return color

def simulate_day(color):
    neighbor_offsets = [(1, -1), (1, 0), (0, -1), (-1, 1), (-1, 0), (0, 1)]
    neighbors_to_add = []
    for coordinates in color:
        for neighbor_offset in neighbor_offsets:
            if tuple(map(sum, zip(coordinates, neighbor_offset))) not in color:
                neighbors_to_add.append(tuple(map(sum, zip(coordinates, neighbor_offset))))
    for neighbor in neighbors_to_add:
        color[neighbor] = 0
    color_copy = color.copy()
    for coordinates in color:
        num_black_adjacent = 0
        for neighbor_offset in neighbor_offsets:
            if tuple(map(sum, zip(coordinates, neighbor_offset))) in color and color[tuple(map(sum, zip(coordinates, neighbor_offset)))] == 1:
                num_black_adjacent += 1
        if color[coordinates] == 1 and (num_black_adjacent == 0 or num_black_adjacent > 2):
            color_copy[coordinates] = 0
        elif color[coordinates] == 0 and num_black_adjacent == 2:
            color_copy[coordinates] = 1
    return color_copy

def main():
    f = open('day_24_input.txt', 'r')
    tiles = f.read().splitlines()
    f.close()
    tiles_split = []
    for tile in tiles:
        tile_split = []
        i = 0
        while i < len(tile):
            if tile[i] == 'e' or tile[i] == 'w':
                tile_split.append(tile[i])
                i += 1
            else:
                tile_split.append(tile[i:i + 2])
                i += 2
        tiles_split.append(tile_split)
    color = flip_tiles(tiles_split)
    count = 0
    for tile_color in color.values():
        if tile_color == 1:
            count += 1
    print("Part 1 Answer: ", count)
    for i in range(100):
        color = simulate_day(color)
    count = 0
    for tile_color in color.values():
        if tile_color == 1:
            count += 1
    print("Part 2 Answer: ", count)

if __name__ == '__main__':
    main()
