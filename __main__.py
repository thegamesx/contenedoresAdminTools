import os
from apiCalls import *


def newCont():
    os.system('cls')
    print("Ingresar nueva placa a la base de datos\n")
    name = input("Nombre: ")
    config = input("Nombre configuración (dejar vacio para default): ")
    password = input("Contraseña (dejar vacio para generar automaticamente): ")
    result = requestNewCont(name, config, password)
    # TODO: Imprimir todo el detalle como corresponde.
    print(result)
    pass


def mainMenu():
    os.system('cls')
    print("Menú principal\n")
    # TODO: Ver que otros comandos se necesitan
    print("1. Ingresar nueva placa a la base de datos.\n")
    notValid = True
    while notValid:
        seleccion = input()
        if len(seleccion) > 1 or len(seleccion) == 0:
            print("Ingresa una opción válida")
        else:
            notValid = False
    match seleccion:
        case "1":
            newCont()
        case _:
            return False


while True:
    mainMenu()
