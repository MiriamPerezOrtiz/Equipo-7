"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""
#Se importan los programas ubicados en la carpeta de este programa para
#poder utilizar sus recursos y evitar errores próximos.
from turtle import *

from freegames import vector

#Se define la función "line" que se encarga de dibujar una línea
#recta en la pantalla de inicio a fin con el clic del mouse.
def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

#Se define la función "square" que se encarga de dibujar cuatro líneas
#rectas en la pantalla de inicio a fin formando un cuadrado
#con el clic del mouse, cuando la figura esta completa, rellena el centro.
def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

#Se define la función "circle" que se encarga de dibujar una circulo
#en la pantalla con el radio establecido en el programa.
def circle(start, end):
    "Draw circle from start to end."
    t = turtle.Turtle()
    r = 50
    t.circle(r)
    pass

#Se define la función "rectangle" que se encarga de dibujar cuatro líneas
#rectas en la pantalla de inicio a fin formando un rectángulo
#con el clic del mouse, cuando la figura esta completa, rellena el centro.
def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward((end.x - start.x)/2)
        left(90)

    end_fill()

#Se define la función "triangle" que se encarga de dibujar tres líneas
#rectas en la pantalla de inicio a fin formando un triángulo
#con el clic del mouse, cuando la figura esta completa, rellena el centro.
def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()

#Se define la función "tap" que se encarga detectar los clics
#en pantalla para poder completar la figura deseada.
def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

#Se define la función "store" que almacena/guarda un valor en estado a clave.
def store(key, value):
    "Store value in state at key."
    state[key] = value

#Se inicializa el programa con las instrucciones dadas.
state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
"New color"
onkey(lambda: color('#72c6a6'), 'A')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
