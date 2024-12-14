
class GardenPlot:

    def __init__(self, start:complex, garden_map: list[str]) -> None:
        self.garden_type = garden_map[int(start.real)][int(start.imag)]
        self.garden = self.get_garden_blob(start, garden_map)


    def get_garden_blob(self, start: complex, garden_map: list[str]) -> set[complex]:
        visited = set([])
        blob = set([start])
        queue = [start]
        

        while queue:
            current = queue.pop(0)
            visited.add(current)

            for direction in DIRECTIONS.values():
                new_pos = current + direction

                if new_pos in visited:
                    continue
                else:
                    visited.add(new_pos)
    
                if new_pos.real < 0 or new_pos.imag < 0 or new_pos.real >= len(garden_map) or new_pos.imag >= len(garden_map[0]):
                    
                    continue

                if garden_map[int(new_pos.real)][int(new_pos.imag)] == self.garden_type:
                    blob.add(new_pos)
                    queue.append(new_pos)

        return blob

    def get_area(self) -> int:
        return len(self.garden)
    
    def get_sides(self) -> int:
        if len(self.garden) == 1:
            return 4

        points = {}
        for point in self.garden:
            for diag in [0.5+0.5j, 0.5-0.5j, -0.5+0.5j, -0.5-0.5j]:
                    diag_point = point + diag
                    points[diag_point] = points.get(diag_point, 0) + 1
        sides = 0
        for _, counts in points.items():
            if counts % 2 == 1:
                sides += 1
        

        for point in self.garden:
            for diag in [1+1j, 1-1j, -1+1j, -1-1j]:
                if point + diag in self.garden:
                    if points[point + (diag/2)] == 2:
                        sides += 1

        return sides
        
    def is_in_garden(self, point: complex) -> bool:
        return point in self.garden
    
    def __repr__(self):
        return f"GardenPlot({self.garden_type},{self.garden})"
DIRECTIONS = { 
    'up': -1+0j, 
    'down': 1+0j, 
    'left': 0-1j, 
    'right': 0+1j}

input = [line.strip() for line in open("day12/input.txt", "r").readlines()]

garden = []

total_cost = 0
for i, line in enumerate(input):
    for j, char in enumerate(line):
        if not any([gardenplot.is_in_garden(complex(i, j)) for gardenplot in garden]):
            gardenplot = GardenPlot(complex(i, j), input)
            garden.append(gardenplot)
            total_cost += gardenplot.get_area() * gardenplot.get_sides()

print(total_cost)