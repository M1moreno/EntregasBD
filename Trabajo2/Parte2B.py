import itertools
from tabulate import tabulate
#Toca hacer pip install tabulate en su consola (cmd)
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
    #Creamos dos listas, una para el lado izquierdo y otro para el lado derecho. ¿Pero a qué me refiero? Me refiero a todos los conjuntos de atributos según el lado de la dependencia funcional
    #Ejemplo: nos dicen que el lado izquierdo es Codigo, entonces la izquierda serian los valores del atributo Codigo QUE NO ESTÉN REPETIDOS
    Izquierda = []
    Derecha = []
    #Empiezo suponiendo que es una dependencia funcional
    VerdadDependenciaFuncional = 1
    #Este for toma la longitud de la primera columna, para poder recorrer todos los datos(La primera por si nada más pone el usuario 1)

    for i in range(0,len(diccionario.get(dependenciaizquierda[0]))):
        #Este if más que todo es para que en caso de que sea 0 no toque recorrer otra vez toda la función
        if VerdadDependenciaFuncional == 1:
                #Ahora vamos a crear dos listas del conjunto de los valores de cada conjunto de atributos según la tabla

                izquierda1 = []
                derecha1 = []
                #Filas (Tuplas)
                #Append (agregar) del dato según en la fila que esté.
                for j in range(0,len(dependenciaizquierda)):
                    izquierda1.append(diccionario.get(dependenciaizquierda[j])[i])
                for j in range(0,len(dependenciaderecha)):
                    derecha1.append(diccionario.get(dependenciaderecha[j])[i])
                #Si tenemos ese conjunto de valores en nuestra lista izquierda tenemos que checkear que en esa misma posición la derecha tenga el mismo valor que el presentado en el actual de la tabla.
                #Como es complicado de explicar tengamos un ejemplo a la mano:
                # Tenemos la dependencia funcional Tipodesangre -> codigo, entonces sabemos que existen un conjunto de valores para ellos.
                #[[A -> 12],..., [A -> 76]], lo que hace es que al ver que A está en la lista va a comparar 12 con el 76 (el que está ahora mismo), en caso de que sean diferentes pues no es dependencia funcional (y realmente no lo son). (Las listas de este ejemplo no son representadas así en el código, es meramente para explicar de una mejor manera).
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
    #Quiero dejar aquí algo muy claro desde el principio: se usó la palabra nombres para referirse a los atributos para poder relacionar mejor las variables que ando creando (ya que un atributo en POO se refiere a algo distinto en BD, es simplemente por mero convenio personal que hice eso).
    #Segunda claridad: si quiere introducir que no hay un dato (NULL) por favor escribalo de la misma forma siempre que lo vaya a realizar. Si escribe NULL siempre debe ser NULL, si pone 0 pues siempre debe ser 0.
    #El diccionario que va a contener cada atributo con sus valores. Preferí hacerlo un diccionario para al nada más llamar el atributo poder acceder a todos sus valores (facilidad)

    diccionarioCabecera = {}
    #Ahora solo ando pidiendo la cabecera (Los atributos van separados por espacios).
    #Ej para introducir: Codigo Usuario Tipodesangre
    print("Se presentará a continuación el punto 2B ")
    print("Digite la cabecera de la tabla por favor (separados por espacio)")
    nombres = input()
    listaNombres = nombres.split()
    #Ahora vamos a introducir cada valor que contiene dicho atributo, también se va separa por espacio:
    #Ej: 13 22 55 330 0
    print("Ahora introduzca los valores por cada atributo: (los datos de cada columna) ")
    #El for es justamente por eso, para que introduzca x veces según la cantidad de x atributos
    for i in range(0,len(listaNombres)):
        print("Atributo " + listaNombres[i] + ": (separados por espacio)")
        ejemplos = input()
        listaEjemplos = ejemplos.split()
        diccionarioCabecera.update({listaNombres[i]: listaEjemplos})
    #Dibujar una tabla bonita
    Valores = []
    Nombres = []
    #Recorro todo el diccionario para obtener los atributos
    for key in diccionarioCabecera:
        Nombres.append(key)
    #Ahora los valores de cada atributo
    for i in range(0,len(diccionarioCabecera.get(Nombres[0]))):
        Valor = []
        for key in diccionarioCabecera:
            Valor.append(diccionarioCabecera[key][i])
        Valores.append(Valor)
    print(tabulate(Valores,headers = Nombres))
    print("Ahora es momento de verificar las dependencias funcionales")
    #Funcionar 1 o 0. Si es 1 entonces puede entrar a verificar, sino pues se deja de ejecutar el programa.
    Funcionar = int(input("¿Quiere verificar las dependencias funcionales? (1 si quiere seguir, 0 si no)"))
    Repeticion = 0
    while Funcionar == 1:
        #Va a imprimir la repetición x
        print("Verificación de la dependencia funcional número " + str(Repeticion))
        #Ahora vamos a verificar las dependencias. Primero el lado izquierdo de la dependencia.
        print("Introduzca los atributos del lado izquierdo (separados por espacio)")
        izquierda = input()
        dependenciaIzquierda = izquierda.split()
        #Ahora el lado derecho
        print("Introduzca los atributos del lado derecho (separados por espacio)")
        derecha = input()
        dependenciaDerecha = derecha.split()
        while len(dependenciaIzquierda) > 4 or len(dependenciaDerecha) >4:
            print("Introdujo más datos de los que se acordaron, por favor vuelva a introducir los datos")
            print("Introduzca los atributos del lado izquierdo")
            izquierda = input()
            dependenciaIzquierda = izquierda.split()
            print("Introduzca los atributos del lado derecho")
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
                #Se realiza todos los subconjuntos posibles de la parte izquierda, esto para definir si alguno tiene una dependencia funcional con el lado derecho(así no sería completa)

                Subconjunto = subconjuntos(dependenciaIzquierda)
                for i in range(0,len(Subconjunto)):
                    if esDependenciaFuncional(diccionarioCabecera, Subconjunto[i], dependenciaDerecha) == 1:
                        VerdadDependenciaCompleta = 0
                #Ya luego de verificar entonces imprimimos lo adecuado.
                if VerdadDependenciaCompleta != 0:
                    print("La dependencia que acaba de ingresar se cumple en la muestra y es completa.")
                else:
                    print("La dependencia que acaba de ingresar se cumple en la muestra y es incompleta.")
        Funcionar = int(input("¿Quiere seguir con la verificación de dependencias funcionales? (1 si quiere seguir, 0 si no)"))
        if Funcionar == 0:
            print("¡Hasta pronto!")
        Repeticion = Repeticion + 1
