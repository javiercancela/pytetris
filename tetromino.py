import numpy as np
from random import randrange
from enum import Enum
from square import draw_square
from colors import *

class Tetromino:
    def __init__(self):
        self.layout = None
        self.pos_x = None
        self.pos_y = None

    def rotate_clockwise(self):
        if (isinstance(self, OTetromino)):
            return
        self.layout = np.rot90(self.layout, -1)
    
    def rotate_anticlockwise(self):
        if (isinstance(self, OTetromino)):
            return
        self.layout = np.rot90(self.layout)

    def go_down(self):
        self.pos_y -= 1
    
    def go_right(self):
        self.pos_x += 1
    
    def go_left(self):
        self.pos_x -= 1

    def get_position(self):
        y, x = np.where(self.layout == 1)
        return [[self.pos_x + xn, self.pos_y - yn] for xn, yn in zip(x, y)]    
    
    @staticmethod
    def create_tetromino():
        tetros = {
            0: lambda: ITetromino(),
            1: lambda: JTetromino(),
            2: lambda: LTetromino(),
            3: lambda: OTetromino(),
            4: lambda: STetromino(),
            5: lambda: TTetromino(),
            6: lambda: ZTetromino(),
        }
        tetro_type = randrange(7)
        return tetros[tetro_type]()
        

class ITetromino(Tetromino):
    def __init__(self):
        a = [0,0,0,0]
        b = [1,1,1,1]
        self.layout = np.array([a,b,a,a])
        self.pos_x = 3
        self.pos_y = 21
        self.color = CYAN

class JTetromino(Tetromino):
    def __init__(self):
        a = [1,0,0]
        b = [1,1,1]
        c = [0,0,0]
        self.layout = np.array([a,b,c])
        self.pos_x = 3
        self.pos_y = 21
        self.color = BLUE

class LTetromino(Tetromino):
    def __init__(self):
        a = [0,0,1]
        b = [1,1,1]
        c = [0,0,0]
        self.layout = np.array([a,b,c])
        self.pos_x = 3
        self.pos_y = 21
        self.color = ORANGE


class OTetromino(Tetromino):
    def __init__(self):
        a = [0,1,1,0]
        b = [0,0,0,0]
        self.layout = np.array([a,a,b])
        self.pos_x = 3
        self.pos_y = 21
        self.color = YELLOW

class STetromino(Tetromino):
    def __init__(self):
        a = [0,1,1]
        b = [1,1,0]
        c = [0,0,0]
        self.layout = np.array([a,b,c])
        self.pos_x = 3
        self.pos_y = 21
        self.color = GREEN

class TTetromino(Tetromino):
    def __init__(self):
        a = [0,1,0]
        b = [1,1,1]
        c = [0,0,0]
        self.layout = np.array([a,b,c])
        self.pos_x = 3
        self.pos_y = 21
        self.color = PURPLE

class ZTetromino(Tetromino):
    def __init__(self):
        a = [1,1,0]
        b = [0,1,1]
        c = [0,0,0]
        self.layout = np.array([a,b,c])
        self.pos_x = 3
        self.pos_y = 21
        self.color = RED
