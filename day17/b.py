from program import step 
'''
Hidding my input, but my step function execute one step of my program, disconsidering the last instruction (the loop one).
The key insight here is that the programs starts with B = A % 8 (I think/hope this is true for every input).

Args:
    `A` (int): initial value of register A
returns:
    `int`: the B register mod 8 after one single execution of the program (without the last loop instrucion)
'''

def find(A, col=0):
    if step(A) != expected_output[col]:
        return
    
    # when I find the first possivel value, I print and exit
    if col == len(expected_output) - 1: 
        print(A)
        exit()
    else:
        # each iteraction I need to shift my A (to prevent from interfering with the result I find) and test the answer for each mod 8
        for mod_8 in range(8):
            next_A = A << 3
            next_A += mod_8
            find(next_A, col + 1)


with open('day17/input.txt', 'r') as file:
    lines = file.readlines()
    program = list(map(int, lines[4].strip().split(': ')[-1].split(',')))
    expected_output = program[::-1]

# start the search for each mod 8 on the first (last) program digit
for mod in range(8):
    find(mod)