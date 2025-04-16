from validaciones import *

import json



separadores = ',-'
'''Es para  que el .split() detecte tanto comas como guiones cuando el usuario ingresa o reingresa las plataformas en las cuales una película está disponible.'''


def dar_de_alta_pelicula(lista: list) -> dict:
    '''
    La función se encarga de dar de alta una película y de verificar que cada dato esté bien ingresado.

    Recibe como parámetro una lista (en ésta ocación, la lista ¨Cine¨) para obtener los títulos y los IDs de las películas ya existentes.

    Le pide al usuario el título, el género, el año de lanzamiento, la duración, el ATP y las plataformas disponibles de una película.

    Dicha información la guarda en un diccionario y lo retorna.

    Después, en el 'main.py', se guarda en la lista de las películas del CSV ¨Cine¨.
    '''
    titulos_cartelera = []

    ides_cartelera = []

    for i in range(len(lista)):
        titulo_en_cartelera = lista[i]['Título']
        titulos_cartelera.append(titulo_en_cartelera)

        ides_en_cartelera = lista[i]['ID']
        ides_cartelera.append(ides_en_cartelera)


    titulo = input('Ingrese el nombre de la pelicula: ')

    for i in range(len(titulos_cartelera)):
        while len(titulo) > 20 and titulo == titulos_cartelera[i]:
            titulo = input('Error, ingrese una pelicula válida: ')    


    print('''Generos disponibles:
                          'Acción', 'Aventura', 'Animación', 'Biográfico', 'Comedia', 'Comedia romántica', 'Comedia dramática', 'Crimen, Documental', 
                          'Drama', 'Fantasía', 'Histórico', 'Infantil', 'Musical', 'Misterio', 'Policíaco', 'Romance','Ciencia ficción', 'Suspenso', 
                          'Terror','Western', 'Bélico', 'Deportivo', 'Noir', 'Experimental', 'Familiar', 'Superhéroes', 'Espionaje', 'Artes marciales', 
                          'Fantástico', 'Catástrofe', 'Melodrama', 'Erótico', 'Cine independiente', 'Zombies', 'Vampiros', 'Cyberpunk', 'Steampunk', 
                          'Distopía', 'Utopía', 'Road Movie', 'Docuficción', 'Mockumentary', 'Gótico', 'Slasher', 'Adolescente', 'Culto', 'Maravilloso'
                        ''')
    
    validar_genero = False

    genero = input('Ingrese el genero de la pelicula: ')
    genero = genero.capitalize()
    
    for i in range(len(generos_disponibles)):
        if genero == generos_disponibles[i]:
            validar_genero = True

    if validar_genero == False:
        genero = input('Error, ingrese un genero válido: ')
        genero = genero.capitalize()


    anio = input('Ingrese el año de lanzamiento de la pelicula (1888 - 2024): ')

    while validar_entero(anio) == False:
        anio = input('Error, ingrese un año de lanzamiento de la pelicula válido (1888 - 2024): ')

    anio = int(anio)


    duracion = input("Ingrese la duracion de la pelicula (en minutos): ")

    while validar_entero(duracion) == False:
        duracion = input('Error, ingrese una duracion de válida (en minutos): ')

    duracion = int(duracion)


    atp = input('La pelicula, ¿es Apta para Todo Publico? (si / no): ')
    atp = atp.lower()

    if atp == 'si':
        atp = True
        
    elif atp == 'no':
        atp = False
        
    else:
        atp = input('Error, ingrese una de las opciones válidas (si / no):')
        atp = atp.lower()
    

    plataforma = input('Ingrese en cuáles plataformas es posible ver la pelicula: ')

    for i in range(len(plataforma)):
        while validar_entero(plataforma[i]) == True or len(plataforma[i]) > 20:
            plataforma = input('Eror, reingrese en cuáles plataformas es posible ver la pelicula: ')

    
    ide = (obtener_maximo(ides_cartelera) + 1)
 
    nueva_pelicula = {
        'ID': ide,
        'Título': titulo,
        'Género': genero,
        'Año de lanzamiento': anio,
        'Duración': duracion,
        'ATP': atp,
        'Plataformas': plataforma.split(separadores)
        }
    

    return nueva_pelicula

def agregar_pelicula(lista: list, pelicula: dict):
    '''
    Ésta función se encarga de agregar el diccionario (que sería la película ingresada por el usuario) a la lista.

    Tanto la lista donde se va a guardar la nueva película, como el diccionario que sería la película en sí, los recibe como parámetros.

    No devuelve específicamente nada, imprime un mesaje que le comunica que su película fue agregada exitosamente a la lista.
    '''
    if pelicula != {}:
        lista.append(pelicula)

        print('¡Su pelicula ha sido agregada a la cartelera exitosamente!')

    else:
        print('Error, el diccionario esta vacío: ')


def modificar_pelicula(lista: list):
    '''
    Ésta función se encarga de modificar cualquier dato de cualquier película dentro de una lista.

    Dicha lista la recibe como parámetro.

    La función le pregunta al usuario el título de la película a modificar.

    Si existe, mediante un sub-menú, le pregunta al usuario cuál es el dato que quiere modificar.

    Finalmente, le pide que ingrese el nuevo dato y modifica la lista original.

    No retorna nada en específico, solamente notifica al usuario la cantidad de cambios efectuados o si hubo algún percance (que el título no exista o que no se hayan hecho cambios).
    '''
    contador_modificaciones = 0
    modificacion = False

    bandera_titulo = False

    titulo_clave = input('Ingrese el titulo de la pelicula a modificar: ')

    
    for pelicula in range(len(lista)):
        if titulo_clave == lista[pelicula]['Título']:
            bandera_titulo = True

            while True:
                print('''
                    1) Titulo.
                    2) Genero.
                    3) Año.
                    4) Duracion.
                    5) Aptitud (si es Apta para Todo Publico o no)
                    6) Plataformas.
                    7) Salir.
                    ''')
                
                option = input('Seleccione una opcion: ')
                
                if validar_entero(option) == True:
                        option = int(option)
    
                        match option:
                            case 1:
                                titulo = input('Ingrese el nuevo nombre de la pelicula: ')

                                for pelicula in range(len(lista)):
                                    titlulo_en_cartelera = lista[pelicula]['Título']


                                while len(titulo) > 20 and titulo != titlulo_en_cartelera:
                                    titulo = input('Error, ingrese una pelicula válida: ')
                                
                                lista[pelicula]['Título'] = titulo


                                print('Se modificó el titulo de la pelicula...')

                                modificacion = True

                                contador_modificaciones += 1

                            case 2:
                                validar_genero = False

                                genero = input('Ingrese el nuevo genero de la pelicula: ')
                                genero = genero.capitalize()
                                
                                for i in range(len(generos_disponibles)):
                                    if genero == generos_disponibles[i]:
                                        validar_genero = True

                                if validar_genero == False:
                                    genero = input('Error, ingrese un genero válido: ')
                                    genero = genero.capitalize()
                                
                                lista[pelicula]['Género'] = genero

                                print('Se modificó el genero de la pelicula...')

                                modificacion = True

                                contador_modificaciones += 1

                            case 3:
                                anio = input('Ingrese el nuevo año de lanzamiento de la pelicula (1888 - 2024): ')

                                while validar_entero(anio) == False:
                                    anio = input('Error, ingrese un año de lanzamiento de la pelicula válido (1888 - 2024): ')

                                anio = int(anio)

                                lista[pelicula]['Año de lanzamiento'] = anio

                                print('Se modificó el año de estreno de la pelicula...')

                                modificacion = True

                                contador_modificaciones += 1
                                
                            case 4:
                                duracion = input('Ingrese la nueva duracion de la pelicula (en minutos): ')

                                while validar_entero(duracion) == False:
                                    duracion = input('Error, ingrese una duracion de válida (en minutos): ')

                                duracion = int(duracion)

                                lista[pelicula]['Duración'] = duracion

                                print('Se modificó el año de estreno de la pelicula...')

                                modificacion = True

                                contador_modificaciones += 1
                            
                            case 5:
                                atp = input('La pelicula, ¿es Apta para Todo Publico? (si / no): ').lower()

                                if atp == 'si':
                                    atp = True
                                
                                elif atp == 'no':
                                    atp = False

                                else:
                                    atp = input('Error, ingrese una de las opciones validas (si / no): ').lower()

                                lista[pelicula]['ATP'] = atp

                                print('Se modificó la aptitud de la pelicula...')

                                modificacion = True

                                contador_modificaciones += 1

                            case 6:
                                plataforma = input('Ingrese en cuáles plataformas es posible ver la pelicula ahora: ')

                                for i in range(len(plataforma)):
                                    while validar_entero(plataforma[i]) == True or len(plataforma[i]) > 20:
                                        plataforma = input('Eror, reingrese en cuáles plataformas es posible ver la pelicula: ')
                                
                                lista[pelicula]['Plataformas'] = plataforma.split(separadores)

                                print('Se modificó en que plataformas es posible ver la pelicula...')

                                modificacion = True

                                contador_modificaciones += 1

                            case 7:
                                print(f'Se hicieron {contador_modificaciones} modificaciones...')
                                break

                            case _:
                                print('¡Ingrese una opción válida!')


            break

    if modificacion == False:
        print('No se reailzaron modificaciones...')

    if bandera_titulo == False:
        print('¡No existe ninguna pelicula con ese titulo!')

def eliminar_pelicula(lista: list):
    '''
    Ésta función se encarga de eliminar completamente una película de la lista de diccionarios el cual contiene las películas.

    Le pregunta al usuario qué película quiere eliminar y, si existe, mediante un .remove() elimina el diccionario que representa dicha película.

    No retorna nada en específico, pero le notifica al usuario que su película fue eliminada exitosamente (o que no se encontró, si no existe dicho título).
    '''
    titulo = input('Ingrese el titulo de la pelicula que desea eliminar: ')

    for pelicula in range(len(lista)):
        if titulo == lista[pelicula]['Título']:
            lista.remove(lista[pelicula])

            print('Se ha eliminado la película con éxito')

            break

    else:
        print('No se encontró ninguna película con ese título, lo sentimos.')
    

def molde_peliculas(lista: list):
    '''
    Ésta función se encarga de crear el ¨molde¨ con el cual se van a imprimir las películas.

    Recibe como perámetro una lista para poder encontrar los datos requeridos he imprimirlos.

    No devuelve nada específico, pero imprime todos los datos de forma ordenada.
    '''
    print('*' * 166)
    print(f'''| {'Título':48} | {'Género':20} | {'Año de lanzamiento':18} | {'Duración':13} | {'ATP':3} | {'Plataformas':45} |''')
    print('-' * 166)

    for i in range(len(lista)):
        if lista[i]['ATP'] == True:
            atp = 'Sí'
    
        else:
            atp = 'No'

        plataforma = lista[i]['Plataformas']
        plataformas = ', '.join(plataforma)
        
        print(f'| {lista[i]['Título']:48} | {lista[i]['Género']:20} | {str(lista[i]['Año de lanzamiento']):18} | {str(lista[i]['Duración']):5} minutos | {atp:3} | {plataformas:45} |')

    print('*' * 166)


def mostrar_peliculas(lista: list):
    '''
    Ésta función se encarga de imprimir las películas (usando el molde de las películas) según lo pida el usuario.

    Recibe como parámetro una lista para poder buscar he imprimir los datos.

    Mediante un sub-menú, le pregunta al usuario qué quiere imprimir, ya sea por categoría o por un dato específico (género, año, plataforma)

    Finalmente, imprime los datos pedidos de forma ordenada (gracias al molde de las películas).
    '''
    while True:
        print('''
                1) Todas las películas.
                2) De determinado género.
                3) De determinado año.
                4) Todas las ATP
                5) Todas las No ATP.
                6) De determinada plataforma.
                7) Salir.
                ''')
        
        option = input('Ingrese una de las opciones: ')

        if validar_entero(option) == True:
            option = int(option)

            match option:
                case 1:
                    molde_peliculas(lista)

                case 2:
                    print('''Generos disponibles:
                          'Acción', 'Aventura', 'Animación', 'Biográfico', 'Comedia', 'Comedia romántica', 'Comedia dramática', 'Crimen, Documental', 
                          'Drama', 'Fantasía', 'Histórico', 'Infantil', 'Musical', 'Misterio', 'Policíaco', 'Romance','Ciencia ficción', 'Suspenso', 
                          'Terror','Western', 'Bélico', 'Deportivo', 'Noir', 'Experimental', 'Familiar', 'Superhéroes', 'Espionaje', 'Artes marciales', 
                          'Fantástico', 'Catástrofe', 'Melodrama', 'Erótico', 'Cine independiente', 'Zombies', 'Vampiros', 'Cyberpunk', 'Steampunk', 
                          'Distopía', 'Utopía', 'Road Movie', 'Docuficción', 'Mockumentary', 'Gótico', 'Slasher', 'Adolescente', 'Culto', 'Maravilloso'
                        ''')
                    
                    genero_a_elegir = input('Ingrese el genero que quiera buscar: ')
                    genero_a_elegir = genero_a_elegir.capitalize()


                    for i in range(len(generos_disponibles)):
                        while genero_a_elegir.isalpha() == False and genero_a_elegir != generos_disponibles[i]:
                            genero_a_elegir = input('Error, ingrese un genero válido: ')
                            genero_a_elegir = genero_a_elegir.capitalize()

                    genero_elegido = []

                    for i in range(len(lista)):
                        if lista[i]['Género'] == genero_a_elegir:
                            genero_elegido.append(lista[i])

                    
                    molde_peliculas(genero_elegido)
                
                case 3:
                    anio_a_elegir = input('Ingrese el año de lanzamiento de la pelicula (1888 - 2024): ')

                    while validar_entero(anio_a_elegir) == False:
                        anio_a_elegir = input('Error, ingrese un año de lanzamiento de la pelicula válido (1888 - 2024): ')

                    anio_a_elegir = int(anio_a_elegir)

                    anio_elegido = []

                    for i in range(len(lista)):
                        if lista[i]['Año de lanzamiento'] == anio_a_elegir:
                            anio_elegido.append(lista[i])
                    
                    molde_peliculas(anio_elegido)
                
                case 4:
                    atp_si = []

                    for i in range(len(lista)):
                        if lista[i]['ATP'] == True:
                            atp_si.append(lista[i])
                    
                    molde_peliculas(atp_si)
                
                case 5:
                    atp_no = []

                    for i in range(len(lista)):
                        if lista[i]['ATP'] == False:
                            atp_no.append(lista[i])
                    
                    molde_peliculas(atp_no)
                
                case 6:
                    plataforma_a_elegir = input('Ingrese en que plataforma se encuentra la pelicula: ')

                    for i in range(len(plataforma_a_elegir)):
                        while validar_entero(plataforma_a_elegir[i]) == True or len(plataforma_a_elegir[i]) > 20:
                            plataforma_a_elegir = input('Eror, reingrese en cuáles plataformas es posible ver la pelicula: ')
                    
                    plataforma_elegida = []

                    for i in range(len(lista)):
                        for j in range(len(lista[i]['Plataformas'])):
                              if lista[i]['Plataformas'][j].strip() == plataforma_a_elegir:
                                plataforma_elegida.append(lista[i])

                    molde_peliculas(plataforma_elegida)
                
                case 7:
                    break

        else:
            option = input('Ingrese una opción valida: ')

def ordenar_peliculas(lista: list):
    '''
    Ésta función se encarga de ordenar las películas según una clave específica.

    Recibe como parámetro una lista para poder ordenar los elementos de dicha lista.

    Dicha clave específica se lo pregunta al usuario mediante un sub-menú. También le pregunta el orden (si lo quiere de forma ascendente o descendente).

    Utilizando la función bubble_sort(), le otroga la lista, la clave y el orden y ordena efectivamente la lista.

    Finalmente, utilizando el molde de las películas, imprime y le muestra al usuario la lista completamente ordenada.
    '''
    while True:
        print('''
                1) Título.
                2) Género.
                3) Año de lanzamiento.
                4) Duración.
                5) Salir.
                ''')
        
        option = input('Ingrese una de las opciones: ')

        if option == '5':
            break
            
        orden = input('¿En qué orden quiere ordenarlo? (Ascendente / Descendente): ').lower()

        if validar_entero(option) == True and orden == 'ascendente' or orden == 'descendente':
            option = int(option)

            if option == 1:
                clave = 'Título'

            elif option == 2:
                clave = 'Género'

            elif option == 3:
                clave = 'Año de lanzamiento'
            
            elif option == 4:
                clave = 'Duración'

            ordenado = bubble_sort(lista, clave, orden)

            molde_peliculas(ordenado)

        else:
            option = input('Ingrese una opción valida: ')

            orden = input('Elija entre ascendente y descendente, por favor:').lower()


def buscar_titulo(lista: list):
    '''
    Ésta función se encarga de buscar el título de una película dentro de la lista de diccionarios (la cual recibe como parámetro).

    Recorre la lista y, si encuentra el título ingresado por el usuario, imprime con el molde dicha película.

    También utiliza la función preguntar_seguir() para saber si el usuario desea buscar otra película más o si desea irse del programa. 
    '''
    titulo_a_buscar = input('Ingrese el titulo de la pelicula que desee buscar: ')

    titulo_econtrado = []

    for i in range(len(lista)):
        if lista[i]['Título'] == titulo_a_buscar:
            titulo_econtrado.append(lista[i])

            molde_peliculas(titulo_econtrado)
        
    if titulo_econtrado == []:
        print('Lamentablemente no pudimos encontrar su pelicula, lo sentimos :(...')
        print('-------------------------------------------------------------------')
        print('Recuerde que puede usar la opción 1 del menú principal para dar de alta la pelicula que desee :)')
    

    deseo = preguntar_seguir()

    if deseo == True:
        buscar_titulo(lista)
    
    else:
        print('¡Que disfrute de las otras opciones!')

def calcular_promedios(lista: list):
    '''
    Ésta función calcula el promedio de un dato dentro de la lista que recibe como parámetro.

    Usando un sub_menú, le pregunta al usuario sobre qué dato quiere saber el promedio.

    Ya obtenido dicho dato, usa la función calcular_promedio() para calcular el promedio de dicho dato.

    Finalmente, imprime el promedio de dicho dato.
    '''
    acumulador_anio = 0
    acumulador_duracion = 0

    while True:
        print('''
                1) Año de lanzamiento.
                2) Duración de las películas.
                3) Salir.
                ''')
        
        option = input('Ingrese una de las opciones: ')

        if validar_entero(option) == True:
            option = int(option)

            match option:
                case 1:
                    for i in range(len(lista)):
                        acumulador_anio += lista[i]['Año de lanzamiento']

                    promedio = calcular_promedio(lista, acumulador_anio)

                    print(f'El promedio de los años de lanzamientos de las peliculas es de {int(promedio)} años.')

                case 2:
                    for i in range(len(lista)):
                        acumulador_duracion += lista[i]['Duración']

                    promedio = calcular_promedio(lista, acumulador_duracion)

                    print(f'El promedio de duracion de las peliculas es de {int(promedio)} minutos.')

                case 3:
                    break
        
        else:
            option = input('Ingrese una opción valida: ')


def calcular_porcentajes(lista: list):
    '''
    Ésta función calcula el porcentaje de un dato dentro de la lista que recibe como parámetro.

    Usando un sub_menú, le pregunta al usuario sobre qué dato quiere saber el porcentaje.

    Ya obtenido dicho dato, usa la función dividir() para calcular el porcentaje de dicho dato.

    Finalmente, imprime el porcentaje de dicho dato.
    '''
    acumulador_genero = 0

    acumulador_atp_si = 0
    acumulador_atp_no = 0

    cantidad_total_respuestas = (len(lista))

    while True:
        print('''
                1) Porcentaje por genero.
                2) Porcentaje por ATP (Apto para Todo Publico).
                3) Salir.
                ''')
        
        option = input('Ingrese una de las opciones: ')

        if validar_entero(option) == True:
            option = int(option)

            match option:
                case 1:
                    validar_genero = False

                    print('''Generos disponibles:
                          'Acción', 'Aventura', 'Animación', 'Biográfico', 'Comedia', 'Comedia romántica', 'Comedia dramática', 'Crimen, Documental', 
                          'Drama', 'Fantasía', 'Histórico', 'Infantil', 'Musical', 'Misterio', 'Policíaco', 'Romance','Ciencia ficción', 'Suspenso', 
                          'Terror','Western', 'Bélico', 'Deportivo', 'Noir', 'Experimental', 'Familiar', 'Superhéroes', 'Espionaje', 'Artes marciales', 
                          'Fantástico', 'Catástrofe', 'Melodrama', 'Erótico', 'Cine independiente', 'Zombies', 'Vampiros', 'Cyberpunk', 'Steampunk', 
                          'Distopía', 'Utopía', 'Road Movie', 'Docuficción', 'Mockumentary', 'Gótico', 'Slasher', 'Adolescente', 'Culto', 'Maravilloso'
                        ''')
                    
                    genero = input('Ingrese sobre cuál genero quiere saber su porcentaje: ')

                    for i in range(len(generos_disponibles)):
                        if genero == generos_disponibles[i]:
                            validar_genero = True

                    if validar_genero == False:
                        genero = input('Error, ingrese un genero válido: ')
                        genero = genero.capitalize()


                    for i in range(len(lista)):
                        if lista[i]['Género'] == genero:
                            acumulador_genero += 1
                    
                    porcentaje = dividir(acumulador_genero, cantidad_total_respuestas) * 100

                    print(f'{genero} aparece un {int(porcentaje)}% de las veces')

                case 2:
                    for i in range(len(lista)):
                        if lista[i]['ATP'] == True:
                            acumulador_atp_si += 1
                        
                        else:
                            acumulador_atp_no += 1
                    
                    porcentaje_si = dividir(acumulador_atp_si, cantidad_total_respuestas) * 100

                    porcentaje_no = dividir(acumulador_atp_no, cantidad_total_respuestas) * 100

                    print(f'Hay un {int(porcentaje_si)}% de peliculas que son Aptas para Todo Publico.')
                    print(f'Hay un {int(porcentaje_no)}% de peliculas que NO son Aptas para Todo Publico.')

                case 3:
                    break

        else:
            option = input('Ingrese una opción valida: ')


def mostrar_por_genero(lista: list):
    peliculas_por_genero = {}

    for i in range(len(lista)):
        genero = lista[i]['Género']

        if genero not in peliculas_por_genero:
            peliculas_por_genero[genero] = []

        peliculas_por_genero[genero].append(lista[i]["Título"])
    
    for genero in peliculas_por_genero:
        titulos = peliculas_por_genero[genero]
        

        print(f"{genero}: {', '.join(titulos)}.")
        print(f"Total de películas de género {genero.lower()}: {len(titulos)}.\n")

    
    with open('primer_parcial/peliculas_por_genero.json', 'w', encoding='utf-8') as archivo:
        json.dump(peliculas_por_genero, archivo, ensure_ascii = False, indent = 4)