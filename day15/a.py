DIRECTIONS = {
    '^': -1+0j,
    'v': 1+0j,
    '>': 0+1j,
    '<': 0-1j
}

def is_move_legal(maze, position, direction):
    
    new_position = position + direction
    while 0 <= new_position.real and new_position.real < len(maze) and 0 <= new_position.imag and new_position.imag < len(maze[0]):

        if maze[int(new_position.real)][int(new_position.imag)] == '#':
            return False
        
        if maze[int(new_position.real)][int(new_position.imag)] == '.':
            return new_position
        
        new_position += direction

    return False

def rearrange_maze(maze, position, next_empty_position, direction):
    
    maze[int(position.real)][int(position.imag)] = '.'
    position += direction
    maze[int(position.real)][int(position.imag)] = '@'
    while position != next_empty_position:
        position += direction
        maze[int(position.real)][int(position.imag)] = 'O'
    
    return maze
    
def move(maze, position, direction):
    next_empty = is_move_legal(maze, position, direction)

    if next_empty:
        maze = rearrange_maze(maze, position, next_empty, direction)
        position += direction
    
    return maze, position

def count_gps_coordinates(maze):
    gps = 0
    for idy, row in enumerate(maze):
        for idx, cell in enumerate(row):
            if cell == 'O':
                gps += 100 * idy + idx
    return gps


def get_starting_position(maze):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == '@':
                return complex(y, x)
            
def print_maze(maze):
    for row in maze:
        print(''.join(row))
    print()


with open('day15/input.txt', 'r') as f:
    input = f.read().split('\n\n')

    maze = [list(row) for row in input[0].split('\n')]
    instructions = input[1].replace('\n', '')

pos = get_starting_position(maze)

for instruction in instructions:
    maze, pos = move(maze, pos, DIRECTIONS[instruction])

print(count_gps_coordinates(maze))