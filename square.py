import pyglet

SQUARE_SIDE = 20

class Square(pyglet.shapes.Rectangle):
    def __init__(self, x, y, batch):
        pyglet.shapes.Rectangle.__init__(self, x, y, SQUARE_SIDE, SQUARE_SIDE, color=RED[0], batch=batch)



def draw_square(x, y, batch, color):
    square = pyglet.shapes.Rectangle(x, y, SQUARE_SIDE, SQUARE_SIDE, color=color[0], batch=batch) 

    left_vertical_line_x = x + 2
    left_vertical_line_y_bottom = y
    left_vertical_line_y_top = y + SQUARE_SIDE
    
    right_vertical_line_x = x + SQUARE_SIDE - 1
    right_vertical_line_y_bottom = left_vertical_line_y_bottom
    right_vertical_line_y_top = left_vertical_line_y_top

    bottom_horizontal_line_y = y + 2
    bottom_horizontal_line_x_left = x
    bottom_horizontal_line_x_right = x + SQUARE_SIDE

    top_horizontal_line_y = y + SQUARE_SIDE - 1
    top_horizontal_line_x_left = bottom_horizontal_line_x_left
    top_horizontal_line_x_right = bottom_horizontal_line_x_right

    line1 = pyglet.shapes.Line(
        top_horizontal_line_x_left, 
        top_horizontal_line_y, 
        top_horizontal_line_x_right, 
        top_horizontal_line_y, 
        width=3, color=(color[1]), batch=batch)

    line2 = pyglet.shapes.Line(
        left_vertical_line_x, 
        left_vertical_line_y_bottom, 
        left_vertical_line_x, 
        left_vertical_line_y_top, 
        width=3, color=(color[2]), batch=batch)

    line3 = pyglet.shapes.Line(
        bottom_horizontal_line_x_left, 
        bottom_horizontal_line_y, 
        bottom_horizontal_line_x_right, 
        bottom_horizontal_line_y, 
        width=3, color=(color[3]), batch=batch)

    line4 = pyglet.shapes.Line(
        right_vertical_line_x, 
        right_vertical_line_y_bottom, 
        right_vertical_line_x, 
        right_vertical_line_y_top, 
        width=3, color=(color[4]), batch=batch)

    return square, line1, line2, line3, line4
