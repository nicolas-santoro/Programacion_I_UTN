from class_video import *
from data import *

"""
Consigna:
1. IMPLEMENTAR LOS METODOS VACIOS DE LA CLASE VIDEO

2. CREAR UN MENU DE USUARIO CON LAS SIGUIENTES OPCIONES:

A. NORMALIZAR OBJETOS: para cada video de la lista, se deberá llamar a los métodos de instancia: dividir_titulo, 
obtener_codigo_url y formatear_fecha, dado que la lista de objetos que nos pasan no cumple con las normas de estandarización 
de videos que nos solicitan.
B. MOSTRAR TEMAS: se deberá mostrar la lista de todos los temas
C. ORDENAR TEMAS: los temas se ordenarán por número de sesión de menor a mayor.
D. PROMEDIO DE VISTAS: mostrar el promedio de vistas expresado en k.
E. MAXIMA REPRODUCCION: mostrar el o los videos con mayor cantidad de vistas.
F. BUSQUEDA POR CODIGO: mostrar los videos cuyo código comiencen con la palabra "nick"
G. LISTAR POR COLABORADOR: el usuario ingresa el nombre de un colaborador y el programa deberá listar todos los videos de 
ese colaborador.
H. SALIR 

NOTA: 
1. Las opciones BCDEFG no serán accesibles si no se normalizan previamente los datos.
2. Todas las opciones tienen que estar resueltas en metodos de la clase Video que reciban una lista de videos sumado a los
parametros necesarios para lograr el objetivo y mantener independencia de código.
"""

validar = False

while True:
    menu = print("""
    A) Normalizar objetos
    B) Mostrar temas
    C) Ordenar temas
    D) Promedio de vistas
    E) Maxima reproducción
    F) Búsqueda por código
    G) Listar por colaborador
    H) Salir
    """)


    option = input("Seleccione una opción: ")
    option = option.upper()

    match option:
        case  "A":
            validar = True

            for i in range (len(lista_videos)):
                lista_videos[i].dividir_titulo()
                lista_videos[i].obtener_codigo_url()
                lista_videos[i].formatear_fecha()

            
            print('Normalización realizada...')


        case "B":
            if validar == True:
                for i in range(len(lista_videos)):
                    lista_videos[i].mostrar_tema()

            else:
                print("Ingrese la opción A")

        case "C":
            if validar == True:
                ordenar_lista(lista_videos)

                print('Canciones ordenadas...')

            else:
                print("Ingrese la opción A")

        case "D":
            if validar == True:
                promedio = calcular_promedio_vistas(lista_videos)

                print(f'El promedio de vistas de todos los videos es de {promedio} vistas')

            else:
                print("Ingrese la opción A")

        case "E":
            if validar == True:
                maximo = calcular_maxima_reproducción(lista_videos)

                print(f'El video con más reproducciones es: {maximo}')

            else:
                print("Ingrese la opción A")

        case "F":
            if validar == True:
                nick = busqueda_por_codigo(lista_videos)

                print(nick)

            else:
                print("Ingrese la opción A")

        case "G":
            if validar == True:
                colaborador = listar_por_colaborador(lista_videos)

                print(colaborador)

            else:
                print("Ingrese la opción A")

        case "H":
            break

        case _:
            print("Opción no válida. Intente de nuevo.")