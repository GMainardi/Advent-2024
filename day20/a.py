def get_point(maze, char):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == char:
                return complex(y, x)
            
def in_bounds(maze, point):
    return 0 <= point.real < len(maze[0]) and 0 <= point.imag < len(maze)

def find_path(maze, start, end):
    queue = [(start, [start])]
    visited = {start}

    while queue:
        curr, path = queue.pop(0)

        if curr == end:
            return path
        
        for direction in [1, -1, 1j, -1j]:
            next = curr + direction

            if not in_bounds(maze, next):
                continue

            if maze[int(next.real)][int(next.imag)] == '.' and next not in visited:
                visited.add(next)

                queue.append((next, path + [next]))

    return {}

def print_maze(maze):
    for row in maze:
        print(''.join(row))

def find_cheats(path):
    cheats = {}
    for idx, step in enumerate(path):
        for direction in [1, -1, 1j, -1j]:
            next = step + direction
            try:
                cheat_step = path.index(next, idx + 1)
                cheated_steps = cheat_step - idx - 2
                cheats[cheated_steps] = cheats.get(cheated_steps, 0) + 1
            except ValueError:
                continue
    return cheats
            
maze = [list(line.strip()) for line in open('day20/input.txt', 'r').readlines()]
start = get_point(maze, 'S')
end = get_point(maze, 'E')
maze[int(start.real)][int(start.imag)] = '.'
maze[int(end.real)][int(end.imag)] = '.'

shortest_path = find_path(maze, start, end)

cheats = find_cheats(shortest_path)

cheating_paths = sum(map(lambda x: x[1], filter(lambda x: x[0] >= 100, cheats.items())))
print(cheating_paths)