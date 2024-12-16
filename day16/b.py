from heapq import heappop, heappush
from functools import reduce

def can_step(maze, step):
    return maze[step[0]][step[1]] != '#'

def rotate_clockwise(direction: tuple[int]):
    return - direction[1], direction[0]

def rotate_counter_clockwise(direction: tuple[int]):
    return direction[1], - direction[0]

def get_point(maze, point_char):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == point_char:
                return i, j
def get_maze_points(maze):
    points = []
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == '.':
                points.append((i, j))
    return points

def print_maze(maze):
    for row in maze:
        print(''.join(row))

def get_allowed_steps(maze, pos, direction):
    clockwise = rotate_clockwise(direction)
    counter_clockwise = rotate_counter_clockwise(direction)
    
    allowed = [(pos, counter_clockwise), (pos, clockwise)]
    
    forward = (pos[0] + direction[0], pos[1] + direction[1])
    if can_step(maze, forward):
        allowed.append((forward, direction))

    return allowed

def dijkstra(maze, start):
    queue = [(0, start, (0, 1), set([start]))] 
    visited = {
        pos: {direction: {"score": float("inf"), "tiles": set()} for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]}
        for pos in get_maze_points(maze)
    }

    while queue:
        score, curr, direction, tiles = heappop(queue)
        allowed = get_allowed_steps(maze, curr, direction)
        for step, new_dir in allowed:
            step_score = score + 1 if new_dir == direction else score + 1000
            state = visited[step][new_dir]

            if step_score > state["score"]:
                continue

            new_tiles = tiles | {step}
            state["score"] = step_score
            state["tiles"] |= new_tiles
            heappush(queue, (step_score, step, new_dir, state["tiles"]))

    return visited


maze = [list(line.strip()) for line in open('day16/input.txt', 'r').readlines()]
start = get_point(maze, 'S')
end = get_point(maze, 'E')
maze[start[0]][start[1]] = '.'
maze[end[0]][end[1]] = '.'

paths = dijkstra(maze, start)
best_path = min(paths[end].values(), key = lambda x: x['score'])

print(len(best_path['tiles']))