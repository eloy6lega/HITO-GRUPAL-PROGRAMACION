# #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# #EJERCICIO 1:

# #Parte hecha por Eloy

# #lo primero, necesitaremos importar randint de random para trabajar
# from random import randint

# #declaramos una función donde meteremos todo
# def numerosAleatorios(n=10):
#     #creamos un set VACÍO para almacenar de los 10 números, los que NO SE REPITAN
#     #--------------------------------------------------------------------------------------------------------------------#
#     #SE CREA COMO DICT, LO QUE HACE QUE SE MUESTREN EN ORDEN. CAMBIAR A SET, A NO SER QUE CARMELO DIGA QUE ASÍ ESTÁ BIEN
#     #--------------------------------------------------------------------------------------------------------------------#
#     numeroslocos={}
#     #aquí hacemos el bucle
#     while True:
#         #el numero generado, lo generaremos del 0-10 un total de 10 veces (el range(n) significa que hará el rango de las veces que hayamos puesto la función, en este caso n=10)
#         numgenerado={randint(0, 10) for _ in range(n)}
#         #ESTO ES MUY IMPORTANTE. SI EL NÚMERO GENERADO NO COINCIDE CON NINGUNO DEL SET, SE ALMACENA EN ESTE, PERO SI SE REPITE, PASA AL SIGUIENTE
#         if numgenerado!=numeroslocos:
#             numeroslocos = numgenerado
#             break
    
#     #nos devuelve el set con los números generados y almacenados ya
#     return numeroslocos

# #en otra variable que se llama igual, almacenamos la function
# numeroslocos = numerosAleatorios()
# #printeamos
# print(numeroslocos)

# #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#forma 'correcta'

from random import sample 
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
#bubblesort(vector_bubblesort) #invocamos la function

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

from random import sample 
#importamos el método 'sample' de la biblioteca random para generar listas aleatorias

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