import functools

def sum_lines(x, y):
    return f'{x[0] - x[1]} {x[1] + y[1]}'


with open('day01/input.txt') as f:

    lines = f.readlines()
    left = map(lambda x: int(x.strip().split(' ')[0]), lines)
    left = sorted(list(left))

    rigth = map(lambda x: int(x.strip().split(' ')[-1]), lines)
    rigth = sorted(list(rigth))
    
total = [abs(x[0] - x[1]) for x in zip(left, rigth)]
print(sum(total))