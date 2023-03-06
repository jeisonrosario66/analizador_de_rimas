import os
from clearwindow import clearWindow
from funciones import *
clearWindow()

def mostrar_menu(opciones):
    print("\t\t:..Analizar Rimas..:\n")
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Mostrar letra (No dinamico)', accion1),
        '2': ('Opción 2', accion2),
        '3': ('Opción 3', accion3),
        '4': ('Limpiar pantalla', clear),
        '5': ('Salir', salir)
    }

    generar_menu(opciones, '5')


def accion1():
    clearWindow()
    print(f"\t\t:..Texto Modificado..:\n{versosTextoPlano}")


def accion2():
    print('Has elegido la opción 2')


def accion3():
    print('Has elegido la opción 3')


def salir():
    print('Saliendo')

def clear():
    clearWindow()


if __name__ == '__main__':
    menu_principal()