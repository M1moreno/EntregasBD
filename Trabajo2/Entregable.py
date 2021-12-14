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
    print("Digite la cabecera por favor")
    atributos = input()
    listaAtributos = atributos.split()
    #Ahora vamos a introducir cada valor que contiene dicho atributo, también se va separa por espacio:
    #Ej: 13 22 55 330 0
    print("Ahora introduzca los valores por cada atributo:")
    #El for es para que introduzca x veces según la cantidad de x atributos
    for i in range(0,len(listaAtributos)):
        print("Atributo " + listaAtributos[i] + ":")
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
#Esta función va a revisar si existe esa dependencia funcional en el otro grupo
#Esta funcion es para resumir lo de que solo agregar elementos que no estén duplicados en la lista
def agregarNoDuplicados(listaA,listaB):
    #Este pequeño detalle es demasiado importante en python. Si ponemos que son iguales va a referenciar al mismo, es decir, va a modificar al mismo que se anda apuntando (haciendo un error fatal). Por eso nada más creamos este con todos los elementos que tiene el otro, pero sin apuntar al mismo
    listaRetornar = listaA[:]
    #Ahora vamos a recorrer toda la lista B para saber si existe un duplicado, si no está ese elemento entonces lo agregamos a la lista de la izquierda

    for i in range(0,len(listaB)):
        if listaB[i] not in listaRetornar:
            listaRetornar.append(listaB[i])
    #Retornamos lo que tenía la listaA con los elementos no repetidos de la listaB (los que no estaban en A)
    return listaRetornar
            
def probar(listaIzquierda,listaDerecha,listaIzquierdaContraria,listaDerechaContraria):
    #Toda la función es similar al algoritmo presentado en las diapositivas
    #El comprobable es el grupo de atributos con el que puede ser dependencia funcional el lado izquierda (como en el algoritmo)
    #Hicimos lo mismo que en la anterior función: crear una lista que tenga los elementos de la otra, pero sin referirnos a la misma (apuntar a la misma).

    comprobable = listaIzquierda[:]
    #Hacemos esto para que se pueda cumplir el while inicial
    anterior = len(comprobable) - 1
    #El while es por si se ha modificado la lista, en caso de que no pues se detiene el algoritmo (Puede ser menor o puede ser diferente, el punto es que se diferencien)

    while anterior < len(comprobable):
        #Tomamos el tamaño de la lista actualmente
        anterior = len(comprobable)
        #Vamos a recorrer toda la parte izquierda del grupo contrario
        #(Vamos a recorrer todo el grupo de dependencias )
        for i in range(0,len(listaIzquierdaContraria)):
            #Si los atributos de esta parte de la lista izquierda están en el comprobable:
            #Igual que en el algoritmo. Si resultado del algoritmo que andamos obteniendo está en alguna de las partes izquierda entonces revise si la parte derecha ya está en el resultado cambiante del algoritmo
            comprobar = all(i in comprobable for i in listaIzquierdaContraria[i])
            if comprobar == True:
                #Como esos atributos están en el comprobable vamos a agregar la parte derecha, pero solo los elementos que no estén en el comprobable (Como en el algoritmo)
                comprobable = agregarNoDuplicados(comprobable,listaDerechaContraria[i])
    #Ahora vamos a checkear si los atributos de listaDerecha están en el comprobable, como se hizo en el algoritmo
    #En palabras más sencillas, si la parte derecha de la dependencia está en el resultado del algoritmo. (De la que andabamos revisando en primer lugar)

    comprobacion = all(i in comprobable for i in listaDerecha)
    #Si así es pues se devuelve 1 (True)

    #A este punto el comprobable pudo o no haber cambiado de tamaño. En caso de que haya cambiado entonces que siga comprobando, hasta cuando llegue al punto de que sean iguales el anterior al actual (El resultado cambiante del algoritmo dejó de modificarse)

    if comprobacion == True:
        return 1
    #Si no pues sería 0 (False)
    else:
        return 0
    



def A():
    #Introducir el primer grupo:
    #Introducir el tamaño del primer grupo
    print("Introduzca el tamaño del primer conjunto")
    #El tamaño es para el for, para saber cuantos elementos van a existir en el grupo
    tamanoUno = int(input())
    #Aquí van a estar en sí todo el grupo de dependencias del grupo 1 según su lado
    #Ejemplo sencillo:
    #Tenemos el grupo [AP -> BHW, BHW -> C]
    #Entonces en este programa estaría guardandose como:
    #[[A P], [B H W]] (grupoUnoIzquierda)
    #[[B H W],[C]] (grupoUnoDerecha)
    #Así mismo va a ser con los del grupo dos, pero con sus respectivas listas.
    grupoUnoIzquierda = []
    grupoUnoDerecha = []
    #Se introduce primero la parte izquierda y luego la parte derecha, todo esto con espacios (por favor escriba estas letras en mayusculas)
    for i in range(0,tamanoUno):
        #Puse al final el i para que no se pierda de donde está
        print("Introduzca la parte izquierda " + str(i+1))
        izquierda = input()
        izquierdaMayuscula = izquierda.upper()
        grupoUnoIzquierda.append(izquierdaMayuscula.split())
        print("Introduzca la parte derecha " + str(i+1))
        derecha = input()
        derechaMayuscula = derecha.upper()
        grupoUnoDerecha.append(derechaMayuscula.split())
    #Ahora el segundo grupo hacemos lo mismo
    print("Introduzca el tamaño del segundo conjunto")
    tamanoDos = int(input())
    grupoDosIzquierda = []
    grupoDosDerecha = []
    for i in range(0,tamanoDos):
        print("Introduzca la parte izquierda " + str(i+1))
        izquierda = input()
        izquierdaMayuscula = izquierda.upper()
        grupoDosIzquierda.append(izquierdaMayuscula.split())
        print("Introduzca la parte derecha " + str(i+1))
        derecha = input()
        derechaMayuscula = derecha.upper()
        grupoDosDerecha.append(derechaMayuscula.split())


    #Voy a imprimir ahora los datos, para que se visualice de la mejor forma lo que se acabó de realizar
    print("Grupo 1: ")
    #Las listas que se van a visualizar al final
    listaImprimirUno = []
    listaImprimirDos = []
    for i in range(0,len(grupoUnoIzquierda)):
        listaEjemplo = []
        #La parte de la izquierda de la dependencia funcional en donde está situado ahora mismo el recorrido
        listaEjemplo.append(grupoUnoIzquierda[i])
        #La flecha para que se de cuenta de que es una dependencia funcional
        listaEjemplo.append("->")
        #La parte derecha
        listaEjemplo.append(grupoUnoDerecha[i])
        listaImprimirUno.append(listaEjemplo)
    print(listaImprimirUno)
    #Hacemos lo mismo con 2
    print("Grupo 2: ")
    for i in range(0,len(grupoDosIzquierda)):
        listaEjemplo = []
        listaEjemplo.append(grupoDosIzquierda[i])
        listaEjemplo.append("->")
        listaEjemplo.append(grupoDosDerecha[i])
        listaImprimirDos.append(listaEjemplo)
    print(listaImprimirDos)
    #Ya tenemos los datos listos
    #Grupo 1 a grupo 2
    #Esto es si realmente son equivalentes o no, entonces por ahora vamos a suponer que sí son equivalentes
    verdadFunciona = 1
    
    for i in range(0,len(grupoUnoIzquierda)):
        verdad = probar(grupoUnoIzquierda[i],grupoUnoDerecha[i],grupoDosIzquierda,grupoDosDerecha)
        #En caso de que en ese caso no tenga una dependencia funcional que cumpla entonces verdadFunciona = 0, significa que no funciona
        if verdad == 0:
            verdadFunciona = 0
    #Si del 1 a 2 funciona entonces ahora del 2 al 1 a checkear

    if verdadFunciona == 1:
        for i in range(0,len(grupoDosIzquierda)):
            #Lo mismo que el anterior pero en sus contrarios
            verdad = probar(grupoDosIzquierda[i],grupoDosDerecha[i],grupoUnoIzquierda,grupoUnoDerecha)
         
            if verdad == 0:
                verdadFunciona = 0
        if verdadFunciona == 1:
            print("Son equivalentes")
        else:
            print("No son equivalentes")
    #Si no funciona pues no funciona
    else:
        print("No son equivalentes")
def ParteB():
    #Quiero dejar aquí algo muy claro desde el principio: se usó la palabra nombres para referirse a los atributos para poder relacionar mejor las variables que ando creando (ya que un atributo en POO se refiere a algo distinto en BD, es simplemente por mero convenio personal que hice eso).
    #Segunda claridad: si quiere introducir que no hay un dato (NULL) por favor escribalo de la misma forma siempre que lo vaya a realizar. Si escribe NULL siempre debe ser NULL, si pone 0 pues siempre debe ser 0.
    #El diccionario que va a contener cada atributo con sus valores. Preferí hacerlo un diccionario para al nada más llamar el atributo poder acceder a todos sus valores (facilidad)

    diccionarioCabecera = {}
    #Ahora solo ando pidiendo la cabecera (Los atributos van separados por espacios).
    #Ej para introducir: Codigo Usuario Tipodesangre
    print("Se presentará a continuación el punto 2B")
    print("Digite la cabecera por favor")
    nombres = input()
    listaNombres = nombres.split()
    #Ahora vamos a introducir cada valor que contiene dicho atributo, también se va separa por espacio:
    #Ej: 13 22 55 330 0
    print("Ahora introduzca los valores por cada atributo:")
    #El for es justamente por eso, para que introduzca x veces según la cantidad de x atributos
    for i in range(0,len(listaNombres)):
        print("Atributo " + listaNombres[i] + ":")
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
    Funcionar = int(input("¿Quiere verificar las dependencias funcionales?"))
    Repeticion = 0
    while Funcionar == 1:
        #Va a imprimir la repetición x
        print("Verificación de la dependencia funcional número " + str(Repeticion))
        #Ahora vamos a verificar las dependencias. Primero el lado izquierdo de la dependencia.
        print("Introduzca los atributos del lado izquierdo")
        izquierda = input()
        dependenciaIzquierda = izquierda.split()
        #Ahora el lado derecho
        print("Introduzca los atributos del lado derecho")
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
        Funcionar = int(input("¿Quiere seguir con la verificación de dependencias funcionales?"))
        if Funcionar == 0:
            print("¡Hasta pronto!")
        Repeticion = Repeticion + 1
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


