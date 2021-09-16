#Un import sirve para invocar un módulo/programa ubicado en la misma carpeta
#de este programa y utilizar sus recursos

#El import de HCRfinal trae el programa que soluciona el acertijo
import HCRfinal
#El import de pygame hace posible es usode recursos animados
import pygame

#Se define la función "redrawGameWindow" que se encarga de establecer el tamaño
# y posición de la ventana donde se reproducirá la animación
def redrawGameWindow(Dir, p1, p2):
    global x, y, Side_A, Side_B
            
    win.blit(bg,(0,0))
    ypos = 300
    for item in Side_A:
        win.blit(item,(5,ypos))
        ypos = ypos - 60

    ypos = 300
    for item in Side_B:
        win.blit(item,(450,ypos))
        ypos = ypos - 60

    if p1 != 'Unknown':
        if right:
            win.blit(BoatRight,(x,y))
            win.blit(farmer,(x,y-50))
            if p2 != farmer:
                win.blit(p2,(x+50,y-50))           
        elif left:
            win.blit(BoatLeft,(x,y))
            win.blit(farmer,(x,y-50))
            if p2 != farmer:
                win.blit(p2,(x+50,y-50))            
    else:
        win.blit(char,(x, y))
    pygame.display.update()

#Se define la función "get_characters" que se encarga de obtener la imagen de los personajes que en
# en ese momento están seleccionados
def get_characters(d, p1, p2):
    if p2 == 'Zorro':
        character = fox
    elif p2 == 'Maiz':
        character = corn
    elif p2 == 'Ganzo':
        character = duck
    else:
        character = farmer
    return (d, farmer, character)

#Se define la función "Embark_characters" que toma la imagen de los personasjes y los sube al barco
def Embark_characters(B, p1, p2):
    if p1 in B:
        B.remove(p1)     
    if p2 in B:
        B.remove(p2)

#Se define la función "Dismbark_characters" que toma la imagen de los personasjes y los baja del barco
def Disembark_characters(A, p1, p2):
    if p1 not in A:
        A.append(p1)
    if p2 not in A:
        A.append(p2)

#Se define la función "HCR_animación" la cual integra las funciones anteriores y comienza la animación
#Se verá como el bote junto con el granjero tamará a los otros personajes para cambiarlos de lado
def HCR_animacion(P):
    global x, y, left, right, vel
    global Side_A, Side_B
#Se inicia un reloj que permitriá que la animación corra a cierta velociad para que se puede apreciar los cambios
    clock = pygame.time.Clock()
    run = True
    move = 0
    while run:
        clock.tick(27)
#Esta seccion comienza la animacion del transporte de los personajes de lado a lado        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            left = True
            right = False
            if move < len(P):
                direction, p1, p2 = get_characters(P[move], P[move + 1], P[move + 2])
                Embark_characters(Side_B, p1, p2)
                for step in range(65):
                    x -= vel
                    redrawGameWindow(direction, p1, p2)
                    pygame.time.delay(70)
                move += 3
                Disembark_characters(Side_A, p1, p2)

        elif keys[pygame.K_RIGHT]:
            right = True
            left = False
            if move < len(P):
                direction, p1, p2 = get_characters(P[move], P[move + 1], P[move + 2])
                Embark_characters(Side_A, p1, p2)
                for step in range(65):
                    x += vel
                    redrawGameWindow(direction, p1, p2)
                    pygame.time.delay(70)
                move += 3
                Disembark_characters(Side_B, p1, p2)
        else:
            redrawGameWindow ('Standby','Unknown', 'Unknown')
#Una vez que la solución se haya realizado, la animación se termina
    pygame.quit()

#Se define la función "Busca_solucion" que recupera el código de "HCRfinal" para buscar la solucion del acertijo
#y devolver una respuesta, la cual se mostrará en la animación
def Busca_solucion():
    P = HCRfinal.HCR()
    while len(P) > 22:
    #while len(P) > 42:
        HCRfinal.reiniciar_sistema()
        print ('\nBuscando una mejor solución, Longitud del Path', len(P))
        P = HCRfinal.HCR()
    print (P)
    print (len(P))
    print ('\n =====> Solución encontrada:')
    return (P)

#Se inicializa la busqueda de la solucion del acertijo            
P = Busca_solucion()
print ('Aquí su animación')

#Asignacion de valores a las variables que se ocupan en el programa
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("How to Cross the River")

BoatRight   = pygame.image.load('BoteRight.png')
BoatLeft    = pygame.image.load('BoteLeft.png')
bg          = pygame.image.load('seaL.png')
char        = pygame.image.load('BoteRight.png')
fox         = pygame.image.load('fox.png')
corn        = pygame.image.load('corn.png')
duck        = pygame.image.load('duck.png')
farmer      = pygame.image.load('farmer.png')
x       = 10
y       = 425
vel     = 5
left    = False
right   = False

#Inicialización del sistema
Side_A = [farmer, fox, duck, corn]
Side_B = []

#Se inicia la animación
HCR_animacion(P)




