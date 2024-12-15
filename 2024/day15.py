from inputs import input_day15_map, input_day15_inst

def initialize_map(input_data):
    map_str = [row for row in input_data.strip().split("\n")]
    map_ = []
    for row in map_str:
        new_row = []
        for char in row:
            new_row.append(char)
        map_.append(new_row)
    map_width = len(map_[0])
    map_height = len(map_)
    return map_width, map_height, map_, map_str

def initialize_robot(height, width, map_):
    robot = ()
    for y in range(height):
        for x in range(width):
            if map_[y][x] == "@":
                robot = (x,y)
    return robot

def instructions_list(input_data):
    input_inst = [row for row in input_data.strip().split("\n")]
    instructions = ""
    for row in input_inst:
        instructions += row
    return instructions

def direction_selector(instruction):
    dir = (0, 0)
    if instruction == ">":
        dir = (1, 0)
    elif instruction == "v":
        dir = (0, 1)
    elif instruction == "<":
        dir = (-1, 0)
    elif instruction == "^":
        dir = (0, -1)
    return dir

def find_boxes(map_, map_height, map_width, str):
    boxes = []
    for y in range(map_height):
        for x in range(map_width):
            if map_[y][x] == str:
                boxes.append((x,y))
    return boxes

def count_values(boxes):
    count_number=0
    for box in boxes:
        x,y = box
        count_number += y*100 + x
    return count_number

def second_map(map_str):
    map_ = []
    for row in map_str:
        new_row = []
        for char in row:
            if char == ".":
                new_row.append(char)
                new_row.append(char)
            elif char == "#":
                new_row.append(char)
                new_row.append(char)
            elif char == "O":
                new_row.append("[")
                new_row.append("]")
            elif char == "@":
                new_row.append("@")
                new_row.append(".")
        map_.append(new_row)
    return map_

def next_level(nx, ny, dy, char):
    if char == "[":
        if map_[ny+dy][nx] == "#" or map_[ny+dy][nx + 1] == "#":
            return "#"
    elif char == "]":
        if map_[ny+dy][nx] == "#" or map_[ny+dy][nx - 1] == "#":
            return "#"
    pack = []
    for i in [nx, nx + 1, nx-1]:
        if map_[ny+dy][i] == char:
            pack.append((i,ny + dy))
    return pack

map_width, map_height, map_, map_str = initialize_map(input_day15_map)
hero = initialize_robot(map_height, map_width, map_)
instructions = instructions_list(input_day15_inst)

#### Part 1 - Main Loop ####
for inst in instructions:
    direction = direction_selector(inst)
    x,y = hero
    dx, dy = direction
    neighbour = map_[y+dy][x+dx]
    if neighbour == "#":
        continue
    elif neighbour == ".":
        hero = (x+dx, y+dy)
        map_[y+dy][x+dx] = "@"
        map_[y][x] = "."
    elif neighbour == "O":
        for i in range(50):
            next_neighbour_x = x+(i*dx)
            next_neighbour_y = y+(i*dy)
            char_neighbour = map_[next_neighbour_y][next_neighbour_x]
            if char_neighbour == "#":
                break
            elif char_neighbour == ".":
                hero = (x + dx, y + dy)
                map_[next_neighbour_y][next_neighbour_x] = "O"
                map_[y+dy][x+dx] = "@"
                map_[y][x] = "."
                break

boxes = find_boxes(map_, map_height, map_width, "O")
count = count_values(boxes)
print("Final map of Part-1:")
for i in range(map_height):
    print(map_[i])
print(f"Final solution for part 1: {count}")


map_ = second_map(map_str)
map_width = len(map_[0])
map_height = len(map_)
hero = initialize_robot(map_height, map_width, map_)

#### Part 2 - Main Loop ####
for inst in instructions:
    direction = direction_selector(inst)
    x,y = hero
    dx, dy = direction
    neighbour = map_[y+dy][x+dx]
    if neighbour == "#":
        continue
    elif neighbour == ".":
        hero = (x+dx, y+dy)
        map_[y+dy][x+dx] = "@"
        map_[y][x] = "."
    elif neighbour in ["]","["] and dx !=0: # Horizontal movement
        for i in range(50):
            next_neighbour_x = x+(i*dx)
            prev_neighbour_x = x+((i-1)*dx)
            char_neighbour = map_[y][next_neighbour_x]
            if char_neighbour == "#":
                break
            elif char_neighbour == ".":
                hero = (x + dx, y)
                map_[y][x + dx] = "@"
                map_[y][x] = "."
                distance = abs(x-next_neighbour_x)+1
                for i in range(2,distance):
                    new_x = x + dx*i
                    if dx > 0:
                        if i % 2 == 0:
                            map_[y][new_x] = "["
                        else:
                            map_[y][new_x] = "]"
                    elif dx < 0:
                        if i % 2 == 0:
                            map_[y][new_x] = "]"
                        else:
                            map_[y][new_x] = "["
                break
    elif neighbour in ["]", "["] and dy != 0: # Vertical movement
        if neighbour == "[":
            pack = [(x,y+dy)]
            stack = [(x,y+dy)]
            n_level_pack = ""
            while stack:
                x, y = stack.pop()
                n_level_pack = next_level(x, y, dy, "[")
                if n_level_pack == "#":
                    break
                else:
                    for char in n_level_pack:
                        stack.append(char)
                        pack.append(char)
            if n_level_pack == "#":
                continue
            if dy < 0 :
                pack = sorted(pack, key=lambda coord: coord[1])
            else:
                pack = sorted(pack, key=lambda coord: coord[1], reverse=True)
            for box in pack:
                lbx, lby = box
                map_[lby][lbx] = "."
                map_[lby][lbx + 1] = "."
                map_[lby+dy][lbx] = "["
                map_[lby+dy][lbx+1] = "]"
            x, y = hero
            map_[y+dy][x] = "@"
            hero = (x, y + dy)
            map_[y + dy][x + 1] = "."
            map_[y][x] = "."
        elif neighbour == "]":
            pack = [(x,y+dy)]
            stack = [(x,y+dy)]
            n_level_pack = ""
            while stack:
                x, y = stack.pop()
                n_level_pack = next_level(x, y, dy, "]")
                if n_level_pack == "#":
                    break
                else:
                    for char in n_level_pack:
                        stack.append(char)
                        pack.append(char)
            if n_level_pack == "#":
                continue
            if dy < 0:
                pack = sorted(pack, key=lambda coord: coord[1])
            else:
                pack = sorted(pack, key=lambda coord: coord[1], reverse=True)
            for box in pack:
                lbx, lby = box
                map_[lby][lbx] = "."
                map_[lby][lbx - 1] = "."
                map_[lby+dy][lbx] = "]"
                map_[lby+dy][lbx-1] = "["
            x, y = hero
            map_[y+dy][x] = "@"
            hero = (x, y + dy)
            map_[y + dy][x - 1] = "."
            map_[y][x] = "."

boxes = find_boxes(map_, map_height, map_width, "[")
count = count_values(boxes)

print("Final map of Part-2:")
for i in range(map_height):
    print(map_[i])
print(f"Final solution for part 2: {count}")

