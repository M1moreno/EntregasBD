import itertools
from tabulate import tabulate
from Parte1 import *
from Parte2A import *
from Parte2B import *

#Todo este código para adelante es una UI básica.
#Esta primera parte es para la parte inicial, para saber si el usuario quiere cerrar el programa o seguir

def verificarSalidaInicio():
    print("¿Quiere salir de la aplicación? (1: seguir en el programa, 0: cerrar el programa)")
    seleccion = int(input())
    if seleccion == 1:
        print("-----------------------------")
        switchInicial()
    elif seleccion == 0:
        quit()
#Este es para explicar el punto 1 (como debe digitar en el punto 1)
def ejemploUno():
    print("Se le solicita primero la longitud del grupo S1, entonces digita el tamaño del mismo en un número")
    print("Luego de ello se le va a pedir la parte de la dependencia izquierda y dependencia derecha según el elemento en donde esté")
    print("Por ejemplo: tenemos {AP -> BHW, BHW -> C}")
    print("Para introducir sería entonces primero:")
    print("Parte izquierda 1:")
    print(">> A P   (Esto es como lo debe introducir usted, introduce el grupo de atributos con un espacio)")
    print("Parte derecha 1:")
    print(">> B H W")
    print("Así sucesivamente con las dependencias funcionales del grupo 1.")
    print("Cuando ya haya finalizado el grupo 1 lo que debe hacer es hacer lo mismo con el grupo 2")
    print("Por ejemplo: {AP -> BHW, BHW -> C, AP -> C}")
    print("Parte izquierda 1:")
    print(">> A P")
    print("Parte derecha 1:")
    print(">>B H W")
    print("Notas:")
    print("1. No se introduce el '>>', esto solo se hizo para denotar que usted está introduciendo los datos")
    print("2. No se empieza con un espacio a la hora de introducir los datos, el espacio es meramente entre atributos")
#Explicacion del punto 2A
def ejemploDos():
    print("Se le solicitarán los atributos, se escriben con un espacio entre cada uno")
    print("Ejemplo:")
    print("Cedula Nombre")
    print("Luego de ello se le solicita los valores por cada atributo")
    print("Ejemplo por cedula:")
    print("12 23 76 (Se introdujeron los valores con un espacio entre ellos)")
    print("Se le piden los datos de los demás atributos también")
    print("Luego de eso ya se dan los resultados")
#Explicación del punto 2B
def ejemploTres():
    print("Se le solicita los datos como en el punto 2a.")
    print("Luego de introducir los datos vamos a ir a verificar las dependencias funcionales.")
    print("Le va a preguntar si quiere verificar o no, seleccione 1 si lo desea, 0 si no.")
    print("Este se basa en que primero va a pedir la parte izquierda, luego la derecha.")
    print("Ejemplo: {Código, Usuario -> Tipodesangre}")
    print("Parte izquierda:")
    print("Codigo Usuario (Similar a todas nuestras aplicaciones: con espacio entre los datos que introducimos)")
    print("Parte derecha:")
    print("Tipodesangre")
    print("Ya luego de introducir estos datos arroja el resultado deseado")
#UI para las explicaciones de los puntos
def switchEjemplos():
    print("1.Opcion 1")
    print("2.Opcion 2a")
    print("3.Opcion 2b")
    print("4.Volver al menú inicial")
    print("Digite la opción deseada")
    eleccion = int(input())
    if eleccion == 1:
        print("-----------------------------")
        ejemploUno()
        print("-----------------------------")
        switchEjemplos()
    elif eleccion == 2:
        print("-----------------------------")
        ejemploDos()
        print("-----------------------------")
        switchEjemplos()
    elif eleccion == 3:
        print("-----------------------------")
        ejemploTres()
        print("-----------------------------")
        switchEjemplos()
    elif eleccion == 4:
        print("-----------------------------")
        switchInicial()
    



#Este es el menú inicial. Puede elegir los puntos para ejecutarlos o elegir si quiere ver explicaciones o salirse del programa
def switchInicial():
    print("1.Opcion 1")
    print("2.Opcion 2a")
    print("3.Opcion 2b")
    print("4.Explicaciones de las opciones")
    print("5.Salir de la aplicación")
    print("Digite la opción a la cual quiere entrar")
    inicial = int(input())
    if inicial == 1:
        print("-----------------------------")
        A()
        print("-----------------------------")
        verificarSalidaInicio()
    elif inicial == 2:
        print("-----------------------------")
        parteA()
        print("-----------------------------")
        verificarSalidaInicio()
    elif inicial == 3:
        print("-----------------------------")
        ParteB()
        print("-----------------------------")
        verificarSalidaInicio()
        
    elif inicial == 5:
        quit()
    elif inicial == 4:
        print("-----------------------------")
        switchEjemplos()
#Llama a switchInicial para iniciar el programa
switchInicial()


