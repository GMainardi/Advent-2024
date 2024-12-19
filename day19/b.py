from functools import cache

with open('day19/input.txt', 'r') as file:
    data = file.readlines()
    towels = tuple(data[0].strip().split(', '))

    requests = list(map(lambda x: x.strip(), data[2:]))

@cache
def is_pattern_possible(towels, pattern):

    if len(pattern) == 0:
        return 1
    
    is_possible = 0
    for towel in towels:
        if pattern.startswith(towel):
            is_possible += is_pattern_possible(towels, pattern[len(towel):])

    return is_possible

possible_patterns_count = 0
for pattern in requests:
    possible_patterns_count += is_pattern_possible(towels, pattern)
        

print(possible_patterns_count)