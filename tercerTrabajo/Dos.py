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
#(La misma crearTabla de Uno)
def crearTabla(mensaje):
    #La relacion a crear
    relacion = {}
    #Imprimimos el mensaje sobre la primera relacion o segunda
    print(mensaje)
    #Los atributos
    atributosUno = input()
    listaAtributosUno = atributosUno.split(",")
    #Como por ahora no tienen valores entonces se le pone vacío
    for i in range(0,len(listaAtributosUno)):
        relacion.update({listaAtributosUno[i]: []})
    #Cantidad de tuplas
    print("Digite la cantidad de tuplas que posee la tabla (recuerde que los valores de cada tupla se separan con una coma)")
    cantidadTuplas = int(input())
    #Por las tuplas
    for i in range(0,cantidadTuplas):
        print("Tupla " + str(i+1))
        tupla = input()
        listaTuplas = tupla.split(",")
        #El contador es para que se vaya metiendo según el atributo
        contador = 0
        for elemento in listaTuplas:
            relacion[listaAtributosUno[contador]].append(elemento)
            contador += 1
    return relacion
#Vamos a crear una función para revisar si el conjunto de datos de un atributo es un String o un número
#Por toda la lista
def numero(lista):
    #Vamos a ver si todos los elementos de ese atributo son números
    numero_checkear = 0
    for numerito in lista:
        try:
            #¿Lo es? Ah bueno, entonces vaya sumando uno a ese numero_checkear
            float(numerito)
            numero_checkear += 1
        #¿No lo es? Pues no hacemos nada
        except ValueError:
            pass
    #¿Todos son números? Ah bueno, retorne verdadero
    if numero_checkear == len(lista):
        return True
   #Pues si no es pues es falso 
    else:
        return False

#La función del segundo punto
def dos():
    #La tabla en cuestión
    relacion = {}
    #Los atributos de la tabla
    relacion = crearTabla("Introduzca los atributos de la relación (separados por comas)")
    listaAtributos = [x for x in relacion]
    #Dibujar la tabla:
    print("Tabla:")
    imprimirTabla(relacion)
    print("Introduzca la lista de atributos para agrupar: (separados por comas)")
    atributosAgrupar = input()
    listaAtributosAgrupar = atributosAgrupar.split(",")
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
    #En caso de que el grupo no sea toda la tabla
    if atributosAgrupar != "":
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
        listaDemasAtributos = [] #Conjuto de datos segun el conjunto de datos (listaNoRepetidos)
        #Vamos a agregar todos los demás datos a cada agrupación
        for i in range(0,len(listaNoRepetidos)):
            #Primero vacíos
            listaDemasAtributos.append([])
        for i in range(0,len(relacion[listaAtributos[0]])):
            tupla = []
            #Los atributos de la relación
            for key in relacion:
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
            #Hora de sacarle el indice según la lista de atributos 
            indiceAtributoFuncion = listaAtributos.index(atributoFuncion)
            #En caso de que la funcion sea max
            if funcionAgregados[i] == "MAX":
                #Por todos los grupos
                for j in range(0,len(listaDemasAtributos)):
                    listaDedicada = []
                    #Ahora vamos a buscar por todas las tuplas de cada grupo
                    for k in range(0,len(listaDemasAtributos[j])):
                        #Se mete el atributo solicitado por la función
                        listaDedicada.append(listaDemasAtributos[j][k][indiceAtributoFuncion])
                    #Usamos nuestra bella función número para verificar si todos son números
                    verdad = numero(listaDedicada)
                    #¿Son números? Pues bueno, cree una lista en donde todos son floats para encontrar el max.
                    #(Es que esto se hace por la forma en que se compara el max y min en los strings en caso de que sea número, el cual no funciona de forma correcta)
                    if verdad == True:
                        nuevaListaDedicada = [float(x) for x in listaDedicada]
                        Maximo = max(nuevaListaDedicada)
                    #¿No lo es? Ah bueno, entonces comparemos como string y yap
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
                    #Hagamos lo mismo que en MAX, pero ahora pues se hace el mínimo
                    verdad = numero(listaDedicada)
                    if verdad == True:
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
                    #Hacemos el mismo check de que si los elementos son números o String, pero ahora incorporamos la suma
                    verdad = numero(listaDedicada)
                    #¿Todos son números? Ah, pues sume
                    if verdad == True:
                        for elemento in listaDedicada:
                            #Se suma
                            SUMA += float(elemento)
                        #Meta eso a la tabla
                        nuevaTabla[atributosFuncionAgregados[i]].append(SUMA)
                    #Entonces son string, vamos a agregar esto a la parte de errores
                    else:
                        verdadSuma = 0
                #¿Es string? Una lastima, porque ahora se imprimirá error y dirá que se presenta un error
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
                    #Hacemos el mismo check de que si los elementos son números o String, pero ahora incorporamos la suma
                    verdad = numero(listaDedicada)
                    #¿Todos son números? Ah, pues sume
                    if verdad == True:
                        for elemento in listaDedicada:
                            #Se suma
                            SUMA += float(elemento)
                        #Meta eso a la tabla
                        nuevaTabla[atributosFuncionAgregados[i]].append(SUMA/float(len(listaDedicada)))
                    #Entonces son string, vamos a agregar esto a la parte de errores
                    else:
                        verdadAvg = 0
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
        #Si no hay errores se imprime la tabla
        if len(errores) == 0:
            imprimirTabla(nuevaTabla)
        #Si hay errores no se imprime la tabla, como también se muestran los errores
        else:
            print("El operador no se puede procesar, hay al menos un error en los datos ingresados")
            for error in errores:
                print(error)
            print("Muchas gracias por el uso de este software, hasta luego.")
    else:        
        atributosFuncionAgregados = [] #Se crea esta línea para tener el nombre de los atributos de las agrupaciones a hacer (Ej: SUMsalario)
        #Ahora vamos a agregar los nombres de las columnas de cada función con su debido atributo de agrupación
        for i in range(0,len(funcionAgregados)):
            atributo = str(funcionAgregados[i]) + str(atributosAgregados[i])
            nuevaTabla.update({atributo:[]})
            atributosFuncionAgregados.append(atributo)
        #En caso de que no existen atributos para agrupar
        errores = []
        #Hora de comprobar las funciones
        #Usted va a notar que es demasiado similar al otro caso, pero es que acá es con los valores de la tabla original
        for i in range(0,len(funcionAgregados)):
            #Maximo
            if funcionAgregados[i] == "MAX":
                #Revisemos si la columna es de números o de strings
                verdad = numero(relacion[atributosAgregados[i]])
                #De numeros
                if verdad == True:
                    #Entonces tome el max del atributo de la tabla
                    nuevaListaDedicada = [float(x) for x in relacion[atributosAgregados[i]]]
                    Maximo = max(nuevaListaDedicada)
                #De strings
                else:
                    Maximo = max(relacion[atributosAgregados[i]])
                #Metalo a la tabla
                nuevaTabla[atributosFuncionAgregados[i]].append(Maximo)
            #Min (Demasiado similar al max, pero con min)
            if funcionAgregados[i] == "MIN":
                #Revisamos si la columna es de numeros o de strings
                verdad = numero(relacion[atributosAgregados[i]])
                #De numeros
                if verdad == True:
                    #Todos a ser float
                    nuevaListaDedicada = [float(x) for x in relacion[atributosAgregados[i]]]
                    Minimo = min(nuevaListaDedicada)
                #De strings
                else:
                    Minimo = min(relacion[atributosAgregados[i]])
                #Metalo a la tabla
                nuevaTabla[atributosFuncionAgregados[i]].append(Minimo)
            #Sumatoria
            if funcionAgregados[i] == "SUM":
                #Revisemos si son números o strings
                verdad = numero(relacion[atributosAgregados[i]])
                #De numeros
                if verdad == True:
                    #A sumar
                    SUMA = 0
                    #A float todos los elementos para luego sumarlos
                    for x in relacion[atributosAgregados[i]]:
                        SUMA += float(x)
                    #El resultado se mete a la tabla
                    nuevaTabla[atributosFuncionAgregados[i]].append(SUMA)
                #Si no son números no se pueden sumar
                else:
                    mensaje = "La columna " + str(atributosFuncionAgregados[i]) + " presenta un error."
                    errores.append(mensaje)
            #Promedio
            if funcionAgregados[i] == "AVG":
                #Revisemos si son números o strings
                verdad = numero(relacion[atributosAgregados[i]])
                #De numeros
                if verdad == True:
                    #A sumar
                    SUMA = 0
                    #A float todos los elementos para luego sumarlos
                    for x in relacion[atributosAgregados[i]]:
                        SUMA += float(x)
                    #Lo dividimos para que sea AVG
                    SUMA = SUMA/len(relacion[atributosAgregados[i]])
                    #El resultado se mete a la tabla, dividiendo por la longitud
                    nuevaTabla[atributosFuncionAgregados[i]].append(SUMA)
                else:
                    mensaje = "La columna " + str(atributosFuncionAgregados[i]) + " presenta un error."
                    errores.append(mensaje)
            #Contar
            if funcionAgregados[i] == "COUNT":
                #Cantidad de tuplas y ya
                nuevaTabla[atributosFuncionAgregados[i]].append(len(relacion[listaAtributos[0]]))
            #Concatenate:
            if funcionAgregados[i] == "CONCATENATE":
                #Vamos a crear el mensaje completo con el .join
                mensaje = "-".join(relacion[atributosAgregados[i]])
                nuevaTabla[atributosFuncionAgregados[i]].append(mensaje)
        #Si no tenemos errores:
        if len(errores) == 0:
            #En caso de que no tenga funcion de agreagados
            if len(funcionAgregados) == 0:
                print("La tabla está vacía, por eso no se anda dibujando ahora mismo.")
            #En caso contrario
            else:
                imprimirTabla(nuevaTabla)
        #Algún error
        else:
            print("El operador no se puede procesar, hay al menos un error en los datos ingresados")
            #Se imprimen todos los errores
            for error in errores:
                print(error)
            print("Muchas gracias por el uso de este software, hasta luego.")
        




        
    

