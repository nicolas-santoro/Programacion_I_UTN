from funciones import *

import json



validar_2 = False
validar_5 = False

while True:
    print("""================================================
            1) Leer desde CSV / JSON
            2) Dar de alta.
            3) Modificar.
            4) Eliminar.
            5) Mostrar todos.
            6) Mostrar gerentes.
            7) Mostrar Analistas con sueldo mayor a $500000.
            8) Calcular salario promedio.
            9) Ordenar empleados.
            10) Salir.
        ================================================""")
    
    opcion = input('Seleccione una opción: ')

    match opcion:
        case  '1':
            if validar_2 == True and validar_5 == True:
                eleccion = input('Ingrese desde dónde quiere leer la lista de empleados (CSV / JSON): ').upper()

                if eleccion == 'CSV' or eleccion == 'JSON' and eleccion != False:
                    if eleccion == 'CSV':
                        with open('ABM_Archivos/empleados.csv', 'r') as archivo:
                            for linea in archivo.readlines():
                                linea.replace('\n', '')

                                print(linea)
                    
                    if eleccion == 'JSON':
                        with open('ABM_Archivos/empleados.json', 'r') as archivo:
                            data = json.load(archivo)

                            print(data)

                else:
                    eleccion = input('Ingrese correctamente desde dónde quiere leer la lista de empleados (CSV / JSON): ')
                    eleccion = eleccion.upper()

            else:
                print('Tiene que ingresar empleados primero...')

        case '2':
            empleado = dar_de_alta()

            agregar_empleado(lista_empleados, empleado)

            validar = True

        case '3':
            if validar == True:
                print(modificar_empleado(lista_empleados))
            
            else:
                print('Tiene que ingresar empleados primero...')

        case '4':
            if validar == True:
                print(eliminar_empleado(lista_empleados))

            else:
                print('Tiene que ingresar empleados primero...')

        case '5':
            if validar == True:
                mostrar_empleados(lista_empleados)

                validar_5 = True

            else:
                print('Tiene que ingresar empleados primero...')

        case '6':
            if validar == True:
                mostrar_gerentes(lista_empleados)

            else:
                print('Tiene que ingresar empleados primero...')

        case '7':
            if validar == True:
                mostrar_analistas(lista_empleados)

            else:
                print('Tiene que ingresar empleados primero...')

        case '8':
            if validar == True:
                calcular_salario_promedio(lista_empleados)

            else:
                print('Tiene que ingresar empleados primero...')
        
        case '9':
            if validar == True:
                ordenar_empleados(lista_empleados.copy())

            else:
                print('Tiene que ingresar empleados primero...')
        
        case '10':
            break

        case _:
            print('Seleccione una opción válida: ')