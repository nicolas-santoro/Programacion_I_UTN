#1: Crear una función que reciba por parámetro una cadena y un caracter. La función deberá contar cuántas veces aparece dicho caracter en la cadena y retornar ese valor.
def contar_caracteres(cadena: str, caracter: str) -> int:
    contador = 0

    for i in range(len(cadena)):
        if cadena[i] == caracter:
            contador += 1


    return contador



#2: Crear una función que reciba una cadena y un caracter. 
#La función deberá devolver el índice en el que se encuentre la primera incidencia de dicho caracter, o -1 en caso de que no esté.
def reemplazar_caracteres(cadena: str, caracter: str, reemplazo: str) -> str:
    cadena_modificada = ""

    for i in range(len(cadena)):
        if cadena[i] != caracter:
            cadena_modificada += cadena[i]
        else:
            cadena_modificada += reemplazo
    

    return cadena_modificada



#3: Crear una función que reciba una cadena y un caracter.
#La función deberá devolver el índice en el que se encuentre la primera incidencia de dicho caracter, o -1 en caso de que no esté.
def retornar_indice(cadena: str, caracter: str) -> int:
    indice = -1

    for i in range(len(cadena)):
        if cadena[i] == caracter:
            indice = i

            break
        

    return indice



# Crear una función que reciba una cadena y retorne la misma pero al reverso.
# Ej: Si recibe la cadena “hola”, deberá retornar “aloh”.
def revertir_cadena(cadena: str) -> str:
    cadena_reverso = ""

    for i in range(len(cadena) -1, -1, -1):
        cadena_reverso += cadena[i]
    

    return cadena_reverso



#4: Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos. Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.
def suprimir_repetidos(cadena: str) -> str:
    cadena_sin_repetir = ''

    for i in range(len(cadena) - 1):
        if cadena[i] != cadena[i + 1]:
            cadena_sin_repetir += cadena[i]
    
    cadena_sin_repetir += cadena[i + 1]


    return cadena_sin_repetir



#5: Crear una función que reciba una cadena por parámetro y suprima las vocales de la misma. Ej: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”.
# def suprimir_vocales(cadena: str) -> str:
#     vocales = "aeiouAEIOU"

#     cadena_sin_vocales = ""

#     for i in cadena:
#         if i not in vocales:
#             cadena_sin_vocales += i

            
#     return cadena_sin_vocales
# def suprimir_vocales(cadena: str) -> str:
#     cadena_sin_vocales = ""

#     vocales = 'aeiouAEIOU'

#     for i in range(len(cadena)):
#         for j in range(len(vocales)):
#             if cadena[i] != vocales[i]:
#                 cadena_sin_vocales += cadena[i]

            
#     return cadena_sin_vocales

# print(suprimir_vocales('Hola hOla holA'))

#6: Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena. 
#Ej: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá retornar el valor 2.
def contar_subcadenas(cadena: str) -> str:
    pass