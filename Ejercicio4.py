# Se crea un diccionario vacío
diccionario = {}

# Se pide al usuario que introduzca palabras en español y su traducción en inglés
while True:
    espanol = input("Introduce una palabra en español (o escribe 'salir' para finalizar): ")
    if espanol == "salir":
        break
    ingles = input("Introduce la traducción en inglés: ")
    diccionario[espanol] = ingles

# Se pide al usuario que introduzca una frase en español
frase = input("Introduce una frase en español para traducir: ")

# Se dividen las palabras de la frase
palabras = frase.split()

# Se recorren las palabras de la frase
traduccion = []
for palabra in palabras:
    if palabra in diccionario:
        traduccion.append(diccionario[palabra])
    else:
        traduccion.append(palabra)

# Se imprime la frase traducida
print("Traducción: " + " ".join(traduccion))