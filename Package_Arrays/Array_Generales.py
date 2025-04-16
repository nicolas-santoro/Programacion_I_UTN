from .Específicas import *
def contador_positivos_negativos(lista: list) -> None:
    contador_positivos = 0
    contador_negativos = 0

    for number in lista:
        if determinar_positividad(number):
            contador_positivos += 1

        elif number < 0:
            contador_negativos += 1

    print(f"Positivos: {contador_positivos}, Negativos: {contador_negativos}")



def sumar_pares(lista: list) -> None:
    acumulador_pares = 0

    for i in range (len(lista)):
        if validar_paridad(lista[i]) == True:
            acumulador_pares += lista[i]
    
    print(acumulador_pares)



def listar_todos(lista: list) -> None:
    print("Números ingresados: ", lista)