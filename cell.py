import random

class Cell:
    alive = 0
    neighbours = [] # also Cells
    view = "."
    
    def __init__(self):
        f = random.uniform(0, 1)
        self.alive = f < 0.3
        self.view = "0" if self.alive else "."

    def set_neighbours(self, neighbours):
        self.neighbours = neighbours

    def n_living_neighbours(self):
        n = 0
        for c in self.neighbours:
            if c.alive:
                n = n+1
        return n

    def will_live(self):
        n = self.n_living_neighbours()
        if self.alive:
            if (n==2 or n==3):
                live = True
            else:
                live = False
        else: # atm dead
            if n==3:
                live = True
            else:
                live = False
        if live:
            return True 
        else:
            return False

    def live(self):
        self.alive = 1
        self.view = "0"
    
    def die(self):
        self.alive = 0
        self.view = "."
