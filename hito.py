#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#EJERCICIO 1:

#Parte hecha por Eloy

#lo primero, necesitaremos importar randint de random para trabajar
from random import randint

#declaramos una función donde meteremos todo
def numerosAleatorios(n=10):
    #creamos un set VACÍO para almacenar de los 10 números, los que NO SE REPITAN 
    numeroslocos={}
    #aquí hacemos el bucle
    while True:
        #el numero generado, lo generaremos del 0-10 un total de 10 veces (el range(n) significa que hará el rango de las veces que hayamos puesto la función, en este caso n=10)
        numgenerado={randint(0, 10) for _ in range(n)}
        #ESTO ES MUY IMPORTANTE. SI EL NÚMERO GENERADO NO COINCIDE CON NINGUNO DEL SET, SE ALMACENA EN ESTE, PERO SI SE REPITE, PASA AL SIGUIENTE
        if numgenerado!=numeroslocos:
            numeroslocos = numgenerado
            break
    
    #nos devuelve el set con los números generados y almacenados ya
    return numeroslocos

#en otra variable que se llama igual, almacenamos la function
numeroslocos = numerosAleatorios()
#printeamos
print(numeroslocos)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#