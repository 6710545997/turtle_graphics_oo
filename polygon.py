import turtle

class Polygon:
    def __init__(self, num_sides, size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = 0
        self.location = [0, 0]
        self.color = (0, 0, 0)
        self.border_size = 1
    
    def set_location(self, location):
        self.location = location
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])

    def set_orientation(self, orientation):
        self.orientation = orientation
        turtle.setheading(self.orientation)

    def set_color(self, color):
        self.color = color
        turtle.color(self.color)
    
    def set_pensize(self, border_size):
        self.border_size = border_size
        turtle.pensize(self.border_size)

    def draw(self):
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360/self.num_sides)
        turtle.penup()

class EmbeddedPolygon(Polygon):
    def __init__(self, num_sides, size, level):
        Polygon.__init__(self, num_sides, size)
        self.level = level
        self.reduction_ratio = 0.618

    def draw(self):
        Polygon.draw(self)
        for _ in range(self.level):
            # reposition the turtle and get a new location
            turtle.penup()
            turtle.forward(self.size*(1-self.reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(self.size*(1-self.reduction_ratio)/2)
            turtle.right(90)
            self.set_location([turtle.pos()[0], turtle.pos()[1]])
            
            # reduce the size by reduction_ratio
            self.size *= self.reduction_ratio
            Polygon.draw(self)
