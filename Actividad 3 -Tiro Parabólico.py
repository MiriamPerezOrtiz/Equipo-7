#Un import sirve para invocar un módulo/programa ubicado en la misma carpeta
#de este programa y utilizar sus recursos
from random import randrange
from turtle import *
from freegames import vector

#Asignacion de valores a las variables que se ocupan en el programa
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

#Se define la función "tap" que se encarga detectar los clics
#en pantalla para que la bola se lanzada en esa dirección.
def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x += (x + 200) / 25
        speed.y += (y + 200) / 25

#Se define la función "inside" que valida si xy (posición de la pelota)
#se encuentra en dentro de la ventana de animación
def inside(xy):
    return -200 < xy.x < 200 and -200 < xy.y < 200

#Se define la función "draw" que literalmente dibujará tanto la pelota y los círculos objetivos
def draw():
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(10, 'red')

    update()

#Se define la función "move" que se encargará de el movimiento de la pelota y los cículos objetivos
def move():
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

        for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed+10)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            x = randrange(-150, 150)
            y = randrange(-150, 150)
            target.x = x
            target.y = y

    ontimer(move, 50)

#Se inicializa el programa 
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
