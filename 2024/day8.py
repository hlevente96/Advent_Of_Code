from inputs import input_day8
from itertools import product

grid = [row for row in input_day8.strip().split("\n")]

num_rows = len(grid)
num_cols = len(grid[0])

map_ = dict()
for row in range(num_rows):
    for col in range(num_cols):
        char = grid[row][col]
        if char != ".":
            if char not in map_.keys():
                map_[char] = [(row, col)]
            else:
                map_[char].append((row, col))

count = set()
for key, value in map_.items():
    combinations = product(value, repeat = 2)
    for comb in combinations:
        first_antenna = comb[0]
        second_antenna = comb[1]
        distance_x = first_antenna[0] - second_antenna[0]
        distance_y = first_antenna[1] - second_antenna[1]
        locations = []
        for n in range(50):
            locations.append((first_antenna[0]+(n*distance_x), first_antenna[1]+(n*distance_y)))
            locations.append((first_antenna[0]-(n*distance_x), first_antenna[1]-(n*distance_y)))
        for loc in locations:
            if 0 <= loc[0] < num_rows and 0 <= loc[1] < num_cols:
                count.add(loc)

print(len(count))