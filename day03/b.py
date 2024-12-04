import re
import functools


text = ''.join(open('day03/input.txt', 'r').readlines())

expression = r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'
valids = re.findall(expression, text)

DO = True

sum = 0
for command in valids:

    if command == 'do()':
        DO = True
        continue

    if command == 'don\'t()':
        DO = False

    if not DO:
        continue
    
    sum += functools.reduce(lambda x, y: x*y, (map(int, re.findall(r'\d{1,3}', command))))
    

print(sum)
