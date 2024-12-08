def add_antinode(y_max: int, x_max: int, antinode: complex):
    return (0 <= antinode.imag < x_max) and (0 <= antinode.real < y_max)


antenas = {}
input = [line.strip() for line in open("day08/input.txt", "r")]
YMAX = len(input)
XMAX = len(input[0])
for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char != '.':
            antenas[char] = antenas.get(char, []) + [complex(y, x)]

antinodes = set([])

for antena_locs in antenas:
    for idx, loc1 in enumerate(antenas[antena_locs]):
        for loc2 in antenas[antena_locs][idx+1:]:
    
            anti1 = loc1 + (loc1 - loc2)
            if add_antinode(YMAX, XMAX, anti1):
                antinodes.add(anti1)

            anti2 = loc2 + (loc2 - loc1)
            if add_antinode(YMAX, XMAX, anti2):
                antinodes.add(anti2)

print(len(antinodes))