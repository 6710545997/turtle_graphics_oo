import turtle
import random
import polygon

class PolygonArt:
    def __init__(self):
        self.art_list = []
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
    
    def insert_art(self, art_piece):
        self.art_list.append(art_piece)

    def run(self, art_id, num_iter):
        for i in range(num_iter):
            num_sides = self.art_list[art_id][0]()
            size = self.art_list[art_id][1]()
            if len(self.art_list[art_id]) <= 6:
                my_polygon = polygon.Polygon(num_sides, size)
            else:
                nesting_level = self.art_list[art_id][6]()
                my_polygon = polygon.EmbeddedPolygon(num_sides, size, nesting_level)
            orientation = self.art_list[art_id][2]()
            location = self.art_list[art_id][3]()
            color = self.art_list[art_id][4]()
            border_size = self.art_list[art_id][5]()
            my_polygon.set_orientation(orientation)
            my_polygon.set_location(location)
            my_polygon.set_color(color)
            my_polygon.set_pensize(border_size)
            my_polygon.draw()

        # hold the window; close it by clicking the window close 'x' mark
        turtle.done()
    
def get_new_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def get_new_location():
    return [random.randint(-300, 300), random.randint(-200, 200)]

my_portfolio = PolygonArt()
my_portfolio.insert_art([lambda: random.randint(3,3), # num_sides
                         lambda: random.randint(50, 150), # size
                         lambda: random.randint(0, 90), # orientation
                         lambda: get_new_location(), # location
                         lambda: get_new_color(), # color
                         lambda: random.randint(1, 10)]) # border_size
my_portfolio.insert_art([lambda: random.randint(4,4), # num_sides
                         lambda: random.randint(50, 150), # size
                         lambda: random.randint(0, 90), # orientation
                         lambda: get_new_location(), # location
                         lambda: get_new_color(), # color
                         lambda: random.randint(1, 10)]) # border_size
my_portfolio.insert_art([lambda: random.randint(5,5), # num_sides
                         lambda: random.randint(50, 150), # size
                         lambda: random.randint(0, 90), # orientation
                         lambda: get_new_location(), # location
                         lambda: get_new_color(), # color
                         lambda: random.randint(1, 10)]) # border_size
my_portfolio.insert_art([lambda: random.randint(3,5), # num_sides
                         lambda: random.randint(50, 150), # size
                         lambda: random.randint(0, 90), # orientation
                         lambda: get_new_location(), # location
                         lambda: get_new_color(), # color
                         lambda: random.randint(1, 10)]) # border_size
my_portfolio.insert_art([lambda: random.randint(3,3), # num_sides
                         lambda: random.randint(50, 150), # size
                         lambda: random.randint(0, 90), # orientation
                         lambda: get_new_location(), # location
                         lambda: get_new_color(), # color
                         lambda: random.randint(1, 10), # border_size
                         lambda: random.randint(2, 2)]) # nesting level
my_portfolio.insert_art([lambda: random.randint(4,4), # num_sides
                         lambda: random.randint(50, 150), # size
                         lambda: random.randint(0, 90), # orientation
                         lambda: get_new_location(), # location
                         lambda: get_new_color(), # color
                         lambda: random.randint(1, 10), # border_size
                         lambda: random.randint(2, 2)]) # nesting level
my_portfolio.insert_art([lambda: random.randint(5,5), # num_sides
                         lambda: random.randint(50, 150), # size
                         lambda: random.randint(0, 90), # orientation
                         lambda: get_new_location(), # location
                         lambda: get_new_color(), # color
                         lambda: random.randint(1, 10), # border_size
                         lambda: random.randint(2, 2)]) # nesting level
my_portfolio.insert_art([lambda: random.randint(3,5), # num_sides
                         lambda: random.randint(50, 150), # size
                         lambda: random.randint(0, 90), # orientation
                         lambda: get_new_location(), # location
                         lambda: get_new_color(), # color
                         lambda: random.randint(1, 10), # border_size
                         lambda: random.randint(2, 2)]) # nesting level
my_portfolio.insert_art([lambda: random.randint(3,5), # num_sides
                         lambda: random.randint(50, 150), # size
                         lambda: random.randint(0, 90), # orientation
                         lambda: get_new_location(), # location
                         lambda: get_new_color(), # color
                         lambda: random.randint(1, 10), # border_size
                         lambda: random.randint(0, 3)]) # nesting level

art_id = int(input("Select art piece number: "))
my_portfolio.run(art_id-1, 30)
