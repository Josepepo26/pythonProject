import re
from collections import defaultdict

comp = re.compile(" ")


def leerFichero():
    streetno = defaultdict(list)
    with open('Natalidad_2021.txt') as f:
        for linea in f:
            div = lambda linea:  linea.rstrip("\n").split(" ")
            data = list(div(linea))
            provincias = data.pop(0)
            streetno[provincias].append(data)
    return streetno
def ordenar(lista):
    orde = str({key: value for key, value in sorted(lista.items(), key = lambda item: item[1])})
    sep = orde.split(",")
    return sep
prov = leerFichero()
asd = ordenar(prov)
for i in range(len(asd)):
    print(asd[i])