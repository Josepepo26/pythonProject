# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

lista=[]
cifra = 100

while cifra != 0:
     try:
         cifra = input("Teclea cifra (0 para terminar)")
         cifra = int(cifra)
         print("Has tecleado la cifra: "+str(cifra))
         if cifra != 0:
             lista.append(cifra)

     except ValueError:
            print("Esto no es un numero")
print(lista)