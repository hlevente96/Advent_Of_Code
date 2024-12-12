from inputs import input_day12

flower_map = [row for row in input_day12.strip().split("\n")]
garden_width = len(flower_map[0])
garden_height = len(flower_map)
garden = [[[0,0] for _ in range(garden_width)] for _ in range(garden_height)]
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def creating_groups(flowers: list[list[str]], garden_map: list[list[list[int]]]) -> list[list[list[int]]]:
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

def counting_fences(flowers: list[list[str]], garden_map: list[list[list[int]]]) -> list[list[list[int]]]:
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
                else:
                    fences += 1
            garden_map[y][x][1] = fences
    return garden_map

def summing(garden_map: list[list[list[int]]]) -> int:
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
print(result)

