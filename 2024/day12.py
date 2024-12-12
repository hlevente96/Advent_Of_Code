from inputs import input_day12

flower_map = [row for row in input_day12.strip().split("\n")]
garden_width = len(flower_map[0])
garden_height = len(flower_map)
garden = [[[0,0,[]] for _ in range(garden_width)] for _ in range(garden_height)]
DIRECTIONS = [(1, 0, 'K'), (0, 1, 'D'), (-1, 0, 'NY'), (0, -1, 'E')]

def creating_groups(flowers: list, garden_map: list) -> list:
    group = 0
    for y in range(garden_height):
        for x in range(garden_width):
            if garden_map[y][x][0] == 0:
                group +=1
            flower = flowers[y][x]
            stack = [(x,y)]
            while stack:
                current_x, current_y = stack.pop()
                if garden_map[current_y][current_x][0] == 0:
                    garden_map[current_y][current_x][0] = group
                    for direction in DIRECTIONS:
                        new_x, new_y = current_x + direction[0], current_y + direction[1]
                        if 0 <= new_y < garden_height and 0 <= new_x < garden_width:
                            if flowers[new_y][new_x] == flower and garden_map[new_y][new_x][0] == 0:
                                stack.append((new_x,new_y))
    return garden_map

def counting_fences(flowers: list, garden_map: list) -> list:
    for y in range(garden_height):
        for x in range(garden_width):
            fences = 0
            flower = flowers[y][x]
            for direction in DIRECTIONS:
                new_x, new_y = x + direction[0], y + direction[1]
                if 0 <= new_y < garden_height and 0 <= new_x < garden_width:
                    neighbour = flowers[new_y][new_x]
                    if neighbour != flower:
                        fences += 1
                        garden_map[y][x][2].append(direction[2])
                else:
                    fences += 1
                    garden_map[y][x][2].append(direction[2])
            garden_map[y][x][1] = fences
    return garden_map


def summing(garden_map: list) -> int:
    garden_dict = {}
    for y in range(garden_height):
        for x in range(garden_width):
            group = garden_map[y][x][0]
            fences = garden_map[y][x][1]
            if group not in garden_dict.keys():
                garden_dict[group] = {"occurrences": 0, "fences": 0}
            garden_dict[group]["occurrences"] += 1
            garden_dict[group]["fences"] += fences
    total_per_pack = [v["occurrences"] * v["fences"] for k, v in garden_dict.items()]
    total = sum(total_per_pack)
    return total

garden = creating_groups(flower_map, garden)
garden = counting_fences(flower_map, garden)
result = summing(garden)
print(f"First result: {result}")

##################################
############# PART 2 #############
##################################

def checking_number_of_cont(lst):
    count = 1
    for i in range(1, len(lst)):
        if lst[i] != lst[i - 1] + 1:
            count += 1
    return count

new_dict = {}
for y in range(garden_height):
    for x in range(garden_width):
        group = garden[y][x][0]
        fences_dir = garden[y][x][2]
        if group not in new_dict.keys():
            new_dict[group] = {"fences_at_coord": []}
        new_dict[group]["fences_at_coord"].append(((x,y),fences_dir))

total_values = []
for key, values in new_dict.items():
    fences = 0
    group_directions = {"E": [], "D": [], "K": [], "NY": []}
    for subkey, sub_values in values.items():
        for coord, directions in sub_values:
            for s in directions:
                group_directions[s].append(coord)
    for dir, val in group_directions.items():
        if dir == 'E' or dir == "D":
            groups = {}
            for x,y in val:
                if y not in groups.keys():
                    groups[y] = []
                groups[y].append(x)
            for y, x in groups.items():
                 fences += checking_number_of_cont(x)
        elif dir == 'K' or dir == 'NY':
            groups = {}
            for x, y in val:
                if x not in groups.keys():
                    groups[x] = []
                groups[x].append(y)
            for x, y in groups.items():
                fences += checking_number_of_cont(y)
    total_item_per_group = len(values['fences_at_coord'])
    total_values.append(total_item_per_group * fences)

print(f"Second result: {sum(total_values)}")

