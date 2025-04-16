def bubble_sort_menor(lista: list):
    """
    Ordena una lista de números enteros en orden ascendente utilizando el algoritmo de ordenamiento Bubble Sort.

    Argumentos:
        lista (list): La lista de números enteros a ordenar.

    Retorna:
        list: La lista ordenada en orden ascendente.

    Ejemplo de uso:
        >>> lista_desordenada = [5, 2, 4, 1, 3]
        >>> lista_ordenada = bubble_sort_menor(lista_desordenada)
        >>> print(lista_ordenada)
        [1, 2, 3, 4, 5]
    """
    for j in range(len(lista)):
        for i in range(len(lista) - 1 - j):
            if lista[i] > lista[i + 1]:
                auxiliar = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = auxiliar


def bubble_sort_mayor(lista: list):
    """
    Ordena una lista de números enteros en orden descendente utilizando el algoritmo de ordenamiento Bubble Sort.

    Argumentos:
        lista (list): La lista de números enteros a ordenar.

    Retorna:
        list: La lista ordenada en orden descendente.

    Ejemplo de uso:
        >>> lista_desordenada = [5, 2, 4, 1, 3]
        >>> lista_ordenada = bubble_sort_mayor(lista_desordenada)
        >>> print(lista_ordenada)
        [5, 4, 3, 2, 1]
    """
    for j in range(len(lista)):
        for i in range(len(lista) - 1 - j):
            if lista[i] < lista[i + 1]:
                auxiliar = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = auxiliar



def selection_sort(lista: list):
    """
    Ordena una lista de números enteros utilizando el algoritmo de ordenamiento por selección.

    Argumentos:
        lista (list): La lista de números enteros a ordenar.

    Retorna:
        list: La lista ordenada.

    Ejemplo de uso:
        >>> lista_desordenada = [5, 2, 4, 1, 3]
        >>> lista_ordenada = selection_sort(lista_desordenada)
        >>> print(lista_ordenada)
        [1, 2, 3, 4, 5]
    """
    for i in range(len(lista) - 1):
        min_index = i
        
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        
        if min_index != i:
            lista[i], lista[min_index] = lista[min_index], lista[i]
    
    return lista



def partition(lista: list, indice_primer_elemento: int, indice_ultimo_elemento: int):
    """
    Particiona una lista de números enteros en dos sublistas utilizando el algoritmo de ordenamiento rápido.

    Argumentos:
        lista (list): La lista de números enteros a particionar.
        indice_primer_elemento (int): El índice del primer elemento de la sublista izquierda.
        indice_ultimo_elemento (int): El índice del último elemento de la lista.

    Retorna:
        int: El índice del pivote en la lista.

    Ejemplo de uso:
        >>> lista = [5, 2, 4, 1, 3]
        >>> indice_pivote = partition(lista, 0, len(lista) - 1)
        >>> print(indice_pivote)
        3
        >>> print(lista)
        [1, 2, 3, 5, 4]
    """
    pivot = lista[indice_ultimo_elemento]
    
    i = indice_primer_elemento - 1

    for j in range(indice_primer_elemento, indice_ultimo_elemento):
        if lista[j] <= pivot:
            i += 1
            
            lista[i], lista[j] = lista[j], lista[i]

    lista[i + 1], lista[indice_ultimo_elemento] = lista[indice_ultimo_elemento], lista[i + 1]

    return i + 1

def quick_sort(lista: list, indice_primer_elemento: int, indice_ultimo_elemento: int):
    """
    Ordena una lista de números enteros utilizando el algoritmo de ordenamiento rápido.

    Argumentos:
        lista (list): La lista de números enteros a ordenar.
        indice_primer_elemento (int): El índice del primer elemento de la sublista.
        indice_ultimo_elemento (int): El índice del último elemento de la lista.

    Ejemplo de uso:
        >>> lista_desordenada = [5, 2, 4, 1, 3]
        >>> quick_sort(lista_desordenada, 0, len(lista_desordenada) - 1)
        >>> print(lista_desordenada)
        [1, 2, 3, 4, 5]
    """
    if indice_primer_elemento < indice_ultimo_elemento:
        indice_pivot = partition(lista, indice_primer_elemento, indice_ultimo_elemento)

        quick_sort(lista, indice_primer_elemento, indice_pivot - 1)
        
        quick_sort(lista, indice_pivot + 1, indice_ultimo_elemento)



def merge_sort(lista: list):
    """
    Ordena una lista de números enteros utilizando el algoritmo de ordenamiento por mezcla.

    Argumentos:
        lista (list): La lista de números enteros a ordenar.

    Retorna:
        list: La lista ordenada.

    Ejemplo de uso:
        >>> lista_desordenada = [5, 2, 4, 1, 3]
        >>> lista_ordenada = merge_sort(lista_desordenada)
        >>> print(lista_ordenada)
        [1, 2, 3, 4, 5]
    """
    def merge_sort_recursiva(lista, indice_primer_elemento, indice_ultimo_elemento):
        if indice_primer_elemento < indice_ultimo_elemento:
            mitad = (indice_primer_elemento + indice_ultimo_elemento) // 2
            
            merge_sort_recursiva(lista, indice_primer_elemento, mitad)
            
            merge_sort_recursiva(lista, mitad + 1, indice_ultimo_elemento)
            
            merge(lista, indice_primer_elemento, mitad, indice_ultimo_elemento)

    def merge(lista, indice_primer_elemento, mitad, indice_ultimo_elemento):
        tamaño_izquierda = mitad - indice_primer_elemento + 1  # Tamaño de la parte izquierda
        tamaño_derecha = indice_ultimo_elemento - mitad
        
        izquierda = [0] * tamaño_izquierda
        derecha = [0] * tamaño_derecha
        
        for i in range(tamaño_izquierda):
            izquierda[i] = lista[indice_primer_elemento + i]
        
        for j in range(tamaño_derecha):
            derecha[j] = lista[mitad + 1 + j]
        

        i = 0
        j = 0
        k = indice_primer_elemento
        
        while i < tamaño_izquierda and j < tamaño_derecha:
            if izquierda[i] <= derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1
        
        while i < tamaño_izquierda:
            lista[k] = izquierda[i]
            i += 1
            k += 1
        
        while j < tamaño_derecha:
            lista[k] = derecha[j]
            j += 1
            k += 1


    merge_sort_recursiva(lista, 0, len(lista) - 1)



def insertion_sort(lista: list):
    """
    Ordena una lista de números enteros utilizando el algoritmo de ordenamiento por inserción.

    Argumentos:
        lista (list): La lista de números enteros a ordenar.

    Retorna:
        list: La lista ordenada.

    Ejemplo de uso:
        >>> lista_desordenada = [5, 2, 4, 1, 3]
        >>> lista_ordenada = insertion_sort(lista_desordenada)
        >>>
        >>> print(lista_ordenada)
        [1, 2, 3, 4, 5]
    """
    for i in range(1, len(lista)):
        llave = lista[i]
        
        j = i - 1

        while j >= 0 and lista[j] > llave:
            lista[j + 1] = lista[j]

            j -= 1
        
        lista[j + 1] = llave


    return lista



def counting_sort(lista):
    """
    Ordena una lista de números enteros utilizando el algoritmo de ordenamiento por conteo.

    Argumentos:
        lista (list): La lista de números enteros a ordenar.

    Retorna:
        list: La lista ordenada.

    Ejemplo de uso:
        >>> lista_desordenada = [5, 2, 4, 1, 3]
        >>> lista_ordenada = counting_sort(lista_desordenada)
        >>> print(lista_ordenada)
        [1, 2, 3, 4, 5]
    """
    valor_maximo = lista[0]

    for i in lista[1:]:
        if i > valor_maximo:
            valor_maximo = i    

    auxiliar_frecuencia = [0] * (valor_maximo + 1)
    
    for j in lista:
        auxiliar_frecuencia[j] += 1
    
    for i in range(1, len(auxiliar_frecuencia)):
        auxiliar_frecuencia[i] += auxiliar_frecuencia[i - 1]
    

    auxiliar_ordenado = [0] * len(lista)
    
    for j in lista:
        auxiliar_ordenado[auxiliar_frecuencia[j] - 1] = j
        auxiliar_frecuencia[j] -= 1


    return auxiliar_ordenado



def bucket_sort(lista: list):
    """
    Ordena una lista de números enteros utilizando el algoritmo de ordenamiento por cubetas.

    Argumentos:
        lista (list): La lista de números enteros a ordenar.

    Retorna:
        list: La lista ordenada.

    Ejemplo de uso:
        >>> lista_desordenada = [5, 2, 4, 1, 3]
        >>> lista_ordenada = bucket_sort(lista_desordenada)
        >>> print(lista_ordenada)
        [1, 2, 3, 4, 5]
    """
    valor_maximo = lista[0]

    for numero in lista[1:]:
        if numero > valor_maximo:
            valor_maximo = numero
    
    n = len(lista)

    num_buckets = valor_maximo // n + 1


    cubetas = [[] for _ in range(num_buckets)]

    cantidad_cubetas = [0] * num_buckets
    
    for num in lista:
        indice = num // num_buckets

        if indice >= num_buckets:
            indice = num_buckets - 1  # Ajustar el índice si es mayor o igual al número de cubetas

        if cantidad_cubetas[indice] == len(cubetas[indice]):
            cubetas[indice] += [0] * n

        cubetas[indice][cantidad_cubetas[indice]] = num

        cantidad_cubetas[indice] += 1
    

    for i in range(num_buckets):
        # Ordenar la cubeta actual
        j = 1

        while j < cantidad_cubetas[i]:
            key = cubetas[i][j]

            k = j - 1

            while k >= 0 and cubetas[i][k] > key:
                cubetas[i][k + 1] = cubetas[i][k]

                k -= 1

            cubetas[i][k + 1] = key

            j += 1
    

    cubeta_ordenada = [0] * n

    indice = 0

    for i in range(num_buckets):
        for j in range(cantidad_cubetas[i]):
            cubeta_ordenada[indice] = cubetas[i][j]
            indice += 1
    

    return cubeta_ordenada



def heapify(lista, n, i):
    """
    Convierte una sublista en un heap máximo.

    Argumentos:
        lista (list): La lista de números enteros.
        n (int): El tamaño de la lista.
        i (int): El índice del elemento actual.

    Ejemplo de uso:
        >>> lista = [5, 2, 4, 1, 3]
        >>> heapify(lista, len(lista), 0)
        >>> print(lista)
        [5, 4, 3, 1, 2]
    """
    mas_largo = i

    izquierda = 2 * i + 1

    derecha = 2 * i + 2

    if izquierda < n and lista[izquierda] > lista[mas_largo]:
        mas_largo = izquierda

    if derecha < n and lista[derecha] > lista[mas_largo]:
        mas_largo = derecha

    if mas_largo != i:
        lista[i], lista[mas_largo] = lista[mas_largo], lista[i]

        heapify(lista, n, mas_largo)

def heap_sort(lista):
    """
    Ordena una lista de números enteros utilizando el algoritmo de ordenamiento por heapsort.

    Argumentos:
        lista (list): La lista de números enteros a ordenar.

    Retorna:
        list: La lista ordenada.

    Ejemplo de uso:
        >>> lista_desordenada = [5, 2, 4, 1, 3]
        >>> lista_ordenada = heap_sort(lista_desordenada)
        >>> print(lista_ordenada)
        [1, 2, 3, 4, 5]
    """
    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]

        heapify(lista, i, 0)


def counting_sort_radix(lista, exponente):
    """
    Ordena una lista de números enteros utilizando el algoritmo de ordenamiento por conteo con base en la técnica radix.

    Argumentos:
        lista (list): La lista de números enteros a ordenar.
        exponente (int): El exponente a utilizar para el ordenamiento.

    Retorna:
        list: La lista ordenada.

    Ejemplo de uso:
        >>> lista_desordenada = [523, 179, 436, 123, 498]
        >>> lista_ordenada = counting_sort_radix(lista_desordenada, 1)
        >>> print(lista_ordenada)
        [123, 179, 436, 498, 523]
    """
    n = len(lista)

    salida = [0] * n

    cuenta = [0] * 10

    for i in range(n):
        index = (lista[i] // exponente) % 10
        cuenta[index] += 1

    for i in range(1, 10):
        cuenta[i] += cuenta[i - 1]

    i = n - 1

    while i >= 0:
        index = (lista[i] // exponente) % 10

        salida[cuenta[index] - 1] = lista[i]

        cuenta[index] -= 1

        i -= 1

    for i in range(n):
        lista[i] = salida[i]

def radix_sort(lista):
    """
    Ordena una lista de números enteros utilizando el algoritmo de ordenamiento radix.

    Argumentos:
        lista (list): La lista de números enteros a ordenar.

    Retorna:
        list: La lista ordenada.

    Ejemplo de uso:
        >>> lista_desordenada = [523, 179, 436, 123, 498]
        >>> lista_ordenada = radix_sort(lista_desordenada)
        >>> print(lista_ordenada)
        [123, 179, 436, 498, 523]
    """
    numero_maximo = lista[0]

    for numero in lista:
        if numero > numero_maximo:
            numero_maximo = numero


    exponente = 1

    while numero_maximo // exponente > 0:
        counting_sort_radix(lista, exponente)

        exponente *= 10



def shell_sort(lista):
    """
    Ordena una lista de números enteros utilizando el algoritmo de ordenamiento Shell Sort.

    Argumentos:
        lista (list): La lista de números enteros a ordenar.

    Retorna:
        list: La lista ordenada.

    Ejemplo de uso:
        >>> lista_desordenada = [5, 2, 4, 1, 3]
        >>> lista_ordenada = shell_sort(lista_desordenada)
        >>> print(lista_ordenada)
        [1, 2, 3, 4, 5]
    """
    n = len(lista)

    intervalo = n // 2  # Inicializar el intervalo

    while intervalo > 0:
        for i in range(intervalo, n):
            auxiliar = lista[i]

            j = i

            while j >= intervalo and lista[j - intervalo] > auxiliar:
                lista[j] = lista[j - intervalo]

                j -= intervalo

            lista[j] = auxiliar

        intervalo //= 2