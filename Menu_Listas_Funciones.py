from Package_Input.input import get_int



lista = [-1] * 10

validar = False



#A: Pedir el ingreso de 10 números enteros entre -1000 y 1000:
def seleccionar_a(lista: list) -> bool:
    for i in range(len(lista)):
        lista[i] = get_int("Ingrese 10 números: ", -1000, 1000, "Número erróneo: ", 3)

    return True


#B: Mostrar la cantidad de números positivos y negativos:
def  determinar_positividad(number: int) -> bool:
    '''
    Función para determinar la positividad de un número.

    Retorna TRUE si positivo (mayor a 0).

    Retorna FALSE si es negativo (menor a 0).

    Finalmente, retorna la variable RETORNO, el cual contiene el valor booleano (TRUE o FALSE).
    '''
    retorno = None

    if number > 0:
        retorno = True

    elif number < 0:
        retorno = False

    return retorno


def contador_positivos_negativos(lista: list) -> None:
    '''
    Función para contar los números positivos y negativos por separado.

    Utiliza la función ¨determinar_positividad()¨ para determinar si el número es positivo (TRUE) o negativo (FALSE).

    En base a lo anterior, se utilizan dos contadores inicializados dentro de ésta función para contar cada vez que ¨determinar_positividad()¨ sea TRUE o FALSE.

    Finalmente, imprime la cantidad de números positivos y/o negativos que se encuentren en la lista.
    '''
    contador_positivos = 0
    contador_negativos = 0

    for number in lista:
        if determinar_positividad(number):
            contador_positivos += 1

        elif number < 0:
            contador_negativos += 1

    print(f"Positivos: {contador_positivos}, Negativos: {contador_negativos}")


#C: Mostrar la sumatoria de los números pares:
def validar_paridad(numero: int) -> bool:
    par = False

    if numero % 2 == 0:
        par = True
    
    return par


def sumar_pares(lista: list) -> None:
    acumulador_pares = 0

    for i in range (len(lista)):
        if validar_paridad(lista[i]) == True:
            acumulador_pares += lista[i]
    
    print(acumulador_pares)


#D: Informar el mayor de los números impares:
def mayor_impar(lista: list) -> int:
    mayor = None

    for i in lista:
        if i % 2 != 0:
            if mayor == None or i > mayor:
                mayor = i
    
    return mayor



#E: Imprimir todos los números ingresados:
def listar_todos(lista: list) -> None:
    print("Números ingresados: ", lista)


#F: Imprimir todos los números pares:
def listar_pares(lista: list) -> None:
    pares = [i for i in lista if validar_paridad(i)]

    print("Números pares:", pares)


#G: Imprimir los números de los índices impares:
def listar_indices_impares(lista: list) -> None:
    indices_impares = [lista[i] for i in range(1, len(lista), 2)]

    print("Números en índices impares:", indices_impares)



while True:
    print("""
    Elegir una de estas opciones:
    A. Pedir el ingreso de 10 números enteros entre -1000 y 1000.
    B. Mostrar la cantidad de números positivos y negativos.
    C. Mostrar la sumatoria de los números pares.
    D. Informar el mayor de los números impares.
    E. Listar todos los números ingresados.
    F. Listar todos los números pares.
    G. Listar los números de las posiciones impares.
    H. Salir
    """)

    option = input("Seleccione una opción: ")
    
    match option:
        case  "A":
            seleccionar_a(lista)
            validar = True

        case "B":
            if validar == True:
                contador_positivos_negativos(lista)

            else:
                print("Primero debe ingresar los 10 números.")

        case "C":
            if validar == True:
                sumar_pares(lista)

            else:
                print("Primero debe ingresar los 10 números.")

        case "D":
            if validar == True:
                mayor = mayor_impar(lista)

                if mayor != None:
                    print("Mayor de los impares:", mayor)

                else:
                    print("No hay números impares.")

            else:
                print("Primero debe ingresar los 10 números.")

        case "E":
            if validar == True:
                listar_todos(lista)
            else:
                print("Primero debe ingresar los 10 números.")

        case "F":
            if validar == True:
                listar_pares(lista)


            else:
                print("Primero debe ingresar los 10 números.")

        case "G":
            if validar == True:
                listar_indices_impares(lista)

            else:
                print("Primero debe ingresar los 10 números.")

        case "H":
            print("Saliendo...")
            break

        case _:
            print("Opción no válida. Intente de nuevo.")