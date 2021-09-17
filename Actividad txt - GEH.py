# Librerias utilizadas para la creacion de los histogramas
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Se crea un vector vacío donde se almacenará el texto que se quiere leer
texto = []

# Se extrae el texto del archivo deseado y lo convierte a una sola linea
with open("GEH.txt") as archivo:
    lines = archivo.readlines()
    texto = '\t'.join([line.strip() for line in lines])

# Convierte el texto a minúsculas para hacer un mejor conteo de la frecuencia de las palabras
lowtext = texto.lower()
# El comando split divide las palabras de cada oración en el texto.
words = lowtext.split()

# Se crea un vector de () donde se guardará la frecuencia con la que se repite cada palabra del texto
fwords = {}

# Recorre en orden las palabras guardadas en el vector 'words' y cuenta las veces que está en el texto
for word in words:
    if word in fwords:
        fwords[word] += 1
    else:
        fwords[word] = 1


palabras = []  # Lista de palabras
repeticiones = []  # Lista del numero de repetciones

for word in fwords:
    rep = fwords[word]
    palabras.append(word)  # Agrega las palabras a la lista de palabras
    # Agrega el numero de repeticiones a la lista de repeticiones
    repeticiones.append(rep)
    print(f"{word} = {rep}")  # Imprime la palabra y su frecuencia


# Genera un histograma donde se aprecia, a modo de gráfica, las frecuencias de las palabras divididas por rangos
fig, ax = plt.subplots()
ax.set_ylabel('Repeticiones')
ax.set_title('Cantidad de repeticiones por palabra')
plt.bar(palabras[:10], repeticiones[:10])
plt.show()

fig, ax = plt.subplots()
ax.set_ylabel('Repeticiones')
ax.set_title('Cantidad de repeticiones por palabra')
plt.bar(palabras[10:20], repeticiones[10:20])
plt.show()

fig, ax = plt.subplots()
ax.set_ylabel('Repeticiones')
ax.set_title('Cantidad de repeticiones por palabra')
plt.bar(palabras[20:30], repeticiones[20:30])
plt.show()

fig, ax = plt.subplots()
ax.set_ylabel('Repeticiones')
ax.set_title('Cantidad de repeticiones por palabra')
plt.bar(palabras[30:40], repeticiones[30:40])
plt.show()

fig, ax = plt.subplots()
ax.set_ylabel('Repeticiones')
ax.set_title('Cantidad de repeticiones por palabra')
plt.bar(palabras[40:50], repeticiones[40:50])
plt.show()
