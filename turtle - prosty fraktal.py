# Importowanie modułu i wywołanie konstruktora
import turtle
t = turtle.Turtle()

#Ustawianie prędkości poruszania się znacznika
t.speed("fastest")

#Definicja funkcji tworzącej fragment fraktala
def frac_widly(x):
    if x<=1:
        return
    t.left(90)
    t.forward(x)
    t.right(90)
    t.forward(x)
    frac_widly(x/3)
    #cofnij się
    t.backward(x)
    t.right(90)
    t.forward(x)
    #rysuj środkową część wideł (rys. 3)
    t.left(90)
    t.forward(x)
    frac_widly(x/3)
    #cofnij się
    t.backward(x)
    #rysuj prawą część wideł (rys. 4)
    t.right(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    frac_widly(x/3)
    #cofnij się do punktu początkowego i obróć się w kierunku początkowym (rys. 5)
    t.backward(x)
    t.left(90)
    t.forward(x)
    t.right(90)

# Wywołanie funkcji frac_widly
x = 64
t.forward(x)
frac_widly(x)

turtle.Screen().exitonclick()