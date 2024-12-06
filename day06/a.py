input = [line.strip() for line in open("day06/input.txt", "r")]

def get_guard_position(input):
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char == '^':
                return complex(y, x)
            
def guard_patrol(input, guard_pos):
    
    visited = set([guard_pos])
    DIRECTION = -1+0j

    while True:
        new_pos = guard_pos + DIRECTION

        if not( 0 <= new_pos.real < len(input) and 0 <= new_pos.imag < len(input[0])):
            break

        if input[int(new_pos.real)][int(new_pos.imag)] == '#':
            DIRECTION *= -1j
        else:
            guard_pos = new_pos
            visited.add(guard_pos)
    return visited

guard_pos = get_guard_position(input)
visited = guard_patrol(input, guard_pos)
print(len(visited))