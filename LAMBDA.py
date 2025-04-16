lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#A:
cuadrados = list(map(lambda numero: numero ** 2, lista_numeros))

#B:
pares = list(filter(lambda numero: numero % 2 == 0, lista_numeros))



palabras_1 = ['hola', 'mundo', 'python', 'lambda']


#C:
mayusculas = list(map(lambda palabra: palabra.upper(), palabras_1))



palabras_2 = ['¡hola!', 'mundo?', 'python', 'lambda', 'pedro73']


#D:
alfabeticos = list(filter(lambda palabra: palabra.isalpha(), palabras_2))



lista_diccionarios = personas = [
    {'nombre': 'Juan', 'edad': 15},
    {'nombre': 'Ana', 'edad': 22},
    {'nombre': 'Pedro', 'edad': 19},
    {'nombre': 'María', 'edad': 17},
    {'nombre': 'Laura', 'edad': 20}
]


#E:
edad_mayores = list(filter(lambda persona: persona['edad'] > 18, lista_diccionarios))

#F:
nombre_mayusculas = list(map(lambda persona: persona['nombre'].upper(), lista_diccionarios))