def validar_entero(numero_string: str) -> bool:
    '''
    Ésta función se encarga de validar que un string (el cual recibe como parámetro) puede ser convertido a integer.

    Retorna lo que devuelve .isdigit() (True si es que se puede transformar en integer, False si no puede).
    '''
    retorno = numero_string.isdigit()
    
    return retorno


'''
El siguiente código se encarga de almacenar los datos de las películas dentro de 'peliculas_3.csv'.

Transforma los 'Si' y los 'No' de los ATP de las películas a True (si es 'Si') o a False (si es 'No').

También ¨limpia¨ el string que representa las plataformas en las que se puede ver la película y los transforma en una lista de strings.

Si el título de la película al almacenar no fue previamente almacenado, almacena la película a la lista 'Cine'.
'''
cine = []

titulos_cargados = []

with open('primer_parcial/peliculas_3.csv', 'r', encoding = 'utf-8') as cartelera:
    pelicula = cartelera.readlines()

    for i in range(1, len(pelicula)):
        info = pelicula[i]
        info = info.split(',')

        ide = int(info[0])
        titulo = info[1]
        genero = info[2]
        anio = int(info[3])
        duracion = int(info[4])

        if info[5] == 'Si':
            atp = True
        
        else:
            atp = False

        plataformas_sucias = info[6]
        plataforma_limpia = plataformas_sucias.strip()
        plataformas_limpias = plataforma_limpia.split('-')
        plataformas_limpias[-1] = plataformas_limpias[-1].rstrip('\n')

        

        info_pelicula = {'ID': ide,
                        'Título': titulo,
                        'Género': genero,
                        'Año de lanzamiento': anio,
                        'Duración': duracion,
                        'ATP': atp,
                        'Plataformas': plataformas_limpias}

        duplicado = False

        for i in range(len(cine)):
            if cine[i]['Título'] == titulo:
                duplicado = True

                break
        
        if duplicado == False:
            cine.append(info_pelicula)
            titulos_cargados.append(titulo)

'''
Lista de strings los cuales representan los géneros disponibles, se usa para verificar que el género que el usuario ingrese exista.
'''
generos_disponibles = ['Acción', 'Aventura', 'Animación', 'Biográfico', 'Comedia', 'Comedia romántica', 'Comedia dramática',
                        'Crimen, Documental', 'Drama', 'Fantasía', 'Histórico', 'Infantil', 'Musical', 'Misterio', 'Policíaco', 'Romance',
                        'Ciencia ficción', 'Suspenso', 'Terror', 'Western', 'Bélico', 'Deportivo', 'Noir', 'Experimental', 'Familiar',
                        'Superhéroes', 'Espionaje', 'Artes marciales', 'Fantástico', 'Catástrofe', 'Melodrama', 'Erótico', 'Cine independiente', 
                        'Zombies', 'Vampiros', 'Cyberpunk', 'Steampunk', 'Distopía', 'Utopía', 'Road Movie', 'Docuficción', 'Mockumentary', 
                        'Gótico', 'Slasher', 'Adolescente', 'Culto', 'Maravilloso']



def obtener_maximo(lista: list) -> int | float:
    '''
    Ésta función se encarga de encontar el máximo de una lista.

    Retorna un integer o un float el cual representa dicho máximo.
    '''
    maximo = 0

    for i in range(1, len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]


    return maximo


def bubble_sort(lista: list, clave: str, orden: str) -> list:
    '''
    Ésta función aplica el método de ordenamiento Bubble Sort para ordenar los elementos de la lista que recibe como parámetro.

    Recibe como parámetro 3 datos: la lista a ordenar, qué ordenar dentro de dicha lista y cómo ordenarla (ascendente o descendente).

    Retorna la lista ya ordenada.
    '''
    if orden == 'ascendente':
        for j in range(len(lista)):
            for i in range(len(lista) - 1 - j):
                if lista[i][clave] > lista[i + 1][clave]:
                    auxiliar = lista[i]
                    lista[i] = lista[i + 1]
                    lista[i + 1] = auxiliar

    else:
        for j in range(len(lista)):
            for i in range(len(lista) - 1 - j):
                if lista[i][clave] < lista[i + 1][clave]:
                    auxiliar = lista[i]
                    lista[i] = lista[i + 1]
                    lista[i + 1] = auxiliar

    
    return lista


def dividir(dividendo: int | float, divisor: int | float) -> float | bool:
    '''
    Ésta función se encarga de dividir 2 elementos (los cuales los recibe por parámetro) y, si el 'divisor' no es 0, los divide entre sí.

    Retorna el resultado si el divisor es mayor a 0 o False si no se pueden dividir entre sí.
    '''
    if divisor != 0:
        resultado = dividendo / divisor


        return resultado
    
    else:
        return False


def calcular_promedio(lista: list, suma: int | float):
    '''
    Ésta función es la que se encarga de calcular el promedio de un dato dentro de una lista.

    Recibe por parámetro tanto la lista donde está el dato como el dato en sí para poder calcular el promedio
    '''
    cantidad = len(lista)

    promedio = dividir(suma, cantidad)

    return promedio



def preguntar_seguir() -> bool:
    '''
    Ésta función se encarga de preguntarle al usuario si desea continuar dentro de un sub-menú.

    Si el usuario ingresa 'si', devuelve True. Caso contrario, devuelve False.
    '''
    while True:
        deseo = input('¿Quieres continuar? (si / no): ').lower()

        if deseo == 'si':
            return True
        
        elif deseo == 'no':
            return False
        
        else:
            print('Respuesta inválida. Por favor, ingresa "si" o "no"....')