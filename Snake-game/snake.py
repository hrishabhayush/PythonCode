from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        length_turtle = Turtle("square")
        length_turtle.color("white")
        length_turtle.penup()
        length_turtle.goto(position)
        # First the turtle(length of the snake) is created at the center position of the coordinate and then moves to a different position.
        self.segments.append(length_turtle)

    def extend(self):
        '''Add a new segment to the last segment to the snake'''
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        for length_num in range(len(self.segments) - 1, 0, -1):
            # Looping through each segment starting with the last one.
            new_x = self.segments[length_num - 1].xcor()
            new_y = self.segments[length_num - 1].ycor()
            self.segments[length_num].goto(new_x, new_y)
        self.segments[0].forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



