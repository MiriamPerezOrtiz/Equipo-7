#Se crea un vector vacío donde se almacenará el texto que se quiere leer
texto = []

#Se extrae el texto del archivo deseado y lo convierte a una sola linea 
with open ("GEH.txt") as archivo:
    lines = archivo.readlines()
    texto = '\t'.join([line.strip() for line in lines])
    
#Convierte el texto a minúsculas para hacer un mejor conteo de la frecuencia de las palabras
lowtext = texto.lower()
#El comando split divide las palabras de cada oración en el texto. 
words = lowtext.split()

#Se crea un vector de () donde se guardará la frecuencia con la que se repite cada palabra del texto
fwords = {}

#Recorre en orden las palabras guardadas en el vector 'words' y cuenta las veces que está en el texto
for word in words:
    if word in fwords:
        fwords[word] += 1
    else:
        fwords[word] = 1

#Imprime la palabra y su frecuencia
for word in fwords:
    rep = fwords[word]
    print(f"{word} = {rep}")

#Genera un histograma donde se aprecia, a modo de gráfica, las frecuencias de las palabras
