from tqdm import tqdm
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

def find_wall_path(maze, start, end):
    queue = [start]
    visited = {start}

    while queue:
        curr = queue.pop(0)

        if curr == end:
            return True
        
        for direction in [1, -1, 1j, -1j]:
            next = curr + direction

            if not in_bounds(maze, next):
                continue
            
            if next == end:
                return True
            
            if maze[int(next.real)][int(next.imag)] == '#' and next not in visited:
                visited.add(next)
                queue.append(next)

    return False

def print_maze(maze):
    for row in maze:
        print(''.join(row))

def get_cheat_path(path, start, start_idx):

    cheats = []
    for dest in path[start_idx+99:]:
        cheat_dist = abs(dest.real - start.real) + abs(dest.imag - start.imag)
        if cheat_dist <= 20:
            if find_wall_path(maze, start, dest):
                cheats.append(dest)
    return cheats

def find_cheats(path):
    cheats = {}
    for idx, step in tqdm(enumerate(path)):

        possible_cheats = get_cheat_path(path, step, idx)
        for cheat in possible_cheats:

            cheat_dist = abs(cheat.real - step.real) + abs(cheat.imag - step.imag)
            
            saved_time = path.index(cheat, idx) - idx - cheat_dist
            cheats[saved_time] = cheats.get(saved_time, 0) + 1
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