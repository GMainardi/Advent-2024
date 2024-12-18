def print_memory(memory, end):
    for y in range(int(end.imag)+1):
        for x  in range(int(end.real)+1):
            if complex(x, y) in memory:
                print('#', end='')
            else:
                print('.', end='')
        print()

def in_bounds(point, end):
    return 0 <= point.real <= end.real and 0 <= point.imag <= end.imag

def find_path(memory, start, end):
    queue = [(start, 0)]
    visited = {start}

    while queue:
        curr, steps = queue.pop(0)

        if curr == end:
            return steps
        
        for direction in [1, -1, 1j, -1j]:
            next = curr + direction

            if not in_bounds(next, end):
                continue

            if next not in memory and next not in visited:
                visited.add(next)
                queue.append((next, steps+1))

    return -1

bytes = [complex(int(line.strip().split(',')[0]), int(line.strip().split(',')[1]))  for line in open('day18/input.txt', 'r').readlines()]
memory = set(bytes[:1024])
mem_queue = bytes[1024:]

start = 0+0j
end = 70+70j

for byte in mem_queue:
    memory.add(byte)
    if find_path(memory, start, end) == -1:
        print(f'{int(byte.real)},{int(byte.imag)}')
        break