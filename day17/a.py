def get_combo(operand):
    
    if operand < 4:
        return operand
    
    if operand == 4:
        return REGISTERS['A']
    
    if operand == 5:
        return REGISTERS['B']
    
    if operand == 6:
        return REGISTERS['C']
    
    if operand == 7:
        print('Operand Error')
        exit(1)

def adv(instruction_pointer, operand):
    REGISTERS['A'] //= 2**(get_combo(operand))
    return instruction_pointer + 1

def bxl(instruction_pointer, operand):
    REGISTERS['B'] ^= operand
    return instruction_pointer + 1

def bst(instruction_pointer, operand):
    REGISTERS['B'] = get_combo(operand) % 8
    return instruction_pointer + 1

def jnz(instruction_pointer, operand):
    if REGISTERS['A'] != 0:
        return operand
    return instruction_pointer + 1

def bxc(instruction_pointer, operand):
    REGISTERS['B'] ^= REGISTERS['C']
    return instruction_pointer + 1

def out(instruction_pointer, operand):
    print(get_combo(operand) % 8, end=',')
    return instruction_pointer + 1

def bdv(instruction_pointer, operand):
    REGISTERS['B'] = REGISTERS['A'] // 2**(get_combo(operand))
    return instruction_pointer + 1

def cdv(instruction_pointer, operand):
    REGISTERS['C'] = REGISTERS['A'] // 2**(get_combo(operand))
    return instruction_pointer + 1

def print_registers():
    print(f'Register A: {REGISTERS["A"]}')
    print(f'Register B: {REGISTERS["B"]}')
    print(f'Register C: {REGISTERS["C"]}')
    print()

INSTRUCTIONS = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]
REGISTERS = {
    'A': 0,
    'B': 0,
    'C': 0
}

with open('day17/input.txt', 'r') as file:
    lines = file.readlines()
    REGISTERS['A'] = int(lines[0].strip().split(': ')[-1])
    REGISTERS['B'] = int(lines[1].strip().split(': ')[-1])
    REGISTERS['C'] = int(lines[2].strip().split(': ')[-1])

    program = list(map(int, lines[4].strip().split(': ')[-1].split(',')))
    it = iter(program)
    program = list(zip(it, it))

print(program)
instruction_pointer = 0

while instruction_pointer < len(program):
    instruciton_code, operand = program[instruction_pointer]
    instruction_pointer = INSTRUCTIONS[instruciton_code](instruction_pointer, operand)
print()