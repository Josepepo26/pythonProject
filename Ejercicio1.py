import re


class ExceptNombre(Exception):
    pass
class ExceptContra(Exception):
    pass

rexNomb = re.compile("^[A-Za-z][A-Za-z0-9]{5,11}")
rexCont = re.compile("[^ ]{8,}")
nombre = None
contra = None
nomb = []
cont = []

while nombre != "0":
    try:
        nombre = input("Esciba el nombre (0 para salir): ")


        if nombre == "0":
            break
        elif not rexNomb.match(nombre):
            raise ExceptNombre("El nombre no puede contener caracteres, tiene que empezar por letra y tiene que tener entre 6-12")
        contra = input("Escribe la contraseña: ")
        if not rexCont.match(contra):
            raise ExceptContra("La contraseña tiene que tener mas de 8 caracteres")

    except ExceptNombre as ex:
        print(ex)
    except ExceptContra as ex:
        print(ex)
    else:
        #Añadimos el nombre y la contraseña a los arrays creados
        nomb.append(nombre)
        cont.append(contra)
#Recorremos con un for para mostrar por pantalla los usu con su respectiva contraseña
for i in range(len(nomb)):
    print(f'Nombre usuario: {nomb[i]} Contraseña: {cont[i]}')
