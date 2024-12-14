import functools

class Robot:

    def __init__(self, description):
        p, v = description.split(' ')

        self.pos = complex(*list(map(int, p.replace('p=', '').split(','))))
        self.vel = complex(*list(map(int, v.replace('v=', '').split(','))))
    
    def step(self, wide, tall):
        self.pos += self.vel
        if self.pos.real < 0:
            self.pos = complex(wide + self.pos.real, self.pos.imag)

        if self.pos.imag < 0:
            self.pos = complex(self.pos.real, tall + self.pos.imag)
        
        if self.pos.real >= wide:
            self.pos = complex(self.pos.real - wide, self.pos.imag)

        if self.pos.imag >= tall:
            self.pos = complex(self.pos.real, self.pos.imag - tall)

    def __hash__(self):
        return hash((self.pos, self.vel))
    
    def __repr__(self):
        return f'Robot({self.pos}, {self.vel})'
    
    def get_quadrant(self, wide, tall):
        
        if self.pos.real == wide // 2 or self.pos.imag == tall // 2:
            return 0
        
        if self.pos.real < wide // 2:
            if self.pos.imag < tall // 2:
                return 1
            else:
                return 3
        else:
            if self.pos.imag < tall // 2:
                return 2
            else:
                return 4
    

def print_grid(robots, wide, tall):
    grid = [[0 for _ in range(wide)] for _ in range(tall)]
    for robot in robots:
        grid[int(robot.pos.imag)][int(robot.pos.real)] += 1
    for row in grid:
        print(row)
    print()


robots = [Robot(line.strip()) for line in open('day14/input.txt', 'r').readlines()]
wide = 101
tall = 103

for _ in range(100):
    for robot in robots:
        robot.step(wide, tall)

q_counts = [0] * 5
for robot in robots:
    q_counts[robot.get_quadrant(wide, tall)] += 1

# print_grid(robots, wide, tall)
print(functools.reduce(lambda x, y: x * y, q_counts[1:]))