from tabulate import tabulate 
#El nombre de la función dice demasiado de la misma: en caso de que no hayan atributos en común

def noHayRelacionados(tabla1,tabla2):
    #La tabla resultante
    tablaNueva = {}
    #Lista atributos tabla 1:
    atributosUno = list(tabla1.keys())
    #Lista atributos tabla 2:
    atributosDos = list(tabla2.keys())
    #Agregamos los atributos de la tabla 1
    for key in tabla1:
        tablaNueva.update({key:[]})
    #Agregamos los atributos de la tabla 2
    for key in tabla2:
        tablaNueva.update({key:[]})
    '''
    for i in range(0,len(tabla1[primeraKey])):
        #Como toca unir cada tupla de la tabla 2 con la 1 entonces hacemos un for con las tuplas de la tabla 2
        for j in range(0,len(tabla2[primeraKeySegundaTabla])):
            for key in tablaNueva:
       '''
    #Segun la cantidad de tuplas de la tabla 2 inserto SOLAMENTE los valores de las tuplas de la tabla 1 (luego insertaré las de la tabla 2)
    tuplasTabla2 = len(tabla2[atributosDos[0]])
    for i in range(0,len(tabla1[atributosUno[0]])):
        #Vamos a agregar lo que dijimos antes
        #La cantidad de tuplas de la tabla 2 representa este for
        for j in range(0,tuplasTabla2):
            #Este for se refiere a las keys de la tabla 1 (porque SOLAMENTE vamos a insertar los valores de los atributos 1, repitiendo segun la cantidad de tuplas)
            for key in atributosUno:
                tablaNueva[key].append(tabla1[key][i])
    #Ahora vamos a agregar los valores faltantes de la tabla 2 (recordemos que es cada tupla de la tabla 1 con todas las tuplas de la tabla 2, entonces vamos a rotar)
    while len(tablaNueva[atributosDos[0]]) != len(tablaNueva[atributosUno[0]]):
        for i in range(0,tuplasTabla2):
            for key in atributosDos:
                tablaNueva[key].append(tabla2[key][i])
    return tablaNueva
#Dibujar la tabla
def imprimirTabla(diccionario):
    Valores = []
    Nombres = []
    #Recorro todo el diccionario para obtener los atributos
    for key in diccionario:
        Nombres.append(key)
    #Ahora los valores de cada atributo
    for i in range(0,len(diccionario.get(Nombres[0]))):
        Valor = []
        for key in diccionario:
            Valor.append(diccionario[key][i])
        Valores.append(Valor)
    print(tabulate(Valores,headers = Nombres))
#Pues este es el caso en el cual las dos tablas tienen los mismos atributos
def iguales(tabla1,tabla2):
    #La tabla que se va a devolver al final
    tablaNueva = {}
    #Agregamos los atributos de la tabla 1 (da igual si es la 1 o 2, las dos tienen los mismos atributos)
    for key in tabla1:
        tablaNueva.update({key:[]})
    #Lista atributos tabla 1:
    atributosUno = list(tabla1.keys())
    #Lista atributos tabla 2:
    atributosDos = list(tabla2.keys())
    #Agregamos los atributos de la tabla 1
    #Tuplas de la tabla 1
    tuplaUno = []
    #Recorremos las filas por su key para agregarlo a la lista de tupla uno
    for i in range(0,len(tabla1[atributosUno[0]])):
        #La tupla i de la tabla
        tupla = []
        #Agregamos los valores de cada atributo de dicha tupla
        for key in tabla1:
            tupla.append(tabla1[key][i])
        #Para la lista de todas las tuplas
        tuplaUno.append(tupla)
    #Tuplas de la tabla 2 (al ser similar que el caso 2 no voy a comentar todas sus partes)
    tuplaDos = []
    for i in range(0,len(tabla2[atributosDos[0]])):
        tupla = []
        for key in tabla2:
            tupla.append(tabla2[key][i])
        tuplaDos.append(tupla)
    #Ahora lo que vamos a hacer es checkear las tuplas de la tabla 1 con la de la tabla 2, en caso de que una tupla esté en la tupla 2 pues se agrega a la nueva tabla.
    for i in range(0,len(tuplaUno)):
        #Si la tupla está en la tupla dos
        if tuplaUno[i] in tuplaDos:
            #Este contador es para que en cada for vaya al siguiente elemento de la lista (tuplaUno[i]), para agregar el valor con el correspondiente atributo
            contador = 0
            for key in tablaNueva:
                tablaNueva[key].append(tuplaUno[i][contador])
                #Incrementamos el contador justamente para este objetivo
                contador += 1
    return tablaNueva
#La última opción: en caso de que existan atributos en común pero no todos son iguales:
def atributosComun(tabla1,tabla2):
    tablaNueva = {}
    #Lista atributos tabla 1:
    atributosUno = list(tabla1.keys())
    #Lista atributos tabla 2:
    atributosDos = list(tabla2.keys())
    #Agregamos los atributos de la tabla 1
    for key in tabla1:
        tablaNueva.update({key:tabla1[key]})
    #Vamos a encontrar los atributos en común:
    atributosComun = []
    for i in range(0,len(atributosDos)):
        if atributosDos[i] in atributosUno:
            atributosComun.append(atributosDos[i])
    #Vamos a encontar los atributos que NO son comunes:
    atributosNoComun = []
    for i in range(0,len(atributosDos)):
        if atributosDos[i] not in atributosUno:
            atributosNoComun.append(atributosDos[i])
    #Agregamos los atributos de la tabla 2 que no están en la 1
    for key in atributosNoComun:
        tablaNueva.update({key:[]})
    #Tuplas de la tabla 2 NO COMUNES(Toma el mismo estilo de las anteriores veces)
    tuplaDosNoComun = []
    for i in range(0,len(tabla2[atributosDos[0]])):
        tupla = []
        for key in atributosNoComun:
            tupla.append(tabla2[key][i])
        tuplaDosNoComun.append(tupla)
    #Valores de cada tupla, pero solamente se toman de los atributos COMUNES
    tuplaUnoComun = []
    for i in range(0,len(tabla1[atributosUno[0]])):
        #La tupla i de la tabla
        tupla = []
        #Agregamos los valores DE LOS ATRIBUTOS EN COMUN DE DICHA TUPLA
        for key in atributosComun:
            tupla.append(tabla1[key][i])
        tuplaUnoComun.append(tupla)
    #Hacemos lo mismo con la tabla dos (no comentaré por ser un comportamiento similar)
    tuplaDosComun = []
    for i in range(0,len(tabla2[atributosDos[0]])):
        tupla = []
        for key in atributosComun:
            tupla.append(tabla2[key][i])
        tuplaDosComun.append(tupla)
    
    #En caso de que los valores de los atributos en común de la tabla 1 (respecto la tupla en donde se esté) esté presente en la tabla 2 entonces se hará natural join. (En caso de que no esté se introduce NULL)
    for i in range(0,len(tuplaUnoComun)):
        #¿Están estos valores de la tupla (según el atributo en común) en la otra tabla?
        if tuplaUnoComun[i] in tuplaDosComun:
            contador = 0
            #Entonces metalo en los atributos que estaban en la tabla 2 pero no en la 1
            for key in atributosNoComun:
                tablaNueva[key].append(tuplaDosNoComun[i][contador])
                contador += 1
        #¿No están? Entonces meta NULL en esos valores.
        else:
            for key in atributosNoComun:
                tablaNueva[key].append("NULL")
    return tablaNueva

    

#La función del primer punto
def uno():
    #La tabla uno (se realizó otra vez como diccionario por la facilidad para acceder a los datos)
    relacionUno = {}
    #Tabla dos
    relacionDos = {}
    #Se solicita los atributos de la primera tabla
    print("Introduzca los atributos de la primera relación (separados por espacio)")
    atributosUno = input()
    listaAtributosUno = atributosUno.split()
    #Pedimos los valores de cada atributo
    print("Ahora introduzca los valores por cada atributo: (los datos de cada columna)")
    for i in range(0,len(listaAtributosUno)):
        print("Atributo " + listaAtributosUno[i] + " (separados por un espacio)")
        valores = input()
        listaValores = valores.split()
        #Agregamos al atributo y sus valores (que están en una lista) al diccionario (que simula ser una tabla)
        relacionUno.update({listaAtributosUno[i]: listaValores})
    #Dibujar la primera tabla
    print("Tabla uno:")
    imprimirTabla(relacionUno)
    #Vamos a hacer esto mismo con la segunda tabla
    print("Introduzca los atributos de la segunda relación (separados por un espacio)")
    atributosDos = input()
    listaAtributosDos = atributosDos.split()
    #Pedimos los valores de cada atributo
    print("Ahora introduzca los valores por cada atributo: (los datos de cada columna)")
    for i in range(0,len(listaAtributosDos)):
        print("Atributo " + listaAtributosDos[i] + " (separados por un espacio)")
        valores = input()
        listaValores = valores.split()
        #Agregamos el atributo y sus valores (que están en una lista) al diccionario (que simula ser una tabla)
        relacionDos.update({listaAtributosDos[i]:listaValores})
    #Segunda tabla
    print("Tabla dos:")
    imprimirTabla(relacionDos)
    print("\n")
    #Vamos a checkear si tienen atributos en común, dependiendo de los atributos en común se realiza una acción (que son 3 en total)
    print("Tabla resultante:")
    #Primer caso: no hay atributos en comun
    #Si no hay ningun atributo de la listaDos en la listaUno
    if any(x in listaAtributosUno for x in listaAtributosDos) == False:
        nuevaTabla = noHayRelacionados(relacionUno,relacionDos)
    #Caso dos: todos los atributos son comunes:
    #Lo pongo sort para que compare los datos con orden (usted puede introducir la tabla1 y tabla 2 con diferente orden)

    if set(listaAtributosUno) == set(listaAtributosDos):
        #El sort es para introducir luego los datos ordenados
        listaAtributosUno.sort()
        listaAtributosDos.sort()
        nuevaTabla = iguales(relacionUno,relacionDos)
    #Caso tres: Hay atributos en común, pero no todos son iguales en sí
    if any(x in listaAtributosUno for x in listaAtributosDos) == True:
        if len(listaAtributosUno) != len(listaAtributosDos):
            nuevaTabla = atributosComun(relacionUno,relacionDos)
    imprimirTabla(nuevaTabla)

uno()


