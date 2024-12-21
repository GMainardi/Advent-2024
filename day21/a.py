SHORTEST_PATHS = {}
SHORTEST_PATHS[('A', '<')] = 'v<<'
SHORTEST_PATHS[('A', '>')] = 'v'
SHORTEST_PATHS[('A', 'v')] = '<v'
SHORTEST_PATHS[('A', '^')] = '<'
SHORTEST_PATHS[('<', 'A')] = '>>^'
SHORTEST_PATHS[('<', '^')] = '>^'
SHORTEST_PATHS[('<', 'v')] = '>'
SHORTEST_PATHS[('>', 'A')] = '^'
SHORTEST_PATHS[('>', '^')] = '<^'
SHORTEST_PATHS[('>', 'v')] = '<'
SHORTEST_PATHS[('^', 'A')] = '>'
SHORTEST_PATHS[('^', '<')] = 'v<'
SHORTEST_PATHS[('^', '>')] = 'v>'
SHORTEST_PATHS[('v', 'A')] = '^>'
SHORTEST_PATHS[('v', '>')] = '>'
SHORTEST_PATHS[('v', '<')] = '<'

#example
SHORTEST_PATHS[('A', '0')] = '<'
SHORTEST_PATHS[('0', '2')] = '^'
SHORTEST_PATHS[('2', '9')] = '^^>'
SHORTEST_PATHS[('9', 'A')] = 'vvv'

SHORTEST_PATHS[('A', '9')] = '^^^'
SHORTEST_PATHS[('9', '8')] = '<'
SHORTEST_PATHS[('8', '0')] = 'vvv'
SHORTEST_PATHS[('0', 'A')] = '>'

SHORTEST_PATHS[('A', '1')] = '^<<'
SHORTEST_PATHS[('1', '7')] = '^^'
SHORTEST_PATHS[('7', '9')] = '>>'
SHORTEST_PATHS[('9', 'A')] = 'vvv'

SHORTEST_PATHS[('A', '4')] = '^^<<'
SHORTEST_PATHS[('4', '5')] = '>'
SHORTEST_PATHS[('5', '6')] = '>'
SHORTEST_PATHS[('6', 'A')] = 'vv'

SHORTEST_PATHS[('A', '3')] = '^'
SHORTEST_PATHS[('3', '7')] = '<<^^'
SHORTEST_PATHS[('7', '9')] = '>>'
SHORTEST_PATHS[('9', 'A')] = 'vvv'

# input
SHORTEST_PATHS[('A', '3')] = '^'
SHORTEST_PATHS[('3', '8')] = '<^^'
SHORTEST_PATHS[('8', '2')] = 'vv'
SHORTEST_PATHS[('2', 'A')] = 'v>'

SHORTEST_PATHS[('A', '1')] = '^<<'
SHORTEST_PATHS[('1', '7')] = '^^'
SHORTEST_PATHS[('7', '6')] = 'v>>'
SHORTEST_PATHS[('6', 'A')] = 'vv'

SHORTEST_PATHS[('A', '4')] = '^^<<'
SHORTEST_PATHS[('4', '6')] = '>>'
SHORTEST_PATHS[('6', '3')] = 'v'
SHORTEST_PATHS[('3', 'A')] = 'v'

SHORTEST_PATHS[('A', '0')] = '<'
SHORTEST_PATHS[('0', '8')] = '^^^'
SHORTEST_PATHS[('8', '3')] = 'vv>'
SHORTEST_PATHS[('3', 'A')] = 'v'

SHORTEST_PATHS[('A', '7')] = '^^^<<'
SHORTEST_PATHS[('7', '8')] = '>'
SHORTEST_PATHS[('8', '9')] = '>'
SHORTEST_PATHS[('9', 'A')] = 'vvv'

def get_sequence( typing):
    pairs = zip(typing, typing[1:])
    encoded = ''
    for start, end in pairs:
        if start != end:
            encoded += SHORTEST_PATHS[(start, end)]
        encoded += 'A'
    return encoded


total = 0
for line in open('day21/input.txt', 'r'):
    numeric = 'A' + line.strip()
    robot = 'A' + get_sequence(numeric)
    for _ in range(2):
        robot = 'A' + get_sequence(robot)
    min_sequence = len(robot) - 1
    total += min_sequence * int(numeric[1:-1])

print(total)