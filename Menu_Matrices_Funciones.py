import random

# Mostrar la matriz
def mostrar_matriz(matriz:list)-> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]: 4}', end='')


# Generar legajos para choferes (3 líneas, 5 choferes cada una)
matriz_choferes = [[0] * 5 for _ in range(3)]


def brindar_legajos (matriz_vacia:list) -> list:
    legajo = random.randint(0, 1000)

    for i in range(len(matriz_vacia)):
        for j in range(len(matriz_vacia[i])):
            legajo += 1

            matriz_vacia[i][j] = legajo

    return matriz_vacia


# Llenar la matriz de legajos
brindar_legajos(matriz_choferes)


# Crear matriz para recaudaciones (3 líneas, 5 coches cada una, con valores iniciales en 0)
matriz_recaudaciones = [[0 for _ in range(5)] for _ in range(3)]


# Validar legajo
def validar_legajo (legajo: int, matriz: list) -> bool:
    for i in range(len(matriz)):
        for j in range (len(matriz[i])):
            if matriz[i][j] == legajo:
                return True
            
    return False


# Validar línea y coche
def validar_linea (linea: int, matriz: int) -> bool:
    for i in range(len(matriz)):
        if matriz[i][0] == linea:
            return True
        
    return False


def validar_coche (coche: int, matriz: list) -> bool:
    for i in range (len(matriz)):
        for j in range (1, len(matriz[i])):
            if matriz[i][j] == coche:
                return True
            
    return False


# Cargar planilla con la matriz de recaudaciones
def cargar_planilla():
    legajo = int(input("Por favor ingrese su legajo: "))
    

    # Validar el legajo
    while not validar_legajo(legajo, matriz_choferes):
        legajo = int(input("Legajo inválido. Ingrese nuevamente: "))


    while True:
        # Validar línea y coche
        linea = int(input("Ingrese la línea de colectivos (1-3): "))

        while not validar_linea(linea):
            linea = int(input("Línea inválida. Intente nuevamente: "))


        coche = int(input("Ingrese el número de coche (1-5): "))

        while not validar_coche(coche):
            coche = int(input("Coche inválido. Intente nuevamente: "))


        recaudacion = int(input("Ingrese la recaudación del viaje: "))


        # Agregar la recaudación a la matriz de recaudaciones
        matriz_recaudaciones[linea - 1][coche - 1] += recaudacion


        # Preguntar si desea continuar
        continuar = input("¿Desea continuar? (si/no): ").lower()

        if continuar != "si":
            break


# Mostrar recaudaciones por línea y coche
def mostrar_recaudaciones():
    print("Recaudación por línea y coche:")

    for i in range(3):
        for j in range(5):
            print(f"Línea {i + 1}, Coche {j + 1}: {matriz_recaudaciones[i][j]}")


# Calcular y mostrar recaudación por línea
def recaudacion_por_linea():
    print("Recaudación por línea:")

    for i in range(3):
        total = sum(matriz_recaudaciones[i])

        print(f"Línea {i + 1}: {total}")


# Calcular y mostrar recaudación por coche
def recaudacion_por_coche():
    print("Recaudación por coche:")

    for j in range(5):
        total = sum([matriz_recaudaciones[i][j] for i in range(3)])

        print(f"Coche {j + 1}: {total}")


# Calcular y mostrar la recaudación total
def recaudacion_total():
    total = 0

    for i in range(3):
        for j in range(5):
            total += matriz_recaudaciones[i][j]

    print(f"Recaudación total: {total}")




# Menú interactivo para el usuario
menu = print("""
    A) Cargar planilla
    B) Mostrar la recaudación de todos los coches y líneas.
    C) Calcular y mostrar recaudación por línea.
    D) Calcular y mostrar recaudación por coche.
    E) Calcular y mostrar la recaudación total.
    F) Salir
    """)

bandera_validar = False

while True:
    opcion = input("Elegir una de estas opciones: ").upper()

    match opcion:
        case "A":
            bandera_validar = True
            cargar_planilla()
        case "B":
            if bandera_validar:
                mostrar_recaudaciones()
            else:
                print("Primero cargue planilla (opción A).")
        case "C":
            if bandera_validar:
                recaudacion_por_linea()
            else:
                print("Primero cargue planilla (opción A).")
        case "D":
            if bandera_validar:
                recaudacion_por_coche()
            else:
                print("Primero cargue planilla (opción A).")
        case "E":
            if bandera_validar:
                recaudacion_total()
            else:
                print("Primero cargue planilla (opción A).")
        case "F":
            break
        case _:
            print("Opción inválida, elija de nuevo.")