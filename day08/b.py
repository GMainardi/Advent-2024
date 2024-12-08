def add_antinode(y_max: int, x_max: int, antinode: complex):
    return (0 <= antinode.imag < x_max) and (0 <= antinode.real < y_max)

def insert_antinodes(loc1, loc2, YMAX, XMAX):
    antinodes = set([])
    anti = loc1
    i = 0
    while add_antinode(YMAX, XMAX, anti):
        antinodes.add(anti)
        i+=1
        anti = loc1 + (loc1-loc2)*i

    return antinodes

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
            
            antinodes = antinodes.union(insert_antinodes(loc1, loc2, YMAX, XMAX))
            antinodes = antinodes.union(insert_antinodes(loc2, loc1, YMAX, XMAX))

print(len(antinodes))