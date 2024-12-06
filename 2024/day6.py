from inputs import input_day6

paths = [row for row in input_day6.strip().split("\n")]
columns = len(paths[0])
rows = len(paths)
DIRECTIONS = [(-1,0), (0,1), (1,0), (0,-1)]

def collect():
    obstacles_ = set()
    index_row_ = 0
    index_column_ = 0
    for row in range(rows):
        for column in range(columns):
            if paths[row][column] == "^":
                index_row_ = row
                index_column_ = column
            elif paths[row][column] == "#":
                obstacles_.add((row,column))
    return index_row_, index_column_, obstacles_

def first_task():
    turn = 0
    index_row, index_column, obstacles = collect()
    checked_coordinates_ = set()
    while 0 <= index_row < rows and 0 < index_column <= columns:
        direction = DIRECTIONS[turn % 4]
        while ((index_row + direction[0], index_column + direction[1]) not in obstacles
               and 0 <= index_row < rows and 0 <= index_column < columns):
            checked_coordinates_.add((index_row, index_column))
            index_row += direction[0]
            index_column += direction[1]
        turn += 1
    return checked_coordinates_, obstacles

checked_coordinates, obstacles = first_task()
print(f"Part 1 Solution: {len(checked_coordinates)}")

def detecting_loop(row_map, column_map, new_obstacles):
    turn_ = 0
    row_pos, col_pos, _ = collect()
    visited_positions = set()
    while 0 <= row_pos < row_map and 0 <= col_pos < column_map:
        direction_ = DIRECTIONS[turn_ % 4]
        while ((row_pos + direction_[0], col_pos + direction_[1]) not in new_obstacles
               and 0 <= row_pos < rows and 0 <= col_pos < columns):
            if (row_pos, col_pos,direction_) in visited_positions:
                return True
            visited_positions.add((row_pos, col_pos,direction_))
            row_pos += direction_[0]
            col_pos += direction_[1]
        turn_ += 1
    return False

count = 0
for index, coord in enumerate(checked_coordinates):
    obstacles.add(coord)
    if detecting_loop(rows, columns, obstacles):
        count += 1
    obstacles.discard(coord)

print(f"Part 2 Solution: {count}")
