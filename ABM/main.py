from funciones import *

validar = False
    
while True:
    mostrar_menu()

    opcion = input("Seleccione una opción...")

    match opcion:
        case  "1":
            empleado = crear_empleado()

            agregar_empleado(lista_empleados, empleado)

        case "2":
            print(modificar_empleado(lista_empleados))

        case "3":
            print(eliminar_empleado(lista_empleados))

        case "4":
            mostrar_empleados(lista_empleados)

        case "5":
            mostrar_gerentes(lista_empleados)

        case "6":
            promedio = calcular_salario_promedio(lista_empleados)

            print(f"El promedio de los salarios es...{promedio}")

        case "7":
            break