lista_empleados = []

if lista_empleados == []:
    ide = 1

else:
    ultimo_empleado = len(lista_empleados)

    ide = lista_empleados[ultimo_empleado]["id"] + 1

def crear_empleado() -> dict:
    global ide
    
    nombre = input("Ingrese el nombre...")

    while nombre.isalpha() == False or len(nombre) > 15:
        nombre = input("Error, reingrese el nombre...")


    apellido = input("Ingrese el apellido...")

    while apellido.isalpha() == False or len(apellido) > 15:
        apellido = input("Error, reingrese el apellido...")


    puesto = input("Ingrese el puesto (Gerente / Supervisor / Analista / Encargado / Asistente)...")

    while puesto != "Gerente" and puesto != "Supervisor" and puesto != "Encargado" and puesto != "Asistente":
        puesto = input("Error, reingrese el puesto (Gerente / Supervisor / Analista / Encargado / Asistente)...")


    salario = int(input("Ingrese el salario..."))

    while salario < 234315:
        salario = int(input("Error, reingrese el salario..."))


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
        print("Error, el diccionario esta vacío.")

def modificar_empleado(lista: list) -> str:
    retorno = ""

    bandera_id = False

    id = int(input("Ingrese el ID del empleado..."))

    if lista != []:
        for i in range(len(lista)):
            if id == lista[i]["id"]:
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
                            puesto = input("Ingrese el nuevo puesto (Gerente / Supervisor / Analista / Encargado / Asistente)...")

                            while puesto != "Gerente" and puesto != "Supervisor" and puesto != "Encargado" and puesto != "Asistente":
                                puesto = input("Error, reingrese el nuevo puesto (Gerente / Supervisor / Analista / Encargado / Asistente)...")

                            lista[i]["puesto"] = puesto

                            retorno = "Se modificó el apellido..."
                            

                        case "4":
                            salario = int(input("Ingrese el nuevo monto de salario..."))

                            while salario < 234315:
                                salario = int(input("Error, reingrese el nuevo monto de salario..."))

                            lista[i]["salario"] = salario

                            retorno = "Se modificó el apellido..."

                        case "5":
                            break

                        case _:
                            print("Ingrese una opción válida!...")

                break

        if retorno == "":
            retorno = "No se reailzaron modificaciones"

        if bandera_id == False:
            retorno = "No existe un empleado con ese ID"


        return retorno
    
def eliminar_empleado(lista: list) -> str:
    retorno = ""

    id = int(input("Ingrese el ID del empleado..."))

    for i in range(len(lista)):
        if id == lista[i]["id"]:
            empleado_eliminado = lista.pop(i)

            retorno = f"Se ha eliminado al empleado {empleado_eliminado['nombre']} {empleado_eliminado['apellido']}"

        break

    if retorno == "":
        retorno = "No existe un empleado con ese ID"
    

    return retorno

def mostrar_empleado(empleado: dict) -> str:
    mensaje = f"""********************************************************************************************
                ID: {empleado['id']}
                Nombre: {empleado["nombre"]}
                Apellido: {empleado["apellido"]}	
                Puesto: {empleado["puesto"]}
                Salario: ${empleado["salario"]}
                ********************************************************************************************"""
    

    return mensaje

def mostrar_empleados(lista: list) -> None:
    for i in range(len(lista)):
        informacion = mostrar_empleado(lista[i])

        print(informacion)


def mostrar_gerentes(lista: list) -> str:
    for i in range(len(lista)):
        if lista[i]["puesto"] == "Gerente":
            mostrar_empleado(lista[i])

        else:
            mensaje = "No hay empleados con ese puesto"


            return mensaje
        
def calcular_salario_promedio(lista: list) -> float:
    acumulador = 0

    contador = 0

    for i in range(len(lista)):
        acumulador += lista[i]["salario"]

        contador += 1

    retorno = acumulador / contador


    return retorno


def mostrar_menu() -> None:
    print("""================================================
            1. Dar de alta.
            2. Modificar.
            3. Eliminar.
            4. Mostrar todos.
            5. Mostrar gerentes.
            6. Calcular salario promedio.
            7. Salir.
            ================================================""")