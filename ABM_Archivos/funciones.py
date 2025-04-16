import json


lista_empleados = []

if lista_empleados == []:
    ide = 1

else:
    ultimo_empleado = len(lista_empleados)

    ide = lista_empleados[ultimo_empleado]['id'] + 1


def dar_de_alta() -> dict:
    global ide
    
    nombre = input('Ingrese el nombre: ')
    nombre = nombre.capitalize()


    while nombre.isalpha() == False or len(nombre) > 20:
        nombre = input('Error, ingrese un nombre válido: ')
        nombre = nombre.capitalize()


    apellido = input('Ingrese el apellido: ')
    apellido = apellido.capitalize()

    while apellido.isalpha() == False or len(apellido) > 20:
        apellido = input('Error, ingrese un apellido válido: ')
        apellido = apellido.capitalize()


    puesto = input('Ingrese el puesto (Gerente / Supervisor / Analista / Encargado / Asistente): ')
    puesto = puesto.lower()

    while puesto != "gerente" and puesto != "supervisor" and puesto != "encargado" and puesto != "asistente":
        puesto = input('Error, ingrese un puesto existente (Gerente / Supervisor / Analista / Encargado / Asistente): ')
        puesto = puesto.lower()


    salario = int(input("Ingrese el salario: "))

    while salario < 234315:
        salario = int(input('Error, ingrese un salario válido: '))


    nuevo_empleado = {
        "id": ide,
        "nombre": nombre,
        "apellido": apellido,
        "puesto": puesto,
        "salario": salario
        }

    ide += 1


    return nuevo_empleado

def agregar_empleado(lista: list, empleado: dict) -> None:
    if empleado != {}:
        lista.append(empleado)
    
    else:
        print('Error, el diccionario esta vacío: ')


def modificar_empleado(lista: list) -> str:
    retorno = ""

    bandera_id = False

    id = int(input('Ingrese el ID del empleado: '))

    if lista != []:
        for i in range(len(lista)):
            if id == lista[i]['id']:
                bandera_id = True

                while True:
                    opcion = print("Ingrese una opcion a modificar: \n 1. Nombre \n 2. Apellido \n 3. Puesto \n 4. Salario \n 5. Salir")

                    match opcion:
                        case "1":
                            nombre = input("Ingrese el nuevo nombre...")

                            while nombre.isalpha() == False or len(nombre) > 15:
                                nombre = input("Error, reingrese el nuevo nombre...")
                            
                            lista[i]["nombre"] = nombre

                            retorno = "Se modificó el nombre..."

                        case "2":
                            apellido = input("Ingrese el nuevo apellido...")

                            while apellido.isalpha() == False or len(nombre) > 15:
                                apellido = input("Error, reingrese el nuevo apellido...")

                            lista[i]["apellido"] = apellido

                            retorno = "Se modificó el apellido..."

                        case "3":
                            puesto = input("Ingrese el nuevo puesto (Gerente / Supervisor / Analista / Encargado / Asistente)...").lower()

                            while puesto != "gerente" and puesto != "supervisor" and puesto != "encargado" and puesto != "asistente":
                                puesto = input("Error, reingrese el nuevo puesto (Gerente / Supervisor / Analista / Encargado / Asistente)...").lower()

                            lista[i]["puesto"] = puesto

                            retorno = "Se modificó el puesto..."
                            
                        case "4":
                            salario = int(input("Ingrese el nuevo monto de salario..."))

                            while salario < 234315:
                                salario = int(input("Error, reingrese el nuevo monto de salario..."))

                            lista[i]["salario"] = salario

                            retorno = "Se modificó el salario..."

                        case "5":
                            break

                        case _:
                            print("¡Ingrese una opción válida!")


                break

        if retorno == '':
            retorno = 'No se reailzaron modificaciones'

        if bandera_id == False:
            retorno = 'No existe un empleado con ese ID'


        return retorno

def eliminar_empleado(lista: list) -> str:
    retorno = ''

    id = int(input('Ingrese el ID del empleado: '))

    for i in range(len(lista)):
        if id == lista[i]['id']:
            empleado_eliminado = lista.pop(i)

            retorno = f'Se ha eliminado al empleado {empleado_eliminado['nombre']} {empleado_eliminado['apellido']}'

        break

    if retorno == '':
        retorno = 'No existe un empleado con ese ID'
    

    return retorno

def mostrar_empleado(empleado: dict) -> str:
    mensaje = f"""********************************************************************************************
                ID: {empleado['id']}.
                Nombre: {empleado["nombre"]}.
                Apellido: {empleado["apellido"]}.
                Puesto: {empleado["puesto"]}.
                Salario: ${empleado["salario"]}.
                ********************************************************************************************"""
    

    return mensaje

def mostrar_empleados(lista: list):
    for i in range(len(lista)):
        informacion = mostrar_empleado(lista[i])

        print(informacion)
    
    deseo = input('¿Desea buscar alguno en específico? (Si / No)').lower()


    with open('ABM_Archivos/empleados.json', 'w') as archivo:
        json.dump(lista_empleados, archivo, indent = 4, ensure_ascii = False)

    with open('ABM_Archivos/empleados.csv', 'w') as archivo:
        for i in range(len(lista_empleados)):
            archivo.write(f'{lista_empleados[i]}')
    
    key = ''

    if deseo == 'si':
        opcion = int(input('''Seleccione cuál quiere buscar: 
            1) Empleados con determinado puesto.
            2) Empleados con determinado salario.
            3) Empleados con determinado apellido.
            '''))
        
        orden = input('Ingrese el orden en el cuál quiere ordenar (Ascendente / Descendente): ').lower()
        

        if opcion == 1:
            key == 'puesto'

            determinada_key = input('Ingrese qué puesto quiere buscar (Gerente / Supervisor / Analista / Encargado / Asistente): ')
        
        elif opcion == 2:
            key == 'salario'

            determinada_key = int(input('Ingrese el salario a buscar: '))

            for i in range(len(lista)):
                if lista[i][key] <= determinada_key:
                    if orden == 'ascendente':
                        for j in range(len(lista)):
                            for i in range(len(lista) - 1 - j):
                                if lista[i] > lista[i + 1]:
                                    auxiliar = lista[i]
                                    lista[i] = lista[i + 1]
                                    lista[i + 1] = auxiliar
                    
                        print(mostrar_empleado(lista[i]))
                    
                    else:
                        for j in range(len(lista)):
                            for i in range(len(lista) - 1 - j):
                                if lista[i] < lista[i + 1]:
                                    auxiliar = lista[i]
                                    lista[i] = lista[i + 1]
                                    lista[i + 1] = auxiliar
                        
                        print(mostrar_empleado(lista[i]))
        
        else:
            key == 'apellido'

            determinada_key = input('Ingrese el appelido a buscar: ')
        

        if opcion != 2:
            for i in range(len(lista)):
                if lista[i][key] == determinada_key:
                    if orden == 'ascendente':
                        for j in range(len(lista)):
                            for i in range(len(lista) - 1 - j):
                                if lista[i] > lista[i + 1]:
                                    auxiliar = lista[i]
                                    lista[i] = lista[i + 1]
                                    lista[i + 1] = auxiliar
                    
                        print(mostrar_empleado(lista[i]))
                    
                    else:
                        for j in range(len(lista)):
                            for i in range(len(lista) - 1 - j):
                                if lista[i] < lista[i + 1]:
                                    auxiliar = lista[i]
                                    lista[i] = lista[i + 1]
                                    lista[i + 1] = auxiliar
                        
                        print(mostrar_empleado(lista[i]))


def mostrar_gerentes(lista: list) -> str:
    gerentes = []

    for i in range(len(lista)):
        if lista[i]["puesto"] == "Gerente":
            mostrar_empleado(lista[i])

            gerentes.append(lista[i])

        else:
            mensaje = "No hay empleados con ese puesto"


            return mensaje
    
    with open('gerentes.json', 'w') as archivo:
        json.dump(gerentes, archivo, indent = 4, ensure_ascii = False)

    with open('gerentes.csv', 'w') as archivo:
        for i in range(len(gerentes)):
            archivo.write(f'{gerentes[i]}\n')


def mostrar_analistas(lista: list):
    for i in range(len(lista)):
        if lista[i]["puesto"] == "analista" and lista[i]["salario"] >= 500000:
            mostrar_empleado(lista[i])


def calcular_salario_promedio(lista: list) -> float:
    acumulador = 0

    contador = 0

    for i in range(len(lista)):
        acumulador += lista[i]["salario"]

        contador += 1

    promedio = acumulador / contador

    with open('salario_promedio.txt', 'w') as archivo:
        archivo.write(f'El promedio de salarios de todos los empleados es de: {promedio}')


    return print(f'El promedio de salarios de todos los empleados es de: {promedio}')


def ordenar_empleados(lista: list):
    while True:
        clave = input("ingrese cuál dato quiere ordenar (nombre / apellido / salario): ").lower()

        if clave in ("nombre", "apellido", "salario"):
            orden = input("Ingrese el orden de ordenamiento (ascendente / descendente): ").lower()

            if orden == "ascendente":
                for j in range(len(lista)):
                    for i in range(len(lista) - 1 - j):
                        if lista[i][clave] > lista[i + 1][clave]:
                            auxiliar = lista[i]
                            lista[i] = lista[i + 1]
                            lista[i + 1] = auxiliar
                
                print(f"\nEmpleados ordenados por {clave} {orden}:")

                mostrar_empleados(lista)

            elif orden == 'descendente':
                for j in range(len(lista)):
                    for i in range(len(lista) - 1 - j):
                        if lista[i][clave] < lista[i + 1][clave]:
                            auxiliar = lista[i]
                            lista[i] = lista[i + 1]
                            lista[i + 1] = auxiliar
                
                print(f"\nEmpleados ordenados por {clave} {orden}:")

                mostrar_empleados(lista)

            else:
                print("Error, ingrese nuevamente cuál dato quiere ordenar (nombre / apellido / salario): ")

        else:
            print("Error, ingrese nuevamente el orden de ordenamiento (ascendente / descendente): ")