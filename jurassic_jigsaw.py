'''
Day:            20
File:           jurassic_jigsaw.py
Author:         Rishabh Ranjan
Last Modified:  12/25/2020
'''

def find_corners(edges, unique_edges, corners):
    product = 1
    for id in edges:
        num_uniques_edges = 0
        top_edge_unique = True
        right_edge_unique = True
        bottom_edge_unique = True
        left_edge_unique = True
        for tile_id in edges:
            if id != tile_id:
                for edge in edges[tile_id]:
                    if edges[id][0] == edge or edges[id][0] == edge[::-1]:
                        top_edge_unique = False
                    if edges[id][1] == edge or edges[id][1] == edge[::-1]:
                        right_edge_unique = False
                    if edges[id][2] == edge or edges[id][2] == edge[::-1]:
                        bottom_edge_unique = False
                    if edges[id][3] == edge or edges[id][3] == edge[::-1]:
                        left_edge_unique = False
        if top_edge_unique:
            num_uniques_edges += 1
            if id in unique_edges:
                unique_edges[id].append(0)
            else:
                unique_edges[id] = [0]
        if right_edge_unique:
            num_uniques_edges += 1
            if id in unique_edges:
                unique_edges[id].append(1)
            else:
                unique_edges[id] = [1]
        if bottom_edge_unique:
            num_uniques_edges += 1
            if id in unique_edges:
                unique_edges[id].append(2)
            else:
                unique_edges[id] = [2]
        if left_edge_unique:
             num_uniques_edges += 1
             if id in unique_edges:
                 unique_edges[id].append(3)
             else:
                 unique_edges[id] = [3]
        if num_uniques_edges == 2:
            product *= id
            corners.add(id)
    return edges, unique_edges, corners, product

def rotate_90_degrees(image):
    new_image = image.copy()
    for i in range(len(image[0])):
        for j in range(len(image)):
            new_image[i] = new_image[i][:j] + image[j][len(image) - 1 - i] + new_image[i][j + 1:]
    return new_image

def flip(image):
    new_image = image.copy()
    for i in range(len(image)):
        new_image[i] = image[i][::-1]
    return new_image

def insert_in_image(image, image_to_insert, row, col):
    for i in range(len(image_to_insert)):
        image[row + i] = image[row + i][:col] + image_to_insert[i] + image[row + i][col + len(image_to_insert[i]):]
    return image

def get_edges(tile):
    left_edge = ""
    right_edge = ""
    for i in range(len(tile)):
        left_edge += tile[i][0]
        right_edge += tile[i][9]
    return (tile[0], right_edge, tile[9][::-1], left_edge[::-1])

def match_to_right(image, current_tile_id, current_tile, current_tile_with_edges, current_tile_pos, edges, tiles, tiles_with_edges):
    current_tile_edges = get_edges(current_tile_with_edges)
    matching_tile_id = 0
    for id in edges:
        if id != current_tile_id:
            if edges[id][0] == current_tile_edges[1] or edges[id][0] == current_tile_edges[1][::-1]:
                matching_tile_id = id
                break
            if edges[id][1] == current_tile_edges[1] or edges[id][1] == current_tile_edges[1][::-1]:
                matching_tile_id = id
                break
            if edges[id][2] == current_tile_edges[1] or edges[id][2] == current_tile_edges[1][::-1]:
                matching_tile_id = id
                break
            if edges[id][3] == current_tile_edges[1] or edges[id][3] == current_tile_edges[1][::-1]:
                matching_tile_id = id
                break
    matching_tile = tiles[matching_tile_id]
    matching_tile_with_edges = tiles_with_edges[matching_tile_id]
    matching_tile_edges = get_edges(matching_tile_with_edges)
    num = 0
    while current_tile_edges[1] != matching_tile_edges[3][::-1]:
        if num == 3:
            matching_tile = flip(matching_tile)
            matching_tile_with_edges = flip(matching_tile_with_edges)
        else:
            matching_tile = rotate_90_degrees(matching_tile)
            matching_tile_with_edges = rotate_90_degrees(matching_tile_with_edges)
        matching_tile_edges = get_edges(matching_tile_with_edges)
        num += 1
    image = insert_in_image(image, matching_tile, current_tile_pos[0], current_tile_pos[1] + 8)
    current_tile_id = matching_tile_id
    current_tile = matching_tile
    current_tile_with_edges = matching_tile_with_edges
    current_tile_pos = (current_tile_pos[0], current_tile_pos[1] + 8)
    return image, current_tile_id, current_tile, current_tile_with_edges, current_tile_pos

def match_to_bottom(image, current_tile_id, current_tile, current_tile_with_edges, current_tile_pos, edges, tiles, tiles_with_edges):
    current_tile_edges = get_edges(current_tile_with_edges)
    matching_tile_id = 0
    for id in edges:
        if id != current_tile_id:
            if edges[id][0] == current_tile_edges[2] or edges[id][0] == current_tile_edges[2][::-1]:
                matching_tile_id = id
                break
            if edges[id][1] == current_tile_edges[2] or edges[id][1] == current_tile_edges[2][::-1]:
                matching_tile_id = id
                break
            if edges[id][2] == current_tile_edges[2] or edges[id][2] == current_tile_edges[2][::-1]:
                matching_tile_id = id
                break
            if edges[id][3] == current_tile_edges[2] or edges[id][3] == current_tile_edges[2][::-1]:
                matching_tile_id = id
                break
    matching_tile = tiles[matching_tile_id]
    matching_tile_with_edges = tiles_with_edges[matching_tile_id]
    matching_tile_edges = get_edges(matching_tile_with_edges)
    num = 0
    while current_tile_edges[2] != matching_tile_edges[0][::-1]:
        if num == 3:
            matching_tile = flip(matching_tile)
            matching_tile_with_edges = flip(matching_tile_with_edges)
        else:
            matching_tile = rotate_90_degrees(matching_tile)
            matching_tile_with_edges = rotate_90_degrees(matching_tile_with_edges)
        matching_tile_edges = get_edges(matching_tile_with_edges)
        num += 1
    image = insert_in_image(image, matching_tile, current_tile_pos[0] + 8, current_tile_pos[1])
    current_tile_id = matching_tile_id
    current_tile = matching_tile
    current_tile_with_edges = matching_tile_with_edges
    current_tile_pos = (current_tile_pos[0] + 8, current_tile_pos[1])
    return image, current_tile_id, current_tile, current_tile_with_edges, current_tile_pos

def count_sea_monsters(image, sea_monster):
    count = 0
    for i in range(len(image) - len(sea_monster) + 1):
        for j in range(len(image[0]) - len(sea_monster[0]) + 1):
            sea_monster_present = True
            for k in range(len(sea_monster)):
                for l in range(len(sea_monster[0])):
                    if sea_monster[k][l] == '#' and image[i + k][j + l] != '#':
                        sea_monster_present = False
            if sea_monster_present:
                count += 1
    return count

def main():
    f = open('day_20_input.txt', 'r')
    input = f.read().splitlines()
    f.close()
    edges = {}
    tiles = {}
    tiles_with_edges = {}
    unique_edges = {}
    corners = set()
    for i in range(len(input)):
        if input[i].startswith("Tile"):
            left_edge = ""
            right_edge = ""
            for j in range(1, 11):
                left_edge += input[i + j][0]
                right_edge += input[i + j][9]
            edges[int(input[i][5:9])] = (input[i + 1], right_edge, input[i + 10][::-1], left_edge[::-1])
            tiles[int(input[i][5:9])] = [input[i + j][1:9] for j in range(2, 10)]
            tiles_with_edges[int(input[i][5:9])] = [input[i + j] for j in range(1, 11)]
    edges, unique_edges, corners, product = find_corners(edges, unique_edges, corners)
    print("Part 1 Answer: ", product)
    corner_id = next(iter(corners))
    corner = tiles[corner_id]
    corner_with_edges = tiles_with_edges[corner_id]
    if 0 in unique_edges[corner_id] and 1 in unique_edges[corner_id]:
        corner = rotate_90_degrees(corner)
        corner_with_edges = rotate_90_degrees(corner_with_edges)
    elif 1 in unique_edges[corner_id] and 2 in unique_edges[corner_id]:
        corner  = rotate_90_degrees(corner)
        corner  = rotate_90_degrees(corner)
        corner_with_edges = rotate_90_degrees(corner_with_edges)
        corner_with_edges = rotate_90_degrees(corner_with_edges)
    elif 2 in unique_edges[corner_id] and 3 in unique_edges[corner_id]:
        corner  = rotate_90_degrees(corner)
        corner  = rotate_90_degrees(corner)
        corner  = rotate_90_degrees(corner)
        corner_with_edges = rotate_90_degrees(corner_with_edges)
        corner_with_edges = rotate_90_degrees(corner_with_edges)
        corner_with_edges = rotate_90_degrees(corner_with_edges)
    image_line = ""
    for i in range(12):
        image_line += "........"
    image = [image_line for i in range(96)]
    image = insert_in_image(image, corner, 0, 0)
    current_tile_id = corner_id
    current_tile = corner
    current_tile_with_edges = corner_with_edges
    current_tile_pos = (0, 0)
    for i in range(12):
        leftmost_current_tile_id = current_tile_id
        leftmost_current_tile = current_tile
        leftmost_current_tile_with_edges = current_tile_with_edges
        leftmost_current_tile_pos = current_tile_pos
        for j in range(11):
            image, current_tile_id, current_tile, current_tile_with_edges, current_tile_pos = match_to_right(image,
                current_tile_id, current_tile, current_tile_with_edges, current_tile_pos, edges, tiles, tiles_with_edges)
        if i == 11:
            break
        image, current_tile_id, current_tile, current_tile_with_edges, current_tile_pos = match_to_bottom(image,
            leftmost_current_tile_id, leftmost_current_tile, leftmost_current_tile_with_edges, leftmost_current_tile_pos, edges, tiles, tiles_with_edges)
    sea_monster = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]
    sea_monster_count = count_sea_monsters(image, sea_monster)
    num = 0
    while sea_monster_count <= 0:
        if num == 3:
            image = flip(image)
        else:
            image = rotate_90_degrees(image)
        sea_monster_count = count_sea_monsters(image, sea_monster)
        num += 1
    hashtag_count = 0
    for line in image:
        for item in line:
            if item == '#':
                hashtag_count += 1
    print("Part 2 Answer: ", hashtag_count - sea_monster_count * 15)

if __name__ == '__main__':
    main()
