from inputs import input_day16_maze
from collections import deque
maze_str = [row for row in input_day16_maze.strip().split("\n")]
for row in maze_str:
    print(row)

def get_start_position(maze):
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            if maze[y][x] == "S":
                return x,y

def solving_maze(maze):
    width, height = len(maze[0]), len(maze)
    start = get_start_position(maze)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = [[[float('inf')] * len(directions) for _ in range(width)] for _ in range(height)]

    queue = deque()
    queue.append((start[0], start[1], 0, directions[0], 0))
    min_score = float('inf')

    while queue:
        x, y, dist, current_dir, turns = queue.popleft()
        current_dir_index = directions.index(current_dir)

        score = turns * 1000 + dist
        if visited[y][x][current_dir_index] <= score:
            continue
        visited[y][x][current_dir_index] = score

        if maze[y][x] == "E":
            min_score = min(min_score, score)
            continue

        for dir in directions:
            nx, ny = x + dir[0], y + dir[1]
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] != "#":
                is_turn = dir != current_dir
                queue.append((nx, ny, dist + 1, dir, turns + is_turn))

    return min_score

solution = solving_maze(maze_str)
print(solution)
