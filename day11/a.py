from functools import cache

mem = {}
def rec(stones: tuple[int, ...], blinks: int) -> int:

    if (stones, blinks) in mem:
        return mem[(stones, blinks)]
    
    if not blinks:
        mem[(stones, blinks)] = len(stones)
    else:
        mem[(stones, blinks)] = sum([rec(apply_rules(s), blinks-1) for s in stones])
        
    return mem[(stones, blinks)]
    

def apply_rules(stone) -> tuple[int, ...]:
    
    if stone == 0:
        return tuple([1])
    
    elif len(str(stone)) % 2 == 0:
        mid = len(str(stone))//2
        first_half = str(stone)[:mid]
        second_half = str(stone)[mid:]

        return (int(first_half), int(second_half))

    return tuple([stone*2024])

input = tuple(map(int, open("day11/input.txt", "r").read().strip().split()))

print(rec(input, 25))