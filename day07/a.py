
def check_possible_number(goal, value, numbers):
    if len(numbers) == 0:
        return value == goal
    
    next = numbers.pop(0)
    return any([check_possible_number(goal, value + next, numbers.copy()),
                check_possible_number(goal, value * next, numbers.copy())])


correct_lines = 0
for line in open('day07/input.txt', 'r').readlines():
    line = line.strip()
    goal = int(line.split(':')[0])
    numbes = list(map(int, line.split(':')[1].split(' ')[1:]))
    
    if check_possible_number(goal, 0, numbes.copy()):
        correct_lines += goal
print(correct_lines)