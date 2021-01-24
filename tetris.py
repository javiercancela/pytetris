import pyglet
from tetromino import Tetromino
from tetrion import Tetrion
from square import draw_square

BLOCK_WIDTH = 22
PLAYFIELD_COORD_X = 200
PLAYFIELD_COORD_Y = 200

class Tetris(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        self.tetrion = Tetrion()
        self.win = pyglet.window.Window.__init__(self, *args, **kwargs)

        self.batch = pyglet.graphics.Batch()
        self.playfield = pyglet.shapes.Rectangle(200, 200, 220, 484, color=(64, 64, 64), batch=self.batch)
        self.tetromino = Tetromino.create_tetromino()
        self.next_tetromino = Tetromino.create_tetromino()

        pyglet.clock.schedule_interval(self.update, 1/120)
        pyglet.clock.schedule_interval(self.auto_lower_tt, 1/1)
        self.sprites = self.get_sprites()
        self.debug1 = pyglet.text.Label(font_name="Tahoma", font_size=12, x = 620, y=700, batch=self.batch)
        self.debug2 = pyglet.text.Label(font_name="Tahoma", font_size=12, x = 620, y=660, batch=self.batch)

    def update(self, dt):
        self.sprites = self.get_sprites()

    def auto_lower_tt(self, dt):
        self.lower_tt()

    def lower_tt(self):
        if (self.check_next_tetromino()):
            if (self.tetromino.pos_y > 19):
                self.end_game()
                return False
            self.tetromino = self.next_tetromino
            self.next_tetromino = Tetromino.create_tetromino()
            return False
        self.tetromino.go_down()
        return True

    def get_sprites(self):
        sprites = []
        squares = self.tetromino.get_position()
        for square in squares:
            pos_x = square[0]
            pos_y = square[1]
            x = pos_x * BLOCK_WIDTH + PLAYFIELD_COORD_X
            y = pos_y * BLOCK_WIDTH + PLAYFIELD_COORD_Y
            sprites.append(draw_square(x, y, self.batch, self.tetromino.color))

        squares = self.tetrion.get_squares()
        for square in squares:
            pos_x = square[0]
            pos_y = square[1]
            x = pos_x * BLOCK_WIDTH + PLAYFIELD_COORD_X
            y = pos_y * BLOCK_WIDTH + PLAYFIELD_COORD_Y
            sprites.append(draw_square(x, y, self.batch, self.tetrion.color))

        return sprites

    def check_next_tetromino(self):
        next_tetromino = False

        if (self.tetrion.is_collision(self.tetromino, [0, -1])):
            self.tetrion.add_squares(self.tetromino.get_position())
            next_tetromino = True

        return next_tetromino

    def end_game(self):
        self.game_over_label = pyglet.text.Label(font_name="Tahoma", font_size=30, x = 500, y=400, batch=self.batch)
        self.game_over_label.text = "GAME OVER"
        pyglet.clock.schedule_interval(self.auto_lower_tt, 0)



    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.LEFT:
            if (self.tetrion.is_collision(self.tetromino, [-1, 0])):
                return
            self.tetromino.go_left()
        elif symbol == pyglet.window.key.RIGHT:
            if (self.tetrion.is_collision(self.tetromino, [1, 0])):
                return
            self.tetromino.go_right()
        elif symbol == pyglet.window.key.DOWN:
            while self.lower_tt():
                pass
        elif symbol == pyglet.window.key.S or symbol == pyglet.window.key.UP:
            if (self.tetrion.is_collision(self.tetromino, [0, -1])):
                return
            self.tetromino.rotate_clockwise()
        elif symbol == pyglet.window.key.A:
            if (self.tetrion.is_collision(self.tetromino, [0, -1])):
                return
            self.tetromino.rotate_anticlockwise()

    def on_draw(self):
        self.clear() 
        
        self.debug1.text = "X: %d" % self.tetromino.pos_x
        self.debug2.text = "Y: %d" % self.tetromino.pos_y
        self.batch.draw()

tetris = Tetris(caption="TETRIS", height=900, width=800)
pyglet.app.run()