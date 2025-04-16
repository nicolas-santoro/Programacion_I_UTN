from data_stark import lista_personajes



#0:
def stark_normalizar_datos(lista: list) -> bool:
    retorno = False

    for i in range(len(lista)):
        if type(lista[i]['altura']) != float and type(lista[i]['peso']) != float and type(lista[i]['fuerza']) != int:
            lista[i]['altura'] = float(lista[i]['altura'])
            lista[i]['peso'] = float(lista[i]['peso'])
            lista[i]['fuerza'] = int(lista[i]['fuerza'])


            retorno = True
        

    return retorno

#1.1:
def obtener_dato(heroe: dict, dato: str) -> str | int | float | bool:
    if heroe != False and heroe != {}:
        dato = heroe.get(dato)
    
    else:
        return False


    return dato

#1.2:
def obtener_nombre(heroe: dict) -> str | bool:
    dato = obtener_dato(heroe, 'nombre')

    if dato != False:
        formato = f'Nombre: {heroe.get('nombre')}'

        return formato

    else:
        return False

#2:
def obtener_nombre_y_dato(heroe: dict, dato: str) -> str | bool:
    dato_1 = obtener_nombre(heroe)

    dato_2 = obtener_dato(heroe, dato)

    if dato_1 != False and dato_2 != False:
        formato = f'Nombre: {heroe.get('nombre')} | {dato}: {heroe.get(dato)}'

        return formato

    else: 
        return False

#3.1:
def obtener_maximo(lista: list, dato: str) -> dict | bool:
    bandera = False

    retorno = False

    if lista != []:
        for i in range(len(lista)):
            dato = obtener_dato(lista[i], dato)

            if type(dato) == int or type(dato) == float:
                if bandera == False or dato > maximo:
                    maximo = dato

                    retorno = maximo

                    bandera = True
    

    return retorno

#3.2:
def obtener_minimo(lista: list, dato: str) -> int | bool:
    bandera = False

    retorno = False

    if lista != []:
        for i in range(len(lista)):
            dato = obtener_dato(lista[i], dato)

            if type(dato) == int or type(dato) == float:
                if bandera == False or dato < minimo:
                    minimo = dato

                    retorno = minimo

                    bandera = True
    
    return retorno

#3.3:
def obtener_dato_cantidad(lista: list, valor_a_buscar: int | float, dato_a_calcular: str) -> list:
    lista_condicion = []
    
    encontrado = False

    for i in range(len(lista)):
        heroe = lista[i]

        indice_llave = 0

        while indice_llave < len(heroe):
            llave = list(heroe)[indice_llave]

            valor = heroe[llave]

            if llave == dato_a_calcular and str(valor) == str(valor_a_buscar):
                encontrado = True

                break

            indice_llave += 1

        if encontrado:
            lista_condicion.append(heroe['nombre'])

            encontrado = False


    return lista_condicion

#3.4:
def stark_imprimir_heroes(lista: list) -> bool:
    if lista == []:
        return False

    for i in range(len(lista)):
        print("************************************************************")
        print(f"Nombre: {lista[i]['nombre']}")
        print(f"Identidad: {lista[i]['identidad']}")
        print(f"Empresa: {lista[i]['empresa']}")
        print(f"Altura: {lista[i]['altura']}")
        print(f"Peso: {lista[i]['peso']}")
        print(f"Género: {lista[i]['genero']}")
        print(f"Color de ojos: {lista[i]['color_ojos']}")
        print(f"Color de pelo: {lista[i]['color_pelo']}")
        print(f"Fuerza: {lista[i]['fuerza']}")
        print(f"Inteligencia: {lista[i]['inteligencia']}")
        print("************************************************************")


    return True

#4.1:
def sumar_dato_heroe(lista: list, dato: str) -> int | float:
    acumulador = 0

    for i in range(len(lista)):
        dato_personaje = obtener_dato(lista[i], dato)

        if dato_personaje != None and type(dato_personaje) == int or type(dato_personaje) == float:
            acumulador += dato_personaje

    return acumulador

#4.2:
def dividir(dividendo: int, divisor: int) -> float | bool:
    if divisor != 0:
        resultado = dividendo / divisor


        return resultado
    
    else:
        return False

#4.3:
def calcular_promedio(lista: list, dato: str):
    suma = sumar_dato_heroe(lista, dato)

    cantidad = len(lista)

    promedio = dividir(suma, cantidad)

    return promedio

#4.4:
def mostrar_promedio_dato(lista: list, dato: str):
    if lista != None:
        promedio = calcular_promedio(lista, dato)

    if type(promedio) != float:
        return False
    
    print(f'El promedio de {dato} es: {promedio}')

#5.1:
def imprimir_menu():
    print('''
        1) Obetener nombre y cualquier dato de un personaje.
        2) Obetener el máximo de un dato (altura, peso o fuerza).
        3) Obetener el máximo de un dato (altura, peso o fuerza).
        4) Mostrar el promedio de un dato (altura, peso, fuerza)
        5) Imprimir la lista de todos los personajes.
        6) Salir.
        ''')

#5.2:
def validar_entero(numero_string: str) -> bool:
    retorno = numero_string.isdigit()
    
    return retorno

#5.3:
def stark_menu_principal(lista: list) -> int | bool:
    imprimir_menu()

    numero = input('ingrese el número de una de las opciones elegidas: ')

    if validar_entero(numero) == True:
        numero = int(numero)

        
        return numero
    
    else:
        return False

#6:
def stark_marvel_app(lista: list):
    stark_normalizar_datos(lista)

    while True:

        option = stark_menu_principal(lista)
        
        match option:
            case 1:
                for i in range(len(lista)):
                    print(i + 1)

                indice = input('Elija el índice del héroe que quiera investigar sobre él: ')
                indice = int(indice)

                dato = input('''Ingrese un dato para buscar sobre él (identidad / empresa / altura / peso / genero / color_ojos 
                            / color_pelo / fuerza / inteligencia: ''')
                dato = dato.lower()
                
                print(obtener_nombre_y_dato(lista[indice - 1], dato))
            
            case 2:
                dato = input('Ingrese el dato del que quiera saber su máximo (altura / peso / fuerza): ')
                dato = dato.lower()

                maximo = obtener_maximo(lista, dato)

                print(f'El máximo de {dato} es: {maximo}')
            
            case 3:
                dato = input('Ingrese el dato del que quiera saber su máximo (altura / peso / fuerza): ')
                dato = dato.lower()

                minimo = obtener_minimo(lista, dato)

                print(f'El mínimo de {dato} es: {minimo}')

            case 4:
                dato = input('Ingrese el dato del que quiera saber su promedio (altura / peso / fuerza): ')
                dato = dato.lower()

                mostrar_promedio_dato(lista, dato)
            
            case 5:
                stark_imprimir_heroes(lista)

            case 6:
                break

            case _:
                print("Opción no válida. Intente de nuevo.")