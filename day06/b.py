input = [line.strip() for line in open("day06/input.txt", "r")]

def get_guard_position(input):
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char == '^':
                return complex(y, x)

def is_guard_in_loop(input, guard_start):

    DIRECTION = -1+0j
    visited = set([])

    while (guard_start, DIRECTION) not in visited:

        visited.add((guard_start, DIRECTION))
        new_pos = guard_start + DIRECTION

        if not( 0 <= new_pos.real < len(input) and 0 <= new_pos.imag < len(input[0])):
            return False

        if input[int(new_pos.real)][int(new_pos.imag)] == '#':
            DIRECTION *= -1j
        else:
            guard_start = new_pos

    return True

possible_loop_placements = 0
guard_start = get_guard_position(input)

for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char == '^':
            continue

        modified_lab = input.copy()
        modified_lab[y] = modified_lab[y][:x] + '#' + modified_lab[y][x+1:]

        if is_guard_in_loop(modified_lab, guard_start):
            possible_loop_placements += 1

print(possible_loop_placements)