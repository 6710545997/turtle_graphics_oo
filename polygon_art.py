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
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            border_size = random.randint(1, 10)
            if len(self.art_list[art_id]) <= 1:
                my_polygon = polygon.Polygon(num_sides, size, orientation, color, border_size)
            else:
                nesting_level = self.art_list[art_id][1]()
                my_polygon = polygon.EmbeddedPolygon(num_sides, size, orientation, color, border_size, nesting_level)
            my_polygon.set_location(location)
            my_polygon.draw()

        # hold the window; close it by clicking the window close 'x' mark
        turtle.done()

my_portfolio = PolygonArt()
my_portfolio.insert_art([lambda: random.randint(3,3)])
my_portfolio.insert_art([lambda: random.randint(4,4)])
my_portfolio.insert_art([lambda: random.randint(5,5)])
my_portfolio.insert_art([lambda: random.randint(3,5)])
my_portfolio.insert_art([lambda: random.randint(3,3), lambda: random.randint(2, 2)])
my_portfolio.insert_art([lambda: random.randint(4,4), lambda: random.randint(2, 2)])
my_portfolio.insert_art([lambda: random.randint(5,5), lambda: random.randint(2, 2)])
my_portfolio.insert_art([lambda: random.randint(3,5), lambda: random.randint(2, 2)])
my_portfolio.insert_art([lambda: random.randint(3,5), lambda: random.randint(0, 3)])

art_id = int(input("Select an art piece number: "))
my_portfolio.run(art_id-1, 30)
