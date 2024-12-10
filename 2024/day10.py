from inputs import  input_day10
rows = [row for row in input_day10.strip().split("\n")]
grid = []
for row in rows:
    new_row = []
    for char in row:
        new_row.append(int(char))
    grid.append(new_row)

def finding_zero(num,grid):
    coordinates = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if int(grid[row][col]) == num:
                coordinates.append((int(row),int(col)))
    return coordinates

def next_values(coord, grid, current_height):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    next_ = []
    for dir_row, dir_col in directions:
        new_row, new_column = (coord[0]+dir_row, coord[1]+dir_col)
        if 0 <= new_row < len(grid) and 0 <= new_column < len(grid[0]):
            new_value = int(grid[new_row][new_column])
            if new_value == current_height+1:
                next_.append((new_row, new_column))
    return next_

def calculate_score(zero, grid):
    stack = [(zero, 0)]
    visited = set()
    score = 0
    while stack:
        (row, col), current_height = stack.pop()
        if (row, col) in visited:
            continue
        visited.add((row, col))
        if current_height == 9:
            score += 1
            continue
        for neighbor in next_values((row, col), grid, current_height):
            stack.append((neighbor, current_height + 1))
    return score

zeros = finding_zero(0,grid)
total_score = 0
for zero in zeros:
    score = calculate_score(zero, grid)
    total_score += score
print(total_score)

