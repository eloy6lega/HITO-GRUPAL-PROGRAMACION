
#ENLACE DE BASE: https://github.com/GBaudino/MetodosDeOrdenamiento
#falta por adaptar a nuestro lenguaje las explicaciones de los dos últimos (selección y shell)

from random import sample 

#CON BUBBLESORT:

#importamos el método 'sample' de la biblioteca random para generar listas aleatorias

lista_de_numeros = list(range(1, 11)) #Creamos la lista principal con números del 0 al 10

#creamos una lista aleatoria con el método sample con los 10 elementos aleatorios de la lista base
vector_bubblesort = sample(lista_de_numeros,10) 

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

lista_de_numeros_2 = list(range(1, 11)) # Creamos la lista base con números del 1 al 100

#creamos una lista aleatoria con el método sample con los 10 elementos aleatorios de la lista base
vector_insercion = sample(lista_de_numeros_2,10)

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

lista_de_numeros_3 = list(range(1, 11)) # Creamos la lista base con números del 1 al 100

# Creamos una lista aleatoria con sample 
#(8 elementos aleatorios de la lista base)
vector_seleccion = sample(lista_de_numeros_3,10) 


def selectionsort(vector_seleccion):
    # Imprimimos la lista obtenida al principio (Desordenada)
    print ("SELECCIÓN: El vector SIN ordenar es:",vector_seleccion)
    
    largo = 0
    
    for _ in vector_seleccion:
        largo += 1 # Obtenemos el largo del vector
        
    for i in range(largo): 
      
        # Encontrar el minimo elemento de los restantes sin ordenar
        minimo = i 
        for j in range(i+1, largo): 
            if vector_seleccion[minimo] > vector_seleccion[j]: 
                minimo = j 
                
        # Cambiamos el elemento minimo encontrado con el primer elemento de la matriz
        vector_seleccion[i], vector_seleccion[minimo] = vector_seleccion[minimo], vector_seleccion[i]
        # Repetimos el proceso hasta terminar
    print("SELECCIÓN: Ordenado con Selección: ",vector_seleccion)

selectionsort(vector_seleccion)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
print('---------------------------------------------------------------------------------------------------------') #separador
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#SHELL O INCREMENTO DECRECIENTE

lista_de_numeros_4 = list(range(1, 11)) # Creamos la lista base con números del 1 al 100

# Creamos una lista aleatoria con sample 
#(8 elementos aleatorios de la lista base)
vector_shell = sample(lista_de_numeros_4,10)

def shellsort(vector_shell):

    print("SHELL: El vector SIN ordenar es:", vector_shell)
    
    largo = 0
    
    for i in vector_shell:
        largo += 1
    
    distancia = largo // 2
    
     # Creamos un bucle según las distancias
    while distancia > 0:
        # Utilizamos el Insertionsort
        for i in range(distancia, largo):
            val = vector_shell[i]
            j = i
            while j >= distancia and vector_shell[j - distancia] > val:
                vector_shell[j] = vector_shell[j - distancia]
                j -= distancia
            vector_shell[j] = val
        distancia //= 2 # Acotamos la distancia nuevamente y continua el ciclo
    print("SHELL: Ordenado con Shell: ", vector_shell)
    
shellsort(vector_shell)