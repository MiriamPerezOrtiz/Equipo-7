
import random
#Creacion de vectores tipo string 
Lado_A = ['Granjero', 'Zorro', 'Ganzo', 'Maiz']
Lado_B = []
Path = []

#Se define la función 'seleccion' que selecciona al azar un personaje del Lado A
def seleccion(L):
    op = random.randint(0,len(L)-1)
    return (L[op])

#Se define la función 'Viaje' la cual le asigna al Granjero el personaje que llevara al Lado B
def Viaje(F, D):
    p1 = seleccion(F)
    #print ('Selección -> ', p1)
    if p1 != 'Granjero':
        F.remove(p1)
        D.append(p1)

    F.remove('Granjero')
    D.append('Granjero')

    #print (F)
    #print (D)
    return ('Granjero',p1)

#Se define la función "valida_estado" que se encarga de validar que los personajes no elegidos
#puedan quedarse del mismo lado
def valida_estado(L):
    if 'Maiz' in L and 'Ganzo' in L and len(L) == 2:
        return False
    elif 'Zorro' in L and 'Ganzo' in L and len(L) == 2:
        return False
    return True

#Se define la función "reiniciar_sistema" que reestablece el juego para iniciar
#una nueva combinacion para buscar la solución más adecuada
def reiniciar_sistema():
    global Lado_A, Lado_B, Path
    
    Lado_A = ['Granjero', 'Zorro', 'Ganzo', 'Maiz']
    Lado_B = []
    Path = []
    
#Se define la función "HCR" la cual integra las funciones anteriores para realizar la búsqueda de
#la solución al acertijo
def HCR():
    F = Lado_A
    D = Lado_B
    while len(Lado_B) != 4:
        p1, p2 = Viaje(F, D)
        if valida_estado (F) and valida_estado (D):
            #print ('Estado valido, continuamos')
            if F == Lado_A:
                Path.append('A->B :')
            else:
                Path.append('B->A :')
            Path.append(p1)
            Path.append(p2)
            
            Temp = F
            F = D
            D = Temp      
        else:
            #print ('Estado inválido, REINICIO DEL SISTEMA')
            reiniciar_sistema()
            F = Lado_A
            D = Lado_B
    return (Path)

#Se define la función "main" que recibe la longitud de la solucion anterior. Si esta es mayor a 22,
# se reinicia el sistema para buscar una solución más corta
#Finalmente se imprime la solución.
def main():
    P = HCR()
    while len(P) > 22:
        reiniciar_sistema()
        print ('\nBuscando una mejor solución, Longitud del Path', len(P))
        P = HCR()
    print (P)
    print (len(P))

#Se inicia el Programa
main()

  
