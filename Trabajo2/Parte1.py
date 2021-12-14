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



