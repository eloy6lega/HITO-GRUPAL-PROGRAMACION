from random import sample 

#CON BUBBLESORT:

#importamos el método 'sample' de la biblioteca random para generar listas aleatorias

#hacemos una lista que almacene los numeros comprendidos entre el 1 y el 11 (1,2,3,4,5,6,7,8,9,10)
lista_de_numeros = list(range(1, 11)) #Creamos la lista principal con números del 0 al 10

#creamos una lista aleatoria con el método sample con los 10 elementos aleatorios de la lista base
vector_bubblesort = sample(lista_de_numeros,10) 

#creamos una función para hacer los métodos
def bubblesort(vector_bubblesort):
    #printeamos la lista SIN ordenar
    print("BUBBLESORT: Vector sin ordenar:",vector_bubblesort)

    n = 0 #creamos un contador del largo del vector
    for _ in vector_bubblesort: #bucle for _ in _:
        n += 1 #cuenta los caracteres de dentro del vector / se puede poner también de forma: n = +1

    for l in range(n-1): #primer bucle del bucle anidado
    # Le damos un rango n para que complete el proceso. 
        for u in range(0, n-l-1): #segundo bucle del bucle anidado
            #revisa la matriz de 0 hasta n-i-1 (que será 10 en nuestro caso)
            if vector_bubblesort[u] > vector_bubblesort[u+1]:
                vector_bubblesort[u], vector_bubblesort[u+1] = vector_bubblesort[u+1], vector_bubblesort[u]
            # Se intercambian SÓLO SI el elemento encontrado es mayor (vector(u)>vector(u+1))
            #y posteriormente pasa al siguiente

    #ahora printeamos ya una vez hecha la ordenación BubbleSort
    print ('BUBBLESORT: Con ordenación BubbleSort:', vector_bubblesort) 
bubblesort(vector_bubblesort) #invocamos la function

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
print('---------------------------------------------------------------------------------------------------------') #separador
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#CON INSERCIÓN

#hacemos una lista que almacene los numeros comprendidos entre el 1 y el 11 (1,2,3,4,5,6,7,8,9,10)
lista_de_numeros_2 = list(range(1, 11)) # Creamos la lista base con números del 1 al 100

#creamos una lista aleatoria con el método sample con los 10 elementos aleatorios de la lista base
vector_insercion = sample(lista_de_numeros_2,10)

#creamos una función para hacer los métodos
def insertionsort(vector_insercion): 
    #printeamos la lista SIN ordenar
    print("INSERCION: El vector SIN ordenar es:", vector_insercion)

    largo = 0 #creamos un contador del largo del vector

    for i in vector_insercion:
        largo += 1 #obtenemos el largo del vector. También se puede escribir: largo = +1

    #recorremos la lista desde el primer valor hasta el último (1-11)
    for i in range(1, largo): #bucle for _ in _ : 
        elemento = vector_insercion[i] 

        #movemos los elementos de vector_insercion[0...i-1], que son mayores que el elemento a una posición adelante de su posición actual
        j = i-1

        while j >= 0 and elemento < vector_insercion[j] : #bucle while...
                vector_insercion[j+1] = vector_insercion[j] 
                j -= 1 #se puede escribir también como: j = -1
        vector_insercion[j+1] = elemento

    #printeamos el vector YA ordenado por inserción
    print("INSERCION: Ordenado con Inserción: ", vector_insercion)
insertionsort(vector_insercion)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
print('---------------------------------------------------------------------------------------------------------') #separador
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#POR SELECCIÓN

#hacemos una lista que almacene los numeros comprendidos entre el 1 y el 11 (1,2,3,4,5,6,7,8,9,10)
lista_de_numeros_3 = list(range(1, 11)) # Creamos la lista base con números del 1 al 10

#creamos una lista aleatoria con el método sample con los 10 elementos aleatorios de la lista base
vector_seleccion = sample(lista_de_numeros_3,10) 

#creamos una función para hacer los métodos
def selectionsort(vector_seleccion):
    #imprimimos la lista sin la ordenación por selección
    print ("SELECCIÓN: El vector SIN ordenar es:",vector_seleccion)
    
    #establecemos el contador del largo del vector
    largo = 0
    
    #bucle for _ in _ : para obtener cada vez uno en el largo (hasta el límite marcado)
    for _ in vector_seleccion:
        largo += 1 #obtenemos el largo del vector

    #otro bucle for _ in _ :  
    for i in range(largo): 
        #encontrar el minimo elemento de los restantes sin ordenar
        minimo = i 
        #otro bucle for _ in _ : anidado al primero (bucle anidado)
        for j in range(i+1, largo): 
            if vector_seleccion[minimo] > vector_seleccion[j]: 
                minimo = j 
        #cambiamos el elemento minimo encontrado con el primer elemento de la "matriz"
        vector_seleccion[i], vector_seleccion[minimo] = vector_seleccion[minimo], vector_seleccion[i]
        #repetimos el proceso hasta terminar con todos

    #printeamos el vector ordenado por selección
    print("SELECCIÓN: Ordenado con Selección: ",vector_seleccion)
selectionsort(vector_seleccion)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
print('---------------------------------------------------------------------------------------------------------') #separador
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#SHELL O INCREMENTO DECRECIENTE

#hacemos una lista que almacene los numeros comprendidos entre el 1 y el 11 (1,2,3,4,5,6,7,8,9,10)
lista_de_numeros_4 = list(range(1, 11)) # Creamos la lista base con números del 1 al 10

#creamos una lista aleatoria con el método sample con los 10 elementos aleatorios de la lista base
vector_shell = sample(lista_de_numeros_4,10)

#creamos una función para hacer los métodos
def shellsort(vector_shell):
    #printeamos los números sin ordenar según se han generado
    print("SHELL: El vector SIN ordenar es:", vector_shell)

    #contador del largo del vector
    largo = 0

    #bucle for _ in _ : para ir sumando al contador
    for i in vector_shell:
        largo += 1
    distancia = largo // 2

    #creamos un bucle según las distancias
    while distancia > 0:
        #bucle for _ in _ : con rango entre la distancia y el largo
        for i in range(distancia, largo):
            val = vector_shell[i]
            j = i
            while j >= distancia and vector_shell[j - distancia] > val:
                vector_shell[j] = vector_shell[j - distancia]
                j -= distancia #se escribe igual así: j = -distancia
            vector_shell[j] = val
        distancia //= 2 #acotamos la distancia nuevamente y continua el ciclo hasta el final

    #printeamos el vector ordenado con shell o incremento decreciente
    print("SHELL: Ordenado con Shell: ", vector_shell)
shellsort(vector_shell)