UP = -1+0j
DOWN = 1+0j
LEFT = 0-1j
RIGHT = 0+1j

def valid_move(curr, hiking_map):
    return 0 <= curr.real < len(hiking_map) and 0 <= curr.imag < len(hiking_map[0])

def get_map_pos(curr, hiking_map):
    return hiking_map[int(curr.real)][int(curr.imag)]

def count_trailhead_score(curr, hiking_map):

    if get_map_pos(curr, hiking_map) == 9:
        return set([curr])
    
    score = set([])
    for direction in [UP, DOWN, LEFT, RIGHT]:
        next = curr + direction
        if valid_move(next, hiking_map) \
        and get_map_pos(next, hiking_map) - get_map_pos(curr, hiking_map) == 1:
            score = score.union(count_trailhead_score(next, hiking_map))
    
    return score

hiking_map = [list(map(int, line.strip())) for line in open('day10/input.txt', 'r').readlines()]


map_score = 0
for idx, line in enumerate(hiking_map):
    for jdx, char in enumerate(line):
        if char == 0:
            map_score += len(count_trailhead_score(complex(idx, jdx), hiking_map))

print(map_score)