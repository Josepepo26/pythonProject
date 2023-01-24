from builtins import ValueError


class ExceptLetra(Exception):
    pass
class ExceptLimite(Exception):
    pass

def mostrarporconsola():
    print("Nombre alumno: " + nombre)
    print("Notas:")
    for i in range(len(asig)):
        print(" -" + asig[i] + ": " + str(notas[i]))
    print("-------------------------------------------------------------------------")
    print("Asignaturas aprobadas: ")
    for i in range(len(asigaprov)):
        print(" -" + asigaprov[i] + "")
    print("-------------------------------------------------------------------------")
    print("Asignaturas suspendidas:")
    for i in range(len(asigsusp)):
        print(" -" + asigsusp[i])
    print("-------------------------------------------------------------------------0")
    print("Nota maxima: " + str(max(notas)))
    print("Nota minima: " + str(min(notas)))
def aniadiralfich():
    fichero = open("PrimeraEv.txt", 'w')
    fichero.write("Nombre alumno: " + nombre + "\n")
    fichero.write("Notas:\n")
    for i in range(len(asig)):
        fichero.write(" -" + asig[i] + ": " + str(notas[i]) + "\n")
    fichero.write("-------------------------------------------------------------------------\n")
    fichero.write("Asignaturas aprobadas: \n")
    for i in range(len(asigaprov)):
        fichero.write(" -" + asigaprov[i] + "\n")
    fichero.write("-------------------------------------------------------------------------\n")
    fichero.write("Asignaturas suspendidas: \n")
    for i in range(len(asigsusp)):
        fichero.write(" -" + asigsusp[i] + "\n")
    fichero.write("-------------------------------------------------------------------------\n")
    fichero.write("Nota maxima: " + str(max(notas)) + "\n")
    fichero.write("Nota minima: " + str(min(notas)) + "\n")
    fichero.close()

asig = ("Matemaricas", "Lengua", "Fisica y quimica", "Ingles", "Biologia")
notas = []
nombre=input("¿Cual es el nombre del alumno?")
i = 0
j = len(asig)
while i < j:
    try:
        nota=int(input("Nota de la asignatura "+asig[i]+":"))
        if nota>10 or nota<0:
            raise ExceptLimite("La nota debe estar entre 0 y 10")
        else:
            notas.append(nota)
            i=i+1
    except ValueError as ex:
        print("La nota no puede ser una letra")
    except ExceptLimite as ex:
        print(ex)
asigaprov = []
asigsusp = []
for i in range(len(asig)):
   if notas[i]>= 5:
       asigaprov.append(asig[i])
   else:
       asigsusp.append(asig[i])

mostrarporconsola()
aniadiralfich()





