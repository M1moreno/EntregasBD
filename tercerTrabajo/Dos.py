#La libreria para dibujar la tabla
from tabulate import tabulate
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
#La función del segundo punto
def dos():
    #La tabla en cuestión
    relacion = {}
    #Los atributos de la tabla
    print("Introduzca los atributos de la relación (separados por espacio)")
    atributos = input()
    #Una lista con los atributos 
    listaAtributos = atributos.split()
    print("Ahora introduzca los valores por cada atributo: (los datos de cada columna)")
    for i in range(0,len(listaAtributos)):
        print("Atributo " + listaAtributos[i] + " (separados por un espacio)")
        valores = input()
        listaValores = valores.split()
        #Agregamos al atributo y sus valores (que están en una lista) al diccionario (que simula ser una tabla)
        relacion.update({listaAtributos[i]: listaValores})
    #Dibujar la tabla:
    print("Tabla:")
    imprimirTabla(relacion)
    print("Introduzca la lista de atributos para agrupar: (separados por un espacio)")
    atributosAgrupar = input()
    listaAtributosAgrupar = atributosAgrupar.split()
    #Introducir la lista de agregados
    print("Aviso: Cada agregado se introduce en MAYÚSCULAS")
    print("Introduzca la cantidad de agregados:")
    cantidadAgregados = int(input())
    #Se le pedirá la función y su respectivo atributo
    atributosAgregados = []
    funcionAgregados = []
    for i in range(0,cantidadAgregados):
        #Petición de la función
        print("Introduzca la función de grupo: " + str(i+1))
        funcion = input()
        funcionAgregados.append(funcion)
        #Petición del atributo
        print("Introduzca el atributo al cual se le hará la función " + str(i+1))
        atributo = input()
        atributosAgregados.append(atributo)
    #Vamos a ir creando la nueva tabla
    nuevaTabla = {}
    #Agregamos los atributos que nos pidieron al principio (no el de las funciones)
    for i in range(0,len(listaAtributosAgrupar)):
        nuevaTabla.update({listaAtributosAgrupar[i]:[]})
    atributosFuncionAgregados = [] #Se crea esta línea para tener el nombre de los atributos de las agrupaciones a hacer (Ej: SUMsalario)
    #Ahora vamos a agregar los nombres de las columnas de cada función con su debido atributo de agrupación
    for i in range(0,len(funcionAgregados)):
        atributo = str(funcionAgregados[i]) + str(atributosAgregados[i])
        nuevaTabla.update({atributo:[]})
        atributosFuncionAgregados.append(atributo)
    #Lista de no repetidos (Para ir agrupando)
    listaNoRepetidos = []
    #Vamos a recorrer todas las tuplas para buscar ese grupito de valores de los atributos y sus respectivos grupos (es decir, buscar cuales se repiten y agruparlos)
    for i in range(0,len(relacion[listaAtributos[0]])):
        #Los valores con los atributos solicitados
        tupla = []
        for key in listaAtributosAgrupar:
            tupla.append(relacion[key][i])
        #¿Esta tupla ya la hemos visto antes? (Para evitar conjuntos repetidos)
        if tupla not in listaNoRepetidos:
            listaNoRepetidos.append(tupla)
    #Ahora vamos a agregar estos conjuntos a la tabla
    #Método similar al presentado en el punto Uno (Recorrer las tuplas y agregarlos a cada atributo con el [contador])
    for i in range(0,len(listaNoRepetidos)):
        contador = 0
        for key in listaAtributosAgrupar:
            nuevaTabla[key].append(listaNoRepetidos[i][contador])
            contador += 1
    listaAtributosExceso = [] #Los atributos restantes pues
    for i in range(0,len(listaAtributos)):
        if listaAtributos[i] not in listaAtributosAgrupar:
            listaAtributosExceso.append(listaAtributos[i])
    listaDemasAtributos = [] #Conjuto de datos (restantes) segun el conjunto de datos (listaNoRepetidos)
    #Vamos a agregar todos los demás datos a cada agrupación
    for i in range(0,len(listaNoRepetidos)):
        #Primero vacíos
        listaDemasAtributos.append([])
    for i in range(0,len(relacion[listaAtributos[0]])):
        tupla = []
        #La de los otros atributos diferentes a los atributos de agrupamiento
        for key in listaAtributosExceso:
            tupla.append(relacion[key][i])
        #Ahora los atributos de agrupamiento (no me refiero a los atributos en sí, sino al conjunto de valores según la tupla)
        tuplaAtributosAgrupados = []
        for key in listaAtributosAgrupar:
            tuplaAtributosAgrupados.append(relacion[key][i])
        #Saco el indice para poder meter los valores de los atributos diferentes a los atributos de agrupamiento según el conjunto de agrupamiento
        indice = listaNoRepetidos.index(tuplaAtributosAgrupados)
        listaDemasAtributos[indice].append(tupla)
    #Agregamos una lista de errores, para que el usuario conozca en que función se ocasionó el error
    errores = []
    #Hora de comprobar las funciones
    for i in range(0,len(funcionAgregados)):
        #El atributo al que se refiere la función:
        atributoFuncion = atributosAgregados[i]
        #Hora de sacarle el indice según la lista de atributos de exceso (esto para obtener solo los valores de dicho atributo en cada agrupación)
        indiceAtributoFuncion = listaAtributosExceso.index(atributoFuncion)
        #En caso de que la funcion sea max
        if funcionAgregados[i] == "MAX":
            #Por todos los grupos
            for j in range(0,len(listaDemasAtributos)):
                listaDedicada = []
                #Ahora vamos a buscar por todas las tuplas de cada grupo
                for k in range(0,len(listaDemasAtributos[j])):
                    #Se mete el atributo solicitado por la función
                    listaDedicada.append(listaDemasAtributos[j][k][indiceAtributoFuncion])
                #El máximo de ese grupito
                #El primer elemento de la lista, no es necesario verificar los demás
                #
                elemento = listaDedicada[0]
                #Suponemos inicialmente que no son números, sino que son strings
                entero = False
                if elemento.count('-') == 1:
                    #Reemplaza el "-", pero no queremos modificar al elemento en sí. (Nada más verificar)
                    elemento1 = elemento.replace('-','',1)
                    #Ahora reemplacemos ese "-" y unimos las dos partes , para ver si funciona el .isdigit
                    if elemento1.isdigit() == True:
                        #¿Tiene un . para separar el decimal? Entonces veamos si está bien (si es un número)
                        if elemento1.count('.') == 1:
                            #Reemplazamos el . por nada (se elimina el punto)
                            if elemento1.replace('.','',1).isdigit() == True:
                                entero = True
                        elif elemento1.count('.') == 0:
                            if elemento1.isdigit() == True:
                                entero = True
                elif elemento.count('-') == 0:
                    if elemento.count('.') == 1:
                        #Reemplazamos el . por nada (se elimina el punto)
                        if elemento.replace('.','',1).isdigit() == True:
                            entero = True
                    elif elemento.count('.') == 0:
                        if elemento.isdigit() == True:
                            entero = True
                if entero == True:
                    nuevaListaDedicada = [float(x) for x in listaDedicada]
                    Maximo = max(nuevaListaDedicada)
                else:
                    Maximo = max(listaDedicada)
                #Metemos ese máximo a la tabla
                nuevaTabla[atributosFuncionAgregados[i]].append(Maximo)
        #Similar al MAX, solo que ahora es el valor mínimo
        #Función MIN
        if funcionAgregados[i] == "MIN":
            for j in range(0,len(listaDemasAtributos)):
                listaDedicada = []
                for k in range(0,len(listaDemasAtributos[j])):
                    listaDedicada.append(listaDemasAtributos[j][k][indiceAtributoFuncion])
                #Verificamos si el primer elemento es un string o un número (para evitar complicaciones)
                #Esta parte del código se tomó del SUM, dado que nos dimos cuenta de que
                #si se hacía un min o max de un número no estaba funcionando correctamente, entonces
                #tocaba pasar los strings de la lista a floats
                elemento = listaDedicada[0]
                entero = False
                if elemento.count('-') == 1:
                    #Reemplaza el "-", pero no queremos modificar al elemento en sí. (Nada más verificar)
                    elemento1 = elemento.replace('-','',1)
                    #Ahora reemplacemos ese "-" y unimos las dos partes , para ver si funciona el .isdigit
                    if elemento1.isdigit() == True:
                        #¿Tiene un . para separar el decimal? Entonces veamos si está bien (si es un número)
                        if elemento1.count('.') == 1:
                            #Reemplazamos el . por nada (se elimina el punto)
                            if elemento1.replace('.','',1).isdigit() == True:
                                entero = True
                        elif elemento1.count('.') == 0:
                            if elemento1.isdigit() == True:
                                entero = True
                elif elemento.count('-') == 0:
                    if elemento.count('.') == 1:
                        #Reemplazamos el . por nada (se elimina el punto)
                        if elemento.replace('.','',1).isdigit() == True:
                            entero = True
                    elif elemento.count('.') == 0:
                        if elemento.isdigit() == True:
                            entero = True
                if entero == True:
                    nuevaListaDedicada = [float(x) for x in listaDedicada]
                    Minimo = min(nuevaListaDedicada)
                else:
                    Minimo = min(listaDedicada)

                nuevaTabla[atributosFuncionAgregados[i]].append(Minimo)
        #Función SUM
        if funcionAgregados[i] == "SUM":
            #verdadSuma funciona para verificar si existe un dato que no es un digito, entonces no se puede efectuar la suma en sí
            verdadSuma = 1
            #Recorremos todos los grupitos
            for j in range(0,len(listaDemasAtributos)):
                #Por cada grupo se inicia la suma
                SUMA = 0.0
                listaDedicada = []
                #Todas las tuplas de dicho grupo según el atributo de la función
                for k in range(0,len(listaDemasAtributos[j])):
                    listaDedicada.append(listaDemasAtributos[j][k][indiceAtributoFuncion])
                #Ahora hagamos la suma con los atributos de dichas tuplas
                for elemento in listaDedicada:
                    #Vamos a checkear antes algo: ¿Es esto un número negativo o positivo? (Me di cuenta luego de que ,isdigit() no identifica el "-", entonces toca hacerlo a mano)
                    if elemento.count('-') == 1:
                        #Reemplaza el "-", pero no queremos modificar al elemento en sí. (Nada más verificar)
                        elemento1 = elemento.replace('-','',1)
                        #Ahora reemplacemos ese "-" y unimos las dos partes , para ver si funciona el .isdigit
                        if elemento1.isdigit() == True:
                            #¿Tiene un . para separar el decimal? Entonces veamos si está bien (si es un número)
                            if elemento1.count('.') == 1:
                                #Reemplazamos el . por nada (se elimina el punto)
                                if elemento1.replace('.','',1).isdigit() == True:
                                    SUMA += float(elemento)
                                else:
                                    verdadSuma = 0
                            elif elemento1.count('.') == 0:
                                if elemento1.isdigit() == True:
                                    SUMA += float(elemento)
                                else:
                                    verdadSuma = 0
                            else:
                                verdadSuma = 0
                        else:
                            verdadSuma = 0
                    elif elemento.count('-') == 0:
                        if elemento.count('.') == 1:
                            #Reemplazamos el . por nada (se elimina el punto)
                            if elemento.replace('.','',1).isdigit() == True:
                                SUMA += float(elemento)
                            else:
                                verdadSuma = 0
                        elif elemento.count('.') == 0:
                            if elemento.isdigit() == True:
                                SUMA += float(elemento)
                            else:
                                verdadSuma = 0
                        else:
                            verdadSuma = 0
                    else:
                        verdadSuma = 0
                nuevaTabla[atributosFuncionAgregados[i]].append(SUMA)
            #Agregar esta función a las que están dando error si hubo un error.
            if verdadSuma == 0:
                mensaje = "La columna " + str(atributosFuncionAgregados[i]) + " presenta un error."
                errores.append(mensaje)
        #Función average (Demasiado similar a la anterior, solo que se divide por la cantidad de datos)
        if funcionAgregados[i] == "AVG":
            #verdadAvg funciona para verificar si hay un digito o no, en caso de que no pues saltará error luego
            verdadAvg = 1
            #Recorremos todos los grupitos
            for j in range(0,len(listaDemasAtributos)):
                #Por cada grupo se inicia la suma
                SUMA = 0.0
                listaDedicada = []
                #Todas las tuplas de dicho grupo según el atributo de la función
                for k in range(0,len(listaDemasAtributos[j])):
                    listaDedicada.append(listaDemasAtributos[j][k][indiceAtributoFuncion])
                #Ahora hagamos la suma con los atributos de dichas tuplas
                for elemento in listaDedicada:
                    #También vamos a verificar si tiene un "-"
                    if elemento.count('-') == 1:
                        elemento1 = elemento.replace('-','',1)
                        if elemento1.isdigit() == True:
                            #¿Tiene un . para separar el decimal? Entonces veamos si está bien (si es un número)
                            if elemento1.count('.') == 1:
                                #Reemplazamos el . por nada (se elimina el punto) 
                                if elemento1.replace('.','',1).isdigit() == True:
                                    SUMA += float(elemento)
                                else:
                                    verdadAvg = 0
                            elif elemento1.count('.') == 0:
                                if elemento1.isdigit() == True:
                                    SUMA += float(elemento)
                                else:
                                    verdadAvg = 0
                            else:
                                verdadAvg = 0
                        else:
                            verdadAvg = 0
                    elif elemento.count('-') == 0:
                        if elemento.count('.') == 1:
                            #Reemplazamos el . por nada (se elimina el punto) 
                            if elemento.replace('.','',1).isdigit() == True:
                                SUMA += float(elemento)
                            else:
                                verdadAvg = 0
                        elif elemento.count('.') == 0:
                            if elemento.isdigit() == True:
                                SUMA += float(elemento)
                            else:
                                verdadAvg = 0
                        else:
                            verdadAvg = 0
                    else:
                        verdadAvg = 0
                #Aquí será el promedio
                nuevaTabla[atributosFuncionAgregados[i]].append(SUMA/float(len(listaDedicada)))
                #Agregar esta función a las que están dando error si hubo un error.
            if verdadAvg == 0:
                mensaje = "La columna " + str(atributosFuncionAgregados[i]) + " presenta un error."
                errores.append(mensaje)
        #Función count
        if funcionAgregados[i] == "COUNT":
            #No tenemos que pasar por cada valor de cada tupla, porque simplemente es la cantidad de tuplas por grupo
            for j in range(0,len(listaDemasAtributos)):
                contador = len(listaDemasAtributos[j])
                nuevaTabla[atributosFuncionAgregados[i]].append(contador)
        #Función CONCATENATE
        if funcionAgregados[i] == "CONCATENATE":
            for j in range(0,len(listaDemasAtributos)):
                listaDedicada = []
                #Todas las tuplas de dicho grupo según el atributo de la función
                for k in range(0,len(listaDemasAtributos[j])):
                    listaDedicada.append(listaDemasAtributos[j][k][indiceAtributoFuncion])
                #Vamos a crear el mensaje completo con el .join
                mensaje = "-".join(listaDedicada)
                nuevaTabla[atributosFuncionAgregados[i]].append(mensaje)
    if len(errores) == 0:
        imprimirTabla(nuevaTabla)
    else:
        print("El operador no se puede procesar, hay al menos un error en los datos ingresados")
        for error in errores:
            print(error)
    print("Muchas gracias por el uso de este software, hasta luego.")


        
    

