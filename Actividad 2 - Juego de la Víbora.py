#Se importan los programas ubicados en la carpeta de este programa para
#poder utilizar sus recursos y evitar errores próximos.
from turtle import *
from random import randrange
from freegames import square, vector

#Asignacion de valores a las variables que se ocupan proximamente en el programa.
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Elegir la velocidad de Snake.
v = 0

#Se define la función "inicio" que se encarga de pedirle al usuario la
#velocidad inicial del juego.
def inicio(velocidad):
    print("¡Bienvenido al Snake Game!")
    velocidad = input(
        "Elija la velocidad de Snake: Alto, Medio, Bajo.\nVelocidad: ")
    if velocidad.lower() == "alto":
        return 20
    elif velocidad.lower() == "medio":
        return 10
    elif velocidad.lower() == "bajo":
        return 5
    else:
        print("Elija una de las 3 opciones")
        inicio()
#Elegir la velocidad de Snake.

#Se define la función "change" que se encarga de cambiar las
#direcciones de la serpiente en la pantalla con el teclado.
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

#Se define la función "inside" que se encarga de terminar el
#juego si es que la cabeza de la serpiente se toca a sí mismo.
def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

#Se define la función "move" que se encarga de aumentar un cuadro cada
#que la serpiente toca un cuadro rojo.
def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return
#Se definden los límites de hasta donde puede moverse
#la serpiente dentro de la pantalla.
    if head.x == 190:
        change(-v, 0)
        head = snake[-1].copy()
        head.move(aim)

    if head.x == -200:
        change(v, 0)
        head = snake[-1].copy()
        head.move(aim)

    if head.y == -200:
        change(0, v)
        head = snake[-1].copy()
        head.move(aim)

    if head.y == 190:
        change(0, -v)
        head = snake[-1].copy()
        head.move(aim)

    snake.append(head)
#Cada que la sepierte toque el punto rojo, éste desaparecerá y
#aparecera en algun punto aleatorio dentro del rango dado.
    if head == food:
        print('Snake:', len(snake))
        food.x = random.randrange(0, 15, 2)
        food.y = random.randrange(0, 15, 7)
    else:
        snake.pop(0)

    clear()
#Se definen los parámetros iniciales para la serpiente y para
#el alimento.
    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

#Se define la función "tap" que se encarga de mover el alimento
#de forma aleatoria con el clic del mouse dentro del rango dado.
def tap(x,y):
    global food
    food.x = randrange(-13,13) * 6
    food.y = randrange(-13,13) * 6

#Se inicializa el programa.
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onscreenclick(tap)
v = inicio(v)
onkey(lambda: change(v, 0), 'Right')
onkey(lambda: change(-v, 0), 'Left')
onkey(lambda: change(0, v), 'Up')
onkey(lambda: change(0, -v), 'Down')
move()
done()
