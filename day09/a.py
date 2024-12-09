def get_last_filled_idx(disk):

    return sum([val[0] for val in disk if val[1] != '.'])

def disk_to_fill(disk):
    spaces = get_last_filled_idx(disk)


    compacted_disk_size = 0
    for idx, (space, id) in enumerate(disk):
        compacted_disk_size += space
        if compacted_disk_size == spaces:
            return disk[:idx], disk[idx:][::-1]
        
        if compacted_disk_size > spaces:
            split_space = (compacted_disk_size - spaces)
            return disk[:idx] + [(space - split_space, id)],  disk[idx+1:][::-1] + [(split_space, id)]

def fill_disk(disk, queue):
    filled_disk = []
    while queue:
        curr = queue.pop(0)

        if not disk:
            break
        
        while disk[0][1] != '.':
            filled_disk.append(disk.pop(0))
        
        if curr[1] == '.':
            continue

        if curr[0] > disk[0][0]:
            filled_disk.append((disk[0][0], curr[1]))
            curr = (curr[0] - disk[0][0], curr[1])
            disk.pop(0)
            queue.insert(0, curr)

        elif disk[0][0] > curr[0]:
            filled_disk.append((curr[0], curr[1]))
            disk[0] = (disk[0][0] - curr[0], disk[0][1])

        else:
            filled_disk.append((curr[0], curr[1]))
            disk.pop(0)
    while disk:
        filled_disk.append(disk.pop(0))

    return filled_disk
        
def check_sum(disk):
    sum = 0
    idx = 0
    print(disk)
    for space, id in disk:
        while space > 0:
            sum += idx * id
            idx += 1
            space -= 1
    return sum
    
disk = [int(char) for char in open('day09/input.txt', 'r').read().strip()]

id_disk = []
id = 0
for idx, val in enumerate(disk):
    if idx % 2 == 0:
        id_disk.append((val, id))
    else:
        id_disk.append((val, '.'))
        id += 1

compacted_disk, queue = disk_to_fill(id_disk)
filled_disk = fill_disk(compacted_disk, queue)
print(check_sum(filled_disk))