import itertools
from tabulate import tabulate

#como se puede ver, usé parte del código del punto 2b, así puedo verificar rapidamente las dependencias funcionales
#Lo que se hace aquí es hacer todos los subconjuntos posibles de una lista (usando la libreria itertools)
def subconjuntos(conjunto):
    M = []
    for i in range(0,len(conjunto)+1):
        for subconjunto in itertools.combinations(conjunto,i):
            M.append(list(subconjunto))
    #El detalle de este return es para que no retorne la lista vacia
    return M[1:]

def esDependenciaFuncional(diccionario,dependenciaizquierda,dependenciaderecha): #funcion dependencia funcional del compañero modificada levemente para devolver un booleano
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
    #se mira si es completa o no primero chequeando si es compuesto o no
    if VerdadDependenciaFuncional != 0:
        return True
    else:
        return False

#funcion que determina las claves candidatas y devuelve una lista con estas
def clavesCandidatas(claves, relacion):
    candidatas = []
    for atributo in claves:
        if len(atributo) == 1: #si la posible clave es un solo atributo revisamos cuantas veces se repite cada valor, si algún valor no nulo se repite más de una vez entonces no es una clave candidata
            for valor in relacion[atributo[0]]:
                candidata = True
                if relacion[atributo[0]].count(valor) > 1 and relacion[atributo[0]] != "NULL":
                    candidata = False
                    break
            if candidata:
                candidatas.append(atributo)
        elif len(atributo) > 1: #si es un atributo compuesto primero reviso la irreducibilidad de este
            componentes = subconjuntos(atributo)
            irreducible = True
            for componente in componentes[:-1]:
                if componente in candidatas:
                    irreducible = False
            if irreducible: #si es irreducible entonces mediante varias iteraciones guardo las tuplas
                tuplas = []
                for i in range(len(relacion[atributo[0]])): #itero en el numero maximo de valores
                    tupla = []
                    for j in range(len(atributo)): #itero en el número de atributos que lo componen
                        tupla.append(relacion[atributo[j]][i]) #con esas iteraciones agrego cada valor a un tupla patra luego agregar esta ultima a una lista de tuplas
                    tuplas.append(tupla)
                for tupla in tuplas: #por ultimo reviso que si alguna tupla se repite para determinar si es o no clave candidata
                    candidata = True
                    if tuplas.count(tupla)>1:
                        candidata = False
                        break
                if candidata:
                    candidatas.append(atributo)
    return candidatas

def parteA():
    #Segunda claridad: si quiere introducir que no hay un dato (NULL) por favor escribalo de la misma forma siempre que lo vaya a realizar. Si escribe NULL siempre debe ser NULL, si pone 0 pues siempre debe ser 0.
    #El diccionario que va a contener cada atributo con sus valores. Preferí hacerlo un diccionario para al nada más llamar el atributo poder acceder a todos sus valores (facilidad).
    #El diccionario que va a contener cada atributo con sus valores. Preferí hacerlo un diccionario para al nada más llamar el atributo poder acceder a todos sus valores (facilidad).
    relacion = {}
    #Ahora solo ando pidiendo la cabecera (Los atributos van separados por espacios).
    #Ej para introducir: Codigo Usuario Tipodesangre
    print("Punto 2A (Comprobacion de BCNF)")
    print("Digite la cabecera de la tabla por favor (separados por espacio)")
    atributos = input()
    listaAtributos = atributos.split()
    #Ahora vamos a introducir cada valor que contiene dicho atributo, también se va separa por espacio:
    #Ej: 13 22 55 330 0
    print("Ahora introduzca los valores por cada atributo: (los datos de cada columna)")
    #El for es para que introduzca x veces según la cantidad de x atributos
    for i in range(0,len(listaAtributos)):
        print("Atributo " + listaAtributos[i] + ": (separados por espacio)")
        valores = input()
        listaValores = valores.split()
        relacion.update({listaAtributos[i]: listaValores})
    #Dibujar una tabla bonita
    Valores = []
    Nombres = []
    #Recorro todo el diccionario para obtener los atributos
    for key in relacion:
        Nombres.append(key)
    #Ahora los valores de cada atributo
    for i in range(0,len(relacion.get(Nombres[0]))):
        Valor = []
        for key in relacion:
            Valor.append(relacion[key][i])
        Valores.append(Valor)
    print(tabulate(Valores,headers = Nombres))
    #Ahora armare todos los subconjuntos posibles de atributos para tener en cuenta la posibilidad de claves candidatas compuestas
    rKeys = [key for key in relacion] #lista para guardar los atributos
    pClaves = subconjuntos(rKeys) #posibles claves candidatas (subconjuntos de la cabecera)
    candidatas = clavesCandidatas(pClaves, relacion) #determino las claves candidatas
    stringCandidatas = "Claves candidatas: "
    for clave in candidatas: #este for genera la string que al final indica las claves candidatas
        stringCandidatas += "{"
        for i in range(len(clave)):
            stringCandidatas += clave[i]
            stringCandidatas += ", "
        stringCandidatas = stringCandidatas[:-2] + "}"
    determinantes = [] #lista para guardar los determinantes
    for atributo in pClaves: #recorro cada atributo posible que se puede componer
        for atributo1 in pClaves: #recorro por segunda vez para comprobar dependencias funcionales
            if atributo != atributo1:
                dependencia = esDependenciaFuncional(relacion,atributo,atributo1)
                #en esta parte comprobamos que la dependencia funcional es completa con lógica usada en el ejercicio 2B
                if dependencia and len(atributo) < 2:
                    dependencia = True
                else:
                    #Se realiza todos los subconjuntos posibles de la parte izquierda, esto para definir si alguno tiene una dependencia funcional con el lado derecho(así no sería completa)
                    Subconjunto = subconjuntos(atributo)
                    for i in range(0,len(Subconjunto)):
                        if esDependenciaFuncional(relacion, Subconjunto[i], atributo1):
                            dependencia = False
                if dependencia and (atributo not in determinantes): # si hay una depencia funcional completa y no está este atributo ya en la lista (para evitar repetir) agregar el atributo a la lista de determinantes
                    determinantes.append(atributo)
    stringDeterminantes = "Determinantes: "
    for determinante in determinantes: #este for genera la string que al final indica los determinantes
        stringDeterminantes += "{"
        for i in range(len(determinante)): 
            stringDeterminantes += determinante[i]
        stringDeterminantes += ", "
        stringDeterminantes = stringDeterminantes[:-2] + "}"
    esBCNF = True #defino un booleano que define si la relacion es BCNF o no, inicializandolo en True
    for determinante in determinantes: #itero en los determinantes para comprobar si son claves candidatas o no
        if determinante not in candidatas:
            esBCNF = False #si alguno no está entonces ya no es BCNF
    #por último se comprueba el Booleano BCNF y se imprime el mensaje adecuado
    if esBCNF:
        print("La relación se encuentra en BCNF.") 
        print(stringCandidatas)
        print(stringDeterminantes)
    else:
        print("La relación NO se encuentra en BCNF.")
        print(stringCandidatas)
        print(stringDeterminantes)
