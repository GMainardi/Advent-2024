DIRECTIONS = {
    '^': -1+0j,
    'v': 1+0j,
    '>': 0+1j,
    '<': 0-1j
}

def can_move_box(maze, position, direction):

    new_pos = position + direction

    if maze[int(new_pos.real)][int(new_pos.imag)] == '#':
        return False

    if maze[int(new_pos.real)][int(new_pos.imag)] == '.':
        return True

    if direction.real == 0 or maze[int(new_pos.real)][int(new_pos.imag)] == '@':
        return can_move_box(maze, new_pos, direction)
    
    if maze[int(new_pos.real)][int(new_pos.imag)] == '[':
        return can_move_box(maze, new_pos, direction) and can_move_box(maze, new_pos + 1j, direction)
    
    return can_move_box(maze, new_pos, direction) and can_move_box(maze, new_pos - 1j, direction)
    

def swap_places(maze, pos, next):
    maze[int(pos.real)][int(pos.imag)], maze[int(next.real)][int(next.imag)] = maze[int(next.real)][int(next.imag)], maze[int(pos.real)][int(pos.imag)]
    return maze

def rearrange_maze(maze, position, direction):
    
    next = position + direction

    if maze[int(next.real)][int(next.imag)] == '.':
            return swap_places(maze, position, next)
    
    if direction.real == 0:
        maze = rearrange_maze(maze, next, direction)
        return swap_places(maze, position, next)

    if maze[int(next.real)][int(next.imag)] == '[':
        maze = rearrange_maze(maze, next, direction)
        maze = rearrange_maze(maze, next + 1j, direction)

        return swap_places(maze, position, next)
    
    elif maze[int(next.real)][int(next.imag)] == ']':
        maze = rearrange_maze(maze, next, direction)
        maze = rearrange_maze(maze, next - 1j, direction)

        return swap_places(maze, position, next)


def move(maze, position, direction):

    if can_move_box(maze, position, direction):
        maze = rearrange_maze(maze, position, direction)
        position += direction
    
    return maze, position

def count_gps_coordinates(maze):
    gps = 0
    for idy, row in enumerate(maze):
        for idx, cell in enumerate(row):
            if cell == '[':
                gps += 100 * idy + idx
    return gps


def get_starting_position(maze):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == '@':
                return complex(y, x)

def assable_maze(maze):
    new_maze = []
    for row in maze:
        new_row = row.replace('.', '..').replace('#', '##').replace('@', '@.').replace('O', '[]')
        new_maze.append(list(new_row))  
    return new_maze
        
def print_maze(maze):
    for row in maze:
        print(''.join(row))
    print()


with open('day15/input.txt', 'r') as f:
    input = f.read().split('\n\n')

    maze = assable_maze([row for row in input[0].split('\n')])
    instructions = input[1].replace('\n', '')

pos = get_starting_position(maze)

for instruction in instructions:
    maze, pos = move(maze, pos, DIRECTIONS[instruction])

print(count_gps_coordinates(maze))