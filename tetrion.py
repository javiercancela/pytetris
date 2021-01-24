import numpy as np
from colors import *

class Tetrion:
    def __init__(self):
        self.grid = np.full((22, 10), 0)
        self.color = GREY

    def is_collision(self, tetromino, movement):
        bounds_detected = False
        blocks_detected = False
        squares = tetromino.get_position()
        for square in squares:
            next = [a + b for a, b in (zip(square, movement))]
            bounds_detected = any([next[0] < 0, next[0] > 9, next[1] < 0])
            if bounds_detected:
                break
            blocks_detected = (self.grid[next[1]][next[0]] == 1)
            if blocks_detected:
                break

        return bounds_detected or blocks_detected

    def add_squares(self, squares):
        new_grid = np.full((22, 10), 0)
        for square in squares:
            self.grid[square[1], square[0]] = 1
        kept_rows = 0
        for row in self.grid[:]:
            if 0 in row:
                new_grid[kept_rows] = row
                kept_rows += 1
        self.grid = new_grid
                
        

    def get_squares(self):
        y, x = np.where(self.grid == 1)
        return [[xn, yn] for xn, yn in zip(x, y)]    
        