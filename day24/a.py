OPERATIONS = {
    'AND': lambda x, y: x & y,
    'OR': lambda x, y: x | y,
    'XOR': lambda x, y: x ^ y
}

with open('day24/fix.txt', 'r') as f:
    values, connections = f.read().split('\n\n')

    values = {value.split(': ')[0]: bool(int(value.split(': ')[1])) for value in values.split('\n')}
    connections = [
        {
            'left': connection.split(' ')[0],
            'operation': connection.split(' ')[1],
            'right': connection.split(' ')[2],
            'output': connection.split(' ')[4]
        }
        for connection in connections.split('\n')
    ]

while connections:
    for connection in connections:
        if connection['left'] in values and connection['right'] in values:
            values[connection['output']] = OPERATIONS[connection['operation']](values[connection['left']], values[connection['right']])
            connections.remove(connection)

z_values = []

for key, values in values.items():
    if key.startswith('z'):
        z_values.append((key, values))

z_values.sort(key=lambda x: x[0])

result = 0
for i, (key, value) in enumerate(z_values):
    result += value * 2 ** i
print(result)