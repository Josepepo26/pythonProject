class ExceptDia(Exception):
    pass


class ExceptMes(Exception):
    pass


class ExceptAnio(Exception):
    pass


dia = 0
mes = 0
anio = 0
contador = 0
fech = ""
while fech != "x":
    fech = input("Escriba una fecha con formato dd/mm/aaaa (x para salir): ")
    if fech != "x":
        try:
            auxfech = fech.split("/")
            dia = int(auxfech[0])
            mes = int(auxfech[1])
            anio = int(auxfech[2])
            if dia < 1 or dia > 31:
                raise ExceptDia("El dia tiene que estar entre 1 y 31 incluidos")
            elif mes < 1 or mes > 12:
                raise ExceptMes("El mes tiene que estar entre 1 y 12 incluidos")
            elif anio < 1900 or anio > 2022:
                raise ExceptAnio("El año debe estar entre 1900 y 2022 incluidos")
            print(f"La fexha: {fech} cumple todos los requisitos")
        except ValueError as ex:
            print("La fecha no puede ser una letra")
        except ExceptDia as ex:
            print(ex)
        except ExceptAnio as ex:
            print(ex)
        except ExceptMes as ex:
            print(ex)
