def cast_locks(lock: list[str]) -> set:
    lock_key = set([])

    for idy, line in enumerate(lock):
        for idx, char in enumerate(line):
            if char == '#':
                lock_key.add(complex(idy, idx))
    return lock_key

def lock_fits(lock, key):
    
    if len(lock & key) != 0:
        return False
    
    
    return True


with open('day25/input.txt', 'r') as file:
    lock_keys = file.read().split('\n\n')

    lock_keys = list(map(lambda x:[line.strip() for line in x.split('\n')], lock_keys))

    LOCK_HIGHT = len(lock_keys[0])
    LOCK_WIDTH = len(lock_keys[0][0])

    lock_keys = list(map(cast_locks, lock_keys))


fits = 0
for idx, lock in enumerate(lock_keys):
    for jdx, key in enumerate(lock_keys[idx+1:]):

        fits += lock_fits(lock,key)


print(fits)
