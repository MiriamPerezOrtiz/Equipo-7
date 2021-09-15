texto = []

with open ("GEH.txt") as archivo:
    lines = archivo.readlines()
    texto = '\t'.join([line.strip() for line in lines])

lowtext = texto.lower()
words = lowtext.split()

fwords = {}

for word in words:
    if word in fwords:
        fwords[word] += 1
    else:
        fwords[word] = 1
        
for word in fwords:
    rep = fwords[word]
    print(f"{word} = {rep}")
