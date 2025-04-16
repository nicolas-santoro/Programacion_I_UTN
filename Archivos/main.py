from funciones import *



lista = [43, 17, 92, 6, 83, 55, 71, 23, 38, 96]

guardar_numeros(lista, 'Archivos/Numeros.txt')

leer_multiplos_2('Archivos/Numeros.txt')

traspasar_archivo('Archivos/Numeros.txt', 'Archivos/Numeros_2.txt')

print(contar_elementos('Archivos/Poema.txt'))