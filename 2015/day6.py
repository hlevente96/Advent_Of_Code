from inputs import input_day6

rows = [row for row in input_day6.strip().split("\n")]
grid = [[0 for _ in range(1000)] for _ in range(1000)]

def change_grid(r, cord_1, cord_2, lamps):
    for x in range(cord_1[0], cord_2[0]+1):
        for y in range(cord_1[1],cord_2[1]+1):
            if r == "turn on":
                lamps[x][y] += 1
            elif r == "turn off":
                if lamps[x][y] != 0:
                    lamps[x][y] -= 1
            elif r == "toggle":
                lamps[x][y] += 2
    return lamps

for row in rows:
    first_split = row.strip().split("through")
    second_split = first_split[0].strip().split(" ")
    first_coord = (int(second_split[-1].split(",")[0]), int(second_split[-1].split(",")[1]))
    second_coord = (int(first_split[1].strip().split(",")[0]),int(first_split[1].strip().split(",")[1]))
    if len(second_split) == 3:
        rule = second_split[0] + " " + second_split[1]
    else:
        rule = second_split[0]
    grid = change_grid(rule,first_coord,second_coord,grid)

total_ones = sum(sum(row) for row in grid)
print(total_ones)
