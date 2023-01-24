def crearFichero():
    try:
        fichero = open("Login.txt",'w')
        usuarios = ["Jorge;", "Manue;", "Pepito;", "Sierra;", "Inigo;"]
        contras = ["1234;", "abcd;","nolose;"]
        fichero.writelines(usuarios)
        fichero.writelines(contras)
        fichero.close()

    except Exception:
        print("Error")
def leerFichero(usu, contr) -> bool:
    contador = 0
    with open('Login.txt', 'r') as f:
        for linea in f:
            if usu in linea and contr in linea:
                contador=contador+1
    if contador == 1:
        return True
    else:
        return False

crearFichero()
resta = 3
while resta > 0:
    print("Quedan "+str(resta)+" intentos.")
    usu = input("Escribe el nombre de usuario\n")
    contr = input("Escriba la contraseña\n")
    if leerFichero(usu,contr)==True:
        print("El login ha sido correcto")
        print("Usuario: "+usu)
        print("Contraseña: "+contr)
        break
    else:
        print("Repita el login, los datos no coinciden con el fichero Login.")
    resta=resta-1