from inputs import input_day12
rows = [row for row in input_day12.strip().split("\n")]

garden_width = len(rows[0])
garden_height = len(rows)

garden = [[[0,0] for _ in range(garden_width)] for _ in range(garden_height)]
GROUP = 0
directions = [(1,0),(0,1),(-1,0),(0,-1)]

def propagate_group(x, y, group, flower):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if garden[cy][cx][0] == group:
            continue
        garden[cy][cx][0] = group
        for direction in directions:
            newx, newy = cx + direction[0], cy + direction[1]
            if 0 <= newy < garden_height and 0 <= newx < garden_width:
                if rows[newy][newx] == flower and garden[newy][newx][0] == 0:
                    stack.append((newx, newy))

for y in range(garden_height):
    for x in range(garden_width):
        fences = 0
        group = 0
        flower = rows[y][x]
        for direction in directions:
            new_x = x+direction[0]
            new_y = y+direction[1]
            if 0 <= new_y < garden_height and 0 <= new_x < garden_width:
                neighbour = rows[new_y][new_x]
                if neighbour != flower:
                    fences += 1
                elif garden[new_y][new_x][0] != 0:
                    group = garden[new_y][new_x][0]
            else:
                fences += 1
        if group == 0:
            GROUP += 1
            group = GROUP
            propagate_group(x, y, group, flower)

        garden[y][x] = [group, fences]

garden_dict = {}
for y in range(len(garden)):
    for x in range(len(garden[0])):
        group = garden[y][x][0]
        fences = garden[y][x][1]
        if group not in garden_dict.keys():
            garden_dict[group] = {"occurrences": 0, "fences": 0}
        garden_dict[group]["occurrences"] += 1
        garden_dict[group]["fences"] += fences

summing = [v["occurrences"]*v["fences"] for k, v in garden_dict.items()]
total = sum(summing)
print(total)

