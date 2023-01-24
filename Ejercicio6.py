datos = []
mostrar = lambda x: x * 50
cursos = ("C2", "C1", "B2", "B1", "A2", "A1")
aux = 0

with open('Cursos.txt', 'r') as f:
    for linea in f:
        aux2 = 0
        if "C2" in linea:
            datos.extend(linea.split())
            aux = 10
        elif "C1" in linea:
            datos.extend(linea.split())
            aux = 9
        elif "B2" in linea:
            datos.extend(linea.split())
            aux = 8
            aux2 = 1
        elif "B1" in linea:
            datos.extend(linea.split())
            aux = 7
            aux2 = 2
        elif "A2" in linea:
            datos.extend(linea.split())
            aux = 6
            aux2 = 3
        elif "A1" in linea:
            datos.extend(linea.split())
            aux = 5
            aux2 = 4
        else:
            datos.extend(linea.split())
            aux = 4
            aux2 = 5
        if aux == 10:
            print(datos[0] + " tiene todos los cursos posibles")
        else:
            print(datos[0] + " tiene que pagar " + str(mostrar(aux)) + "€ por su siguiente curso que es el "+cursos[aux2])
        datos.clear()
