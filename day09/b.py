def merge_disk(disk):
    idx = 0
    while idx < len(disk) - 1:
        if disk[idx][1] == disk[idx+1][1]:
            disk[idx] = (disk[idx][0] + disk[idx+1][0], disk[idx][1])
            disk.pop(idx+1)
        else:
            idx += 1

    return disk

def compact_disk(disk):
    end = len(disk) - 1
    while end >= 0:
        disk = merge_disk(disk)

        if disk[end][1] == '.':
            end -= 1
            continue

        for idx in range(end):
            if disk[idx][1] == '.':
                if disk[idx][0] == disk[end][0]:
                    disk[idx] = (disk[end][0], disk[end][1])
                    disk[end] = (disk[end][0], '.')
                    break
                elif disk[idx][0] > disk[end][0]:
                    diff = disk[idx][0] - disk[end][0]
                    disk[idx] = (disk[end][0], disk[end][1])
                    disk[end] = (disk[end][0], '.')
                    disk.insert(idx+1, (diff, '.'))
                    break
        end -= 1
    return disk
        
def check_sum(disk):
    sum = 0
    idx = 0
    for space, id in disk:
        while space > 0:
            if type(id) == int:
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

compact = compact_disk(id_disk)
print(check_sum(compact))