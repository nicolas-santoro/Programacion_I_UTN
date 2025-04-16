from data_stark import lista_personajes
from funciones import *



#2)
def nombre_genero_nb(lista: list) -> list:
    lista_vacia = []

    for i in range(len(lista)):
        if lista[i]['genero'] == 'NB':
            lista_vacia.append(lista[i])
    

    return stark_imprimir_heroes(lista_vacia)

#3)
def mas_alta(lista: list):
    lista_auxiliar = []

    for i in range(len(lista)):
        if lista[i]['genero'] == 'F':
            lista_auxiliar.append(lista[i])
    
    altitud_f = obtener_maximo(lista_auxiliar, 'altura')

    for i in range(len(lista_auxiliar)):
        if lista_auxiliar[i]['altura'] == altitud_f:
            alta = obtener_nombre_y_dato(lista_auxiliar[i], 'altura')

    
    return alta

#4)
def mas_alto(lista: list):
    lista_auxiliar = []

    for i in range(len(lista)):
        if lista[i]['genero'] == 'M':
            lista_auxiliar.append(lista[i])
    
    altitud_m = obtener_maximo(lista_auxiliar, 'altura')

    for i in range(len(lista_auxiliar)):
        if lista_auxiliar[i]['altura'] == altitud_m:
            alto = obtener_nombre_y_dato(lista_auxiliar[i], 'altura')

    
    return alto

#5)
def mas_debil_m(lista: list):
    lista_auxiliar = []

    for i in range(len(lista)):
        if lista[i]['genero'] == 'M':
            lista_auxiliar.append(lista[i])
    
    debilidad_m = obtener_minimo(lista_auxiliar, 'fuerza')

    for i in range(len(lista_auxiliar)):
        if lista_auxiliar[i]['fuerza'] == debilidad_m:
            debil_m = obtener_nombre_y_dato(lista_auxiliar[i], 'fuerza')

    
    return debil_m

#6)
def mas_debil_nb(lista: list):
    lista_auxiliar = []

    for i in range(len(lista)):
        if lista[i]['genero'] == 'NB':
            lista_auxiliar.append(lista[i])
    
    debilidad_nb = obtener_minimo(lista_auxiliar, 'fuerza')

    for i in range(len(lista_auxiliar)):
        if lista_auxiliar[i]['fuerza'] == debilidad_nb:
            debil_nb = obtener_nombre_y_dato(lista_auxiliar[i], 'fuerza')

    
    return debil_nb

#7)
def promedio_fuerza_nb(lista: list):
    lista_auxiliar = []

    for i in range(len(lista)):
        if lista[i]['genero'] == 'NB':
            lista_auxiliar.append(lista[i])
    
    fuerza_promedio_nb = calcular_promedio(lista_auxiliar, 'fuerza')

    
    return fuerza_promedio_nb

#8)
def contar_ojos(lista: list):
    colores = []

    for i in range (len(lista)):
        color = lista[i]['color_ojos']

        colores.append(color)


    frecuencias = {}

    for color in colores:
        if color in frecuencias:
            frecuencias[color] += 1

        else:
            frecuencias[color] = 1

    return frecuencias

#9)
def contar_pelo(lista: list):
    colores = []

    for i in range (len(lista)):
        color = lista[i]['color_pelo']

        colores.append(color)


    frecuencias = {}

    for color in colores:
        if color in frecuencias:
            frecuencias[color] += 1

        else:
            frecuencias[color] = 1


    return frecuencias


#10)
def agrupar_color_ojos(lista: list):
    colores = []

    for i in range (len(lista)):
        color = lista[i]['color_ojos'], lista[i]['nombre']

        colores.append(color)


    for j in range(len(colores)):
        for i in range(len(colores) - 1 - j):
            if colores[i] > colores[i + 1]:
                auxiliar = colores[i]
                colores[i] = colores[i + 1]
                colores[i + 1] = auxiliar


    return colores


#11)
def agrupar_tipo_inteligencia(lista: list):
    inteligentes = []

    for i in range (len(lista)):
        inteligencia = lista[i]['inteligencia'], lista[i]['nombre']

        inteligentes.append(inteligencia)


    for j in range(len(inteligentes)):
        for i in range(len(inteligentes) - 1 - j):
            if inteligentes[i] > inteligentes[i + 1]:
                auxiliar = inteligentes[i]
                inteligentes[i] = inteligentes[i + 1]
                inteligentes[i + 1] = auxiliar


    return inteligentes
            


validar = False

while True:
    menu = print("""
    1) Normalizar datos.
    2) Nombre de cada superhéroe de género NB.
    3) Superhéroe más alto de género F.
    4) Superhéroe más alto de género M.
    5) Superhéroe más débil de género M.
    6) Superhéroe más débil de género NB.
    7) Fuerza promedio de los superhéroes de género NB.
    8) Superhéroes que tienen cada tipo de color de ojos.
    9) Superhéroes que tienen cada tipo de color de pelo.
    10) Lista de todos los superhéroes agrupados por color de ojos.
    11) Lista de todos los superhéroes agrupados por tipo de inteligencia.
    12) Salir
    """)

    option = int(input("Seleccione una opción: "))

    match option:   
        case  1:
            validar = True
           
            if stark_normalizar_datos(lista_personajes) == True:
                print('Normalización realizada...')

            else:
                print('Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente')


        case 2:
            if validar == True:
                nombre_genero_nb(lista_personajes)

            else:
                print("Ingrese la opción A")

        case 3:
            if validar == True:
                print(f'La altura del personaje Femenino más alta es: {mas_alto(lista_personajes)}')

            else:
                print("Ingrese la opción A")

        case 4:
            if validar == True:
                print(f'La altura del personaje Masculino más alto es: {mas_alto(lista_personajes)}')

            else:
                print("Ingrese la opción A")

        case 5:
            if validar == True:
                print(f'El personaje Masculino más débil es: {mas_debil_m(lista_personajes)}')

            else:
                print("Ingrese la opción A")

        case 6:
            if validar == True:
                print(f'El personaje No Binario más débil es: {mas_debil_nb(lista_personajes)}')

            else:
                print("Ingrese la opción A")

        case 7:
            if validar == True:
                print(f'El promedio de la fuerza de l@s No Binarios es de: {promedio_fuerza_nb(lista_personajes)}')

            else:
                print("Ingrese la opción A")
        
        case 8:
            if validar == True:
                print(f'La cantidad de colores de ojos que hay dentro de la lista es la siguiente: {contar_ojos(lista_personajes)}')

            else:
                print("Ingrese la opción A")
        
        case 9:
            if validar == True:
                print(f'La cantidad de colores de pelo que hay dentro de la lista es la siguiente: {contar_pelo(lista_personajes)}')

            else:
                print("Ingrese la opción A")
        
        case 10:
            if validar == True:
                print(agrupar_color_ojos(lista_personajes))

            else:
                print("Ingrese la opción A")
        
        case 11:
            if validar == True:
                print(agrupar_tipo_inteligencia(lista_personajes))

            else:
                print("Ingrese la opción A")

        case 12:
            break

        case _:
            print("Opción no válida. Intente de nuevo.")