def mostrar_matriz(matriz: list) -> None:
    '''
    Función para poder mostrar la matriz (una vez ya reemplazada).
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]:4}', end = ' ')

        print('')

def se_pueden_multiplicar(matriz_a, matriz_b) -> bool:
    '''
    Función que verifica si ambas matrices son compatibles para la multiplicación.

    Retorna TRUE si son compatibles, retorna FALSE si no lo son.
    '''
    if len(matriz_a[0]) == len(matriz_b):
        return True
    else:
        return False



def multiplicar_matrices(matriz_a: list, matriz_b: list) -> None:
    '''
    Función para multiplicar las matrices A y B.

    Se le otroga una ´matriz_a´ (que la da el usuario), y una matriz_b (que también se la da el usuario).

    Determina que la matriz_resultado (el resultado de la multiplicación entre ambas matrices) tenga la mismas filas que la matriz_a y las mismas columnas que la matriz_b.

    Multiplica ambas matrices siguiendo el procedimiento (fila1 * columna1  + fila2 * columna2 ...).

    Retorna la matriz_resultado ya reemplazada por los valores de las sumas de las multiplicaciones.
    '''
    filas_resultado = len(matriz_a)
    columnas_resultado = len(matriz_b[0])

    matriz_resultado = [[0] * columnas_resultado for _ in range(filas_resultado)]


    for i in range(filas_resultado):
        for j in range(columnas_resultado):
            for k in range(len(matriz_a[0])):
                matriz_resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]
    
    return matriz_resultado


def ingresar_matriz(filas, columnas):
    '''
    Función que sirve para crear las matrices (A y B) en base a la cantidad de filas y columnas que otorga el usuario.

    También le dice al usuario en qué posición está, sumándole 1 a los índices para que pueda entender mejor (se programa 0, 1, 2, ... . Normalmente se cuenta 1, 2, 3, ...).

    Retorna la matriz ya creada (sea la A o la B).
    '''
    matriz = []

    for i in range(filas):
        fila = []

        for j in range(columnas):
            valor = float(input(f"Ingrese el elemento en la posición ({i+1}, {j+1}): "))

            fila += [valor]

        matriz += [fila]

    return matriz