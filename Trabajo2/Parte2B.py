import itertools
from tabulate import tabulate
#Toca hacer pip install tabulate
#Lo que se hace aquí es hacer todos los subconjuntos posibles de una lista (usando la libreria itertools)

def subconjuntos(conjunto):
    M = []
    for i in range(0,len(conjunto)+1):
        for subconjunto in itertools.combinations(conjunto,i):
            M.append(list(subconjunto))
    #El detalle de este return es para que no retorne ni la lista vacia ni el conjunto original (puesto de ese ya verificamos)

    return M[1:-1]
#Esta función es lo que hace en sí que funcione lo de dependencia funcional, para checkear si es o no es (0 no es, 1 sí es)

def esDependenciaFuncional(diccionario,dependenciaizquierda,dependenciaderecha):
    #Creamos dos listas, una para el lado izquierdo y otro para el lado derecho. ¿Pero a qué me refiero? Me refiero a todos los conjuntos de datos según el lado de la dependencia funcional
    #Ejemplo: nos dicen que el lado izquierdo es Codigo, entonces la izquierda serian los datos de la columna Codigo QUE NO ESTÉN REPETIDOS
    Izquierda = []
    Derecha = []
    #Empiezo suponiendo que es una dependencia funcional
    VerdadDependenciaFuncional = 1
    #Este for toma la longitud de la primera columna, para poder recorrer todos los datos(La primera por si nada más pone el usuario 1)

    for i in range(0,len(diccionario.get(dependenciaizquierda[0]))):
        #Este if más que todo es para que en caso de que sea 0 no toque recorrer otra vez toda la función
        if VerdadDependenciaFuncional == 1:
                #Ahora vamos a crear dos listas de los datos de cada nombre según la tabla

                izquierda1 = []
                derecha1 = []
                #Filas (Tuplas)
                #Append del dato según en la fila que esté.
                for j in range(0,len(dependenciaizquierda)):
                    izquierda1.append(diccionario.get(dependenciaizquierda[j])[i])
                for j in range(0,len(dependenciaderecha)):
                    derecha1.append(diccionario.get(dependenciaderecha[j])[i])
                #Si tenemos ese conjunto de datos en nuestra tabla izquierda tenemos que checkear que en esa misma posición la derecha tenga el mismo dato que el presentado en el actual de la tabla.
                #Como es complicado de explicar tengamos un ejemplo a la mano:
                # Tenemos la dependencia funcional Tipodesangre -> codigo, entonces sabemos que existen un conjunto de datos para ellos.
                #[[A -> 12],..., [A -> 76]], lo que hace es que al ver que A está en la lista va a comprar 12 con el 76 (el que está ahora mismo), en caso de que sean diferentes pues no es dependencia funcional (y realmente no lo son).

                if izquierda1 in Izquierda:
                    indice = Izquierda.index(izquierda1)
                    if Derecha[indice] != derecha1:
                        VerdadDependenciaFuncional = 0
                #En caso de que ese dato de izquierda no esté en Izquierda pues se agrega izquierda1 y derecha1 a Izquierda y Derecha respectivamente
                else: 
                    Izquierda.append(izquierda1)
                    Derecha.append(derecha1)
    return VerdadDependenciaFuncional


def ParteB():
    #El diccionario que va a contener el nombre de cada columna con sus datos. Preferí hacerlo un diccionario para al nada más llamar el nombre poder accerder a todos sus datos (facilidad)

    diccionarioCabecera = {}
    #Ahora solo ando pidiendo la cabecera (La cabecera va separada por espacios).
    #Ej para introducir: Codigo Usuario Tipodesangre
    print("Se presentará a continuación el punto 2B")
    print("Digite la cabecera por favor")
    nombres = input()
    listaNombres = nombres.split()
    #Ahora vamos a introducir cada valor que contiene dicha columna, también se va separa por espacio:
    #Ej: 13 22 55 330 0
    print("Ahora introduzca los atributos por cada nombre:")
    #El for es justamente por eso, para que introduzca x veces según la cantidad de x nombres
    for i in range(0,len(listaNombres)):
        print("Cabecera " + listaNombres[i] + ":")
        ejemplos = input()
        listaEjemplos = ejemplos.split()
        diccionarioCabecera.update({listaNombres[i]: listaEjemplos})
    #Dibujar una tabla bonita
    Valores = []
    Nombres = []
    #Recorro todo el diccionario para obtener los nombres de cada columna
    for key in diccionarioCabecera:
        Nombres.append(key)
    #Ahora los valores de cada columna según su nombre
    for i in range(0,len(diccionarioCabecera.get(Nombres[0]))):
        Valor = []
        for key in diccionarioCabecera:
            Valor.append(diccionarioCabecera[key][i])
        Valores.append(Valor)
    print(tabulate(Valores,headers = Nombres))
    print("Ahora es momento de verificar las dependencias funcionales")
    #Funcionar 1 o 0. Si es 1 entonces puede entrar a verificar, sino pues se deja de ejecutar el programa.
    Funcionar = int(input("¿Quiere verificar las dependencias funcionales?"))
    Repeticion = 0
    while Funcionar == 1:
        #Va a imprimir la repetición x
        print("Verificación de la dependencia funcional número " + str(Repeticion))
        #Ahora vamos a verificar las dependencias. Primero el lado izquierdo de la dependencia.
        print("Introduzca los nombres de los atributos del lado izquierdo")
        izquierda = input()
        dependenciaIzquierda = izquierda.split()
        #Ahora el lado derecho
        print("Introduzca los nombres de los atributos del lado derecho")
        derecha = input()
        dependenciaDerecha = derecha.split()
        #Ya tenemos ahora dos listas con los atributos que queremos
        #Ejemplo [Código,Usuario] -> [Tipo,Tipodesangre]
        
        ######
        #Ahora vamos a verificar la dependencia funcional, en específico si se cumple en la muestra
        #y si es completa o no
        #¿Recuerda la función de arriba? Pues la vamos a usar y vamos a asignar el valor de VerdadDependenciaFuncional al resultado.

        VerdadDependenciaFuncional = esDependenciaFuncional(diccionarioCabecera, dependenciaIzquierda, dependenciaDerecha)
        #Si es 0 pues no es dependencia funcional siquiera
        if VerdadDependenciaFuncional == 0:
            print("La dependencia que acaba de ingresar no se cumple en la muestra.")
        #En caso de que lo sea...
        else:
            #Suponemos en primera instancia que es completa
            VerdadDependenciaCompleta = 1
            #¿Por qué esto? Porque si es de tamaño = 1 pues no tiene subconjuntos siquiera, ya es dependencia funcional completa.
            if len(dependenciaIzquierda) < 2:
                print("La dependencia que acaba de ingresar se cumple en la muestra y es completa.")
            else:
                #Se realiza todos los subconjutos posibles de la parte izquierda, esto para definir si alguno tiene una dependencia funcional con el lado derecho(así no sería completa)

                Subconjunto = subconjuntos(dependenciaIzquierda)
                for i in range(0,len(Subconjunto)):
                    if esDependenciaFuncional(diccionarioCabecera, Subconjunto[i], dependenciaDerecha) == 1:
                        VerdadDependenciaCompleta = 0
                #Ya luego de verificar entonces imprimimos lo adecuado.
                if VerdadDependenciaCompleta != 0:
                    print("La dependencia que acaba de ingresar se cumple en la muestra y es completa.")
                else:
                    print("La dependencia que acaba de ingresar se cumple en la muestra y es incompleta.")
        Funcionar = int(input("¿Quiere seguir con la verificación de dependencias funcionales?"))
        if Funcionar == 0:
            print("¡Hasta pronto!")
        Repeticion = Repeticion + 1

ParteB()