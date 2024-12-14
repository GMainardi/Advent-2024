from sympy import Symbol, Eq
from sympy import solve
import re

class ClawMachine:

    def __init__(self, machine_desc: list):

        self.a_button = complex(machine_desc[0], machine_desc[1])
        self.b_button = complex(machine_desc[2], machine_desc[3])
        self.prize = complex(10000000000000+machine_desc[4], 10000000000000+machine_desc[5])

    def get_press(self) -> tuple:

        n = Symbol('n')
        m = Symbol('m')

        eq1 = Eq(n*self.a_button.real + m*self.b_button.real, self.prize.real)
        eq2 = Eq(n*self.a_button.imag + m*self.b_button.imag, self.prize.imag)

        solution = solve((eq1, eq2), (n, m))

        n = solution[n]
        m = solution[m]

        if n - int(n) > 1e-5 or m - int(m) > 1e-5:
            return 0, 0
        
        return int(n), int(m)
    
    def __repr__(self):
        return f'ClawMachine({self.a_button}, {self.b_button}, {self.prize})'


machine_match = re.compile(
    r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
)

tokens = 0
for claw_machine in machine_match.findall(open('day13/input.txt', 'r').read()):

    machine = ClawMachine(list(map(int, claw_machine)))
    n, m = machine.get_press()
    tokens += 3*n + m
    
print(tokens)