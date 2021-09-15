from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Elegir la velocidad de Snake
v = 0

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
# Elegir la velocidad de Snake



def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

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

    if head == food:
        print('Snake:', len(snake))
        #randomize()
        #food.x = random.randint(0, 1)
        #food.y = random.randint(0, 1)
        food.x = random.randrange(0, 15, 2)
        food.y = random.randrange(0, 15, 7)
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)
    
def tap(x,y):
    global food
    food.x = randrange(-13,13) * 6
    food.y = randrange(-13,13) * 6


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

