with open('day24/fix.txt', 'r') as f:
    _, connections = f.read().split('\n\n')
    connections = [
        (connection.split(' ')[0], connection.split(' ')[2], connection.split(' ')[4], connection.split(' ')[1])
        for connection in connections.split('\n')
    ]

with open('day24/out.txt', 'wb') as out:
    out.write(b'digraph G {\n')
    for (left, right, value, operation) in connections:
        srting = f'{left} -> {value} [label="{operation}"]; \n'
        out.write(bytes(srting, 'utf-8'))
        srting = f'{right} -> {value} [label="{operation}"]; \n'
        out.write(bytes(srting, 'utf-8'))
    out.write(b'}')


result = [
    'z09', 'rkf',
    'vcg', 'z24',
    'z20', 'jgb',
    'rrs', 'rvc'
]

print(','.join(sorted(result)))