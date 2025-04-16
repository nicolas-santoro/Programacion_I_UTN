lista_z = [42, -17, 93, 58, -22, 76, -5, 34, 87, 9, 93]

lista_n = ['Nicolás', 'Lucio', 'Mateo', 'Valentín', 'Tobías', 'Matías', 'Mateo', 'Lautaro', 'Alma', 'Catalina', 'Lola', 'Mateo']

#1: Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números:
def calcular_promedio(lista: list) -> float:
    acumulador = 0
    for i in range(len(lista)):
        acumulador += lista[i]
    
    promedio = acumulador / len(lista)

    return promedio



#2: Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos:
def calcular_promedio_positivos(lista: list) -> float:
    acumulador = 0
    for i in range(len(lista)):
        if lista[i] > 0:
            acumulador += lista[i]
    
    promedio = acumulador / len(lista)

    return promedio



#3: Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro:
def calcular_producto(lista: list) -> float:
    acumulador = 1
    for i in range(len(lista)):
            acumulador *= lista[i]

    return acumulador



#4: Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado:
def posicionar_maximo(lista: list) -> int:
    for i in range(len(lista)):
        if i == 0 or lista[i] > valor_maximo:
            valor_maximo = lista[i]
            inidce_maximo = i

    return inidce_maximo



#5: Escribir una función que reciba como parámetros una lista de enteros y muestre la/s posicion/es en donde se encuentra el valor máximo hallado:
def mostrar_maximo(lista: list):
    for i in range(len(lista)):
        if i == 0 or lista[i] > valor_maximo:
            valor_maximo = lista[i]

    for i in range(len(lista)):
        if valor_maximo == lista[i]:
            indice_maximo = i + 1

            print(f'El valor máximo es {valor_maximo} y se encuentra en el índice {indice_maximo}.')



#6: Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista de nombres, un nombre a reemplazar y su correspondiente reemplazo. 
#   La función debe reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente reemplazo y luego retornar la cantidad total de reemplazos realizados:
def reemplazar_nombres(lista: list, nombre_a_reemplazar: str, nombre_de_reemplazo: str) -> None:
    contador = 0
    for i in range(len(lista)):
        if lista[i] == nombre_a_reemplazar:
            lista[i] = nombre_de_reemplazo

            contador += 1
    
    return contador