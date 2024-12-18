from collections import deque
from inputs import input_day18

def falling_bytes(input_day18, falling):
    bytes_input = [row for row in input_day18.strip().split("\n")]
    bytes_int = []
    for index,row in enumerate(bytes_input):
        if index < falling:
            split = row.strip().split(",")
            inst = (int(split[0]), int(split[1]))
            bytes_int.append(inst)
        else:
            break
    return bytes_int

def creating_maze(byte):
    width = 71
    height = 71
    memory = [["." for _ in range(width)] for _ in range(height)]
    for inst in byte:
        x,y = inst
        memory[y][x] = "#"
    return memory

def solving_maze(maze):
    start = (0,0)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = deque()
    queue.append((start[0],start[1],0))
    visited_pos = set()
    while queue:
        x,y,dist = queue.popleft()
        if (x,y) in visited_pos:
            continue
        visited_pos.add((x,y))
        if (x,y) == (70,70):
            return dist
        for dx,dy in directions:
            nx, ny = x+dx , y+dy
            if 0<= nx <= 70 and 0<=ny <=70 and maze[ny][nx] != "#" and (nx,ny) not in visited_pos:
                queue.append((nx,ny,dist+1))
    return "FAILED"

for i in range(0,3450):
    byte = falling_bytes(input_day18, i)
    maze = creating_maze(byte)
    distance = solving_maze(maze)
    if distance == "FAILED":
        print(byte[-1])
        break
