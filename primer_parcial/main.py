from peliculas import *



while True:
    menu = print("""
    1) Dar de alta.
    2) Modificar.
    3) Eliminar.
    4) Mostrar peliculas.
    5) Ordenar peliculas.
    6) Buscar pelicula por titulo.
    7) Calcular promedio.
    8) Calcular porcentaje.
    9) Mostrar por género.
    10) Salir.
    """)

    option = input('Seleccione una opción: ')

    if validar_entero(option) == True:
        option = int(option)

        match option:
            case 1:
                pelicula = dar_de_alta_pelicula(cine)

                agregar_pelicula(cine, pelicula)

            case 2:
                modificar_pelicula(cine)

            case 3:
                eliminar_pelicula(cine)

            case 4:
                mostrar_peliculas(cine)
            
            case 5:
                ordenar_peliculas(cine)
            
            case 6:
                buscar_titulo(cine)
            
            case 7:
                calcular_promedios(cine)
            
            case 8:
                calcular_porcentajes(cine)

            case 9:
                mostrar_por_genero(cine)
            
            case 10:
                '''
                El siguiente código se encarga de guardar la lista 'cine' al archivo 'peliculas_3.csv'

                Luego de guardar toda la lista al archivo CSV, le comunica al usuario que se guardó con éxito y se despide cordialmente.
                '''
                lista = cine


                campos = ['ID', 'Título', 'Género', 'Año de lanzamiento', 'Duración', 'ATP', 'Plataformas']

                with open('primer_parcial/peliculas_3.csv', 'w', encoding = 'utf-8') as cartelera:
                    cartelera.write(','.join(campos) + '\n')

                    for pelicula in range(len(lista)):
                        fila = []

                        if lista[pelicula]['ATP'] == True:
                            lista[pelicula]['ATP'] = 'Si'

                        else:
                            lista[pelicula]['ATP'] = 'No'

                        plataforma = lista[pelicula]['Plataformas']
                        plataformas = ', '.join(plataforma)

                        for i in range(len(campos)):
                            valor = lista[pelicula][campos[i]]

                            fila.append(str(valor))
                
                        cartelera.write(','.join(fila) + '\n')
                
                print('Lista de películas guardada exitosamente en un archivo CSV. ¡Que tenga lindo dia!')


                break
    
    else:
        option = input('¡Ingrese una opción valida!: ')