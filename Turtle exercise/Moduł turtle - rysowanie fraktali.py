# Moduł turtle - rysowanie fraktali

# skład sekcji:
# 1. inż. Paweł Boryszko ITS 2020

import turtle


def draw_side(x, angle):
    t.forward(x)
    t.left(angle)


def draw_simple_side(x):
    t.forward(x)


def draw_turn(angle):
    t.left(angle)


# Exercise 2
def draw_square(x):
    if x < 1:
        return
    else:
        draw_square(x * 0.9)
    # Exercise 1
    for _ in range(4):
        draw_side(x, 90)


def draw_triangle(x):
    for _ in range(3):
        draw_side(x, 120)


# Exercise 3
def draw_triangle_fractal(x):
    for _ in range(3):
        if x < 8:
            return
        else:
            draw_triangle_fractal(x/2)
        draw_triangle(x)
        draw_simple_side(2*x)
        draw_turn(120)


# Exercise 4 a
class YTreeFractal:
    def draw_trunk(self, x):
        t.forward(x)

    def reverse(self):
        t.left(180)

    def turn(self, angle):
        t.left(angle)

    def draw_y(self, x):
        self.draw_trunk(x)
        self.turn(30)
        self.draw_trunk(x)
        if x < 10:
            pass
        else:
            self.draw_y(x/2)
        self.reverse()
        self.draw_trunk(x)
        self.turn(120)
        self.draw_trunk(x)
        if x < 10:
            pass
        else:
            self.draw_y(x / 2)
        self.reverse()
        self.draw_trunk(x)
        self.turn(30)
        self.draw_trunk(x)
        self.reverse()

    def __init__(self):
        self.turn(90)
        self.draw_y(60)


# Exercise 4 b
class KochFlake:
    def draw(self, length):
        if length < 5:
            t.forward(length)
            return
        self.draw(length/3)
        t.left(60)
        self.draw(length/3)
        t.right(120)
        self.draw(length/3)
        t.left(60)
        self.draw(length/3)

    def draw_snowflake(self):
        for _ in range(3):
            self.draw(100)
            t.right(120)


t = turtle.Turtle()
t.speed("fastest")
# draw_square(100)
# draw_triangle_fractal(100)
elo = KochFlake()
elo.draw_snowflake()

turtle.Screen().exitonclick()
