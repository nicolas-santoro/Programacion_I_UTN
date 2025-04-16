from Package_Input.input import get_int



#1 Realizar una función recursiva que calcule la suma de los primeros números naturales (todos los números anteriores al recibido por parámetro):
def sumar_naturales(numero: int) -> int:
    if numero <= 0:
        return 0
    
    else:
        return numero + sumar_naturales(numero - 1)
    

numero = get_int('Ingrese un número natural: ', 1, 500, 'Ingrese un número natural positivo: ', 3)

resultado = sumar_naturales(numero)

print(f'La suma de los primeros {numero} números es {resultado}.')



#2 Realizar una función recursiva que calcule la potencia de un número:
def calcular_potencia(base: int, exponente: int) -> int:
    if exponente == 0:
        return 1
    
    else:
        return base * calcular_potencia(base, exponente - 1)


base = get_int('Ingrese la base: ', 1, 50, 'Ingrese un número válido: ', 3)
exponente = get_int('Ingrese el exponente: ', 1, 20, 'Ingrese un número válido: ', 3)

resultado = calcular_potencia(base, exponente)

print(f'El resultado de {base} elevado a {exponente} es {resultado}')



#3 Realizar una función recursiva que realice la suma de los dígitos de un número:
def sumar_digitos(numero: int) -> int:
    if numero < 10:
        return numero
    
    ultimo_dígito = numero % 10
    resto = numero // 10

    return ultimo_dígito + sumar_digitos(resto)


numero = get_int('Ingrese cualquier número: ', 10, 99999, 'Ingrese un número válido: ', 3)
resultado = sumar_digitos(numero)

print(f'La suma de los dígitos de {numero} es {resultado}')