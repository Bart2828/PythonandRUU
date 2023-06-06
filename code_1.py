import random

class Grid:
    def __init__(self, n):
        self.n = n
        self.grid = [[None] * n for _ in range(n)]
        self.saw = []

    def initialize_saw(self, start_cell):
        self.saw = [start_cell]
        self.grid[start_cell[0]][start_cell[1]] = True

    def get_neighbours(self, cell):
        x, y = cell
        neighbours = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.n and self.grid[nx][ny] is None:
                neighbours.append((nx, ny))

        return neighbours

    def grow_saw(self):
        current_cell = self.saw[-1]
        neighbours = self.get_neighbours(current_cell)

        if not neighbours:  # No valid neighbours, SAW cannot grow further
            return

        next_cell = random.choice(neighbours)
        self.grid[next_cell[0]][next_cell[1]] = True
        self.saw.append(next_cell)

    def print_grid(self):
        for row in self.grid:
            print(' '.join(['X' if cell else '.' for cell in row]))

#voorbeeld
grid = Grid(20)  #maak een rooster van 10x10 cellen
grid.initialize_saw((8, 8))  #initialiseer de SAW vanaf cel (0, 0)

for _ in range(10):  #laat de SAW 9 keer groeien
    grid.grow_saw()

grid.print_grid()  #print het rooster met de gegroeide SAW
