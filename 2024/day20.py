from collections import deque
from inputs import input_day20
from itertools import combinations

def get_start_positions(maze):
    positions = []
    start = ()
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            if maze[y][x] != "#":
                positions.append((x, y))
            if maze[y][x] == "S":
                start = (x,y)
    return start, positions

def solving_maze(maze,start):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = deque()
    queue.append((start[0],start[1],0))
    visited_pos = set()
    while queue:
        x,y,dist = queue.popleft()
        if (x,y) in visited_pos:
            continue
        visited_pos.add((x,y))
        if maze[y][x] == "E":
            maze[y][x] = dist
        for dx,dy in directions:
            nx, ny = x+dx , y+dy
            if 0<= nx < len(maze[0]) and 0<=ny <len(maze) and maze[ny][nx] != "#" and (nx,ny) not in visited_pos:
                queue.append((nx,ny,dist+1))
                maze[y][x] = dist

def solving_task(input_data):
    maze = [[char for char in row] for row in input_data.strip().split("\n")]
    start, positions = get_start_positions(maze)
    solving_maze(maze, start)
    cheats_1, cheats_2 = 0, 0
    for (x1, y1), (x2, y2) in combinations(positions, 2):
        start = int(maze[y1][x1])
        end = int(maze[y2][x2])
        original_dist = abs(end - start)
        distance = abs(x1 - x2) + abs(y1 - y2)
        saved_time = original_dist - distance
        if distance <= 2 and saved_time >= 100:
            cheats_1 += 1
        if distance <= 20 and saved_time >= 100:
            cheats_2 += 1
    return cheats_1, cheats_2

cheats_1, cheats_2 = solving_task(input_day20)
print(f"First solution: {cheats_1}")
print(f"Second solution: {cheats_2}")

