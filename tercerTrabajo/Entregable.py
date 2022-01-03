from Uno import *
from Dos import *
from tabulate import tabulate
#Quiero dar una aclaración: si usted está viendo que esta interfaz es similar al del anterior trabajo
#le quiero decir que tiene toda la razón, se está empleando la base de la anterior interfaz para 
#esta interfaz. 

#Interfaz para volver al inicio desde el punto 1 o 2
def verificarSalidaInicio():
    print("¿Quiere salir de la aplicación? (1: seguir en el programa, 0: cerrar el programa)")
    seleccion = int(input())
    if seleccion == 1:
        print("-----------------------------")
        switchInicial()
    elif seleccion == 0:
        quit()

def ejemploUno():
    print("Se le pedirá los atributos de la primera relación (separados por espacio)")
    print("Ej:")
    print("a b c d")
    print("Luego de ello se le pedirá los valores que tiene cada atributo (se le pide los datos por cada columna, también separados por un espacio)")
    print("Ej:")
    print("Atributo a (separados por un espacio)")
    print(">> 1 2 8 (NO SE INTRODUCE EL '>>', ESTO ES SOLO UN SIMBOLO REPRESENTADO LO QUE INTRODUCE EL USUARIO)" )
    print("Luego de ello se le hace lo mismo con la relación 2, al final entregará el resultado de R1 LEFT NATURAL OUTER JOIN R2")
def ejemploDos():
    print("Usted introduce los atributos con sus respectivos valores como se hizo en el PUNTO 1, no me detendré en las explicaciones por ser similar ")
    print("Luego de crear la tabla el programa le solicitará la lista de atributos con la cual va a realizar agrupamiento, también deben estar separados por un espacio estos atributos")
    print("Ej:")
    print("Papa Yuca Wakanda")
    print("Luego de esto se solicita la CANTIDAD de agregados en la lista de agregados.")
    print("Ej: para SUM: 'salario, AVG: comision, COUNT: cc, CONCATENATE: nombre' son 4 , entonces usted pone 4 cuando se le solicite ello")
    print(">>4")
    print("Luego de adjuntar la cantidad de agregados se le solicitará x veces (siendo x la cantidad de agregados) la función de grupo, luego de ello su respectivo atributo. (Así sucesivamente)")
    print("Ej: >>SUM")
    print(">>salario")
    print(">>AVG")
    print("comision")
    print(">>COUNT")
    print(">>cc")
    print(">>CONCATENATE")
    print("nombre")
def switchEjemplos():
    print("1.Opcion 1")
    print("2.Opcion 2")
    print("3.Volver al menú inicial")
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
        switchInicial()
#Interfaz inicial
def switchInicial():
    print("Seleccione el punto a evaluar")
    print("1.Opcion 1") #Punto 1
    print("2.Opcion 2") #Punto 2
    print("3.Explicaciones de las opciones") #Ejemplos de los puntos para que el usuario comprenda como usar esto
    print("4.Salir de la aplicación") #Es demasiado autodescriptivo 
    print("Digite la opción a la cual quiere entrar")
    inicial = int(input())
    if inicial == 1: #Punto 1
        print("-----------------------------")
        uno() #La función del punto 1
        print("-----------------------------")
        verificarSalidaInicio()
    elif inicial == 2: #Punto 2
        print("-----------------------------")
        dos() #La función del punto 2
        print("-----------------------------")
        verificarSalidaInicio()
    elif inicial == 4: #Pues se sale
        quit() #Me salgo
    elif inicial == 3: #En caso de que haya seleccionado ver los ejemplos
        print("-----------------------------")
        switchEjemplos()

switchInicial()