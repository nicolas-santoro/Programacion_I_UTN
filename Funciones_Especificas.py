'''
Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
Crear una función que le solicite al usuario el ingreso de una cadena y la retorna. 
Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.
Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.
'''
#1
def pedir_entero() -> int:
    numero_e = int(input('Ingrese un número entero: '))
    return numero_e

#2
def pedir_flotante() -> float:
    numero_f = float(input('Ingrese un número flotante (con coma): '))
    return numero_f

#3
def pedir_cadena() -> str:
    cadena = input('Ingrese caracteres (texto): ')
    return cadena

#4
def pedir_n_entero(mensaje:str, rango_1:int, rango_2:int) -> int:
    numero_e = int(input(mensaje))

    while numero_e < rango_1 or numero_e > rango_2:
        numero_e = int(input(mensaje))

    return numero_e


def pedir_n_flotante(mensaje:str, rango_1:float, rango_2:float) -> float:
    numero_f = float(input(mensaje))

    while numero_f < rango_1 or numero_f > rango_2:
        numero_f = float(input(mensaje))

    return numero_f


def pedir_cadena_texto(mensaje:str) -> str:
    cadena = input(mensaje)

    while cadena == None:
        cadena = input(mensaje)

    return cadena

#5
def calcular_area(radio:float) -> float:
    '''
    Ésta función calcula el área de un cículo.

    Parámetros:
        radio(float): Recibe el radio del área a calcular.
    
    Retorna:
        El área calculada.
    '''

    pi = 3.14
    area = pi * (radio ** 2)

    return area

area = calcular_area(2.5)
print(area)

#6
def definir_par_o_impar(numero:int) -> None:
    mensaje = 'El número seleccionado es impar.'

    if numero % 2 == 0:
        mensaje = 'El número seleccionado es par.'
    print(mensaje)

#7
def encontrar_maximo(numero_1, numero_2, numero_3):
    if numero_1 >= numero_2 and numero_1 >= numero_3:
        return numero_1
    elif numero_2 >= numero_1 and numero_2 >= numero_3:
        return numero_2
    else:
        return numero_3

numero_1 = float(input('Ingrese el primer número: '))
numero_2 = float(input('Ingrese el segundo número: '))
numero_3 = float(input('Ingrese el tercer número: '))

maximo = encontrar_maximo(numero_1, numero_2, numero_3)
print(f'El número máximo es: {maximo}')

#8
def encontrar_potencia():
    base = float(input('Ingrese la base: '))
    exponente = int(input('Ingrese el exponente: '))

    resultado = base ** exponente

    print(f'El resultado es: {resultado}.')

encontrar_potencia()