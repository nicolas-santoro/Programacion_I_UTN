def validate_number(numero:int, mensaje_error:str, minimo:int | float, maximo:int | float , reintentos:int, type: str) -> int | None:
    iteraciones = 0

    while numero < minimo or numero > maximo or numero == None:
        iteraciones += 1

        input(mensaje_error)

        if iteraciones == reintentos:
            print('Se acabaron sus intentos.')
            break
    


    if type == "int":
            numero = int(numero)
            return numero
    else:
        if type == "float":
                numero = float(numero)
                return numero



def validate_length(mensaje: str, cadena: str, mensaje_error: str, longitud: int, reintentos: int) -> str | None:
    iteraciones = 0

    while cadena == None or cadena > longitud:
        iteraciones += 1

        print(mensaje_error)

        if iteraciones == reintentos:
            print('Se acabaron sus intentos.')

            return None
        
        cadena = input(mensaje)
    
    return cadena