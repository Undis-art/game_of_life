import itertools
import copy

from cell import Cell

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.random_grid()
        self.init_survival_grid()
        
    def random_grid(self):
        self.grid = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                new_cell = Cell()
                row.append(new_cell)
            self.grid.append(row)

    def init_survival_grid(self):
        self.survival_grid = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.survival_grid.append(row)

    def print(self):
        for row in self.grid:
            row_string = ""
            for cell in row:
                row_string += cell.view
            print(row_string)
        print("\n")

    def pass_neighbours(self):
        for y in range(self.height):
            for x in range(self.width):
                cell = self.get_cell(x, y)
                neighbours = self.get_neighbour_cells(x, y)
                cell.set_neighbours(neighbours)

    def next_generation(self):
        self.pass_neighbours()

        for y in range(self.height):
            for x in range(self.width):
                cell = self.get_cell(x, y)
                self.survival_grid[y][x] = cell.will_live()
        for y in range(self.height):
            for x in range(self.width):
                cell = self.get_cell(x, y)
                if self.survival_grid[y][x]:
                    cell.live()
                else:
                    cell.die()


    def get_cell(self, x, y):
        return self.grid[y][x]

    def get_neighbour_cells(self, x, y):
        neighbour_coord_candidates = itertools.product(
                [x-1, x, x+1],
                [y-1, y, y+1]
                )

        neighbours = []
        for coords in neighbour_coord_candidates:
            if coords[0] == x and coords[1] == y:
                continue
            if self.is_legit_coordinate(coords):
                neighbours.append(self.get_cell(coords[0], coords[1]))

        return neighbours

    def is_legit_coordinate(self, xy):
        x = xy[0]
        y = xy[1]
        x_legit = x>=0 and x<self.width
        y_legit = y>=0 and y<self.height
        if x_legit and y_legit:
            return True
        else:
            return False

 
