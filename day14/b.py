import cv2 as cv
import numpy as np

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
    
# save the grid as a png file, where Flase should be a pixel with color (0, 0, 0) and True should be a pixel with color (255, 255, 255)
def print_grid(robots, wide, tall, step):

    image_name = f'day14/out/second_{step}.png'
    grid = np.array([np.array([(0, 0, 0) for _ in range(wide)]) for _ in range(tall)])
    for robot in robots:
        grid[int(robot.pos.imag)][int(robot.pos.real)] = (255, 255, 255)
    return grid



robots = [Robot(line.strip()) for line in open('day14/input.txt', 'r').readlines()]
wide = 101
tall = 103


for seconds in range(1, 7083 + 1):
    for robot in robots:
        robot.step(wide, tall)


grid = print_grid(robots, wide, tall, seconds)
cv.imwrite('day14/tree.png', grid.astype(np.uint8))
