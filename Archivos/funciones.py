#1:
def guardar_numeros(lista: list, path: str):
    archivo = open(path, 'w')

    for i in range(len(lista)):
        archivo.write(f'{lista[i]}\n')


    archivo.close()

#2:
def leer_multiplos_2(path: str):
    archivo = open(path, 'r')

    for linea in archivo.readlines():
        linea.replace('\n', '')
        linea = int(linea)

        if linea % 2 == 0:
            print(f'{linea}')


    archivo.close()

#3:
def traspasar_archivo(path_origen: str, path_destino: str):
    archivo_1 = open(path_origen, 'r')

    archivo_original = archivo_1.readlines()

    archivo_1.close()


    guardar_numeros(archivo_original, path_destino)

#4:
def contar_elementos(path: str):
    cantidad_lineas = 0

    cantidad_palabras = 0

    cantidad_caracteres = 0


    with open(path, 'r') as poema:
        for linea in poema:
            cantidad_lineas += 1
            

            cantidad_caracteres += len(linea)
            
            
            palabras = linea.split()

            cantidad_palabras += len(palabras)

    
    datos = {
        "cantidad_lineas": cantidad_lineas,
        "cantidad_palabras": cantidad_palabras,
        "cantidad_caracteres": cantidad_caracteres
    }


    return datos