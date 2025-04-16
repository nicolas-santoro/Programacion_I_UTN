def pedir_numero_e(mensaje:str, mensaje_error:str, minimo:int|float, maximo:int|float, reintentos:int) -> int|None:
    '''
    mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
    mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
    mínimo: valor mínimo admitido (inclusive)
    máximo: valor máximo admitido (inclusive) 
    reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.
    '''
    iteraciones = 0

    numero = int(input(mensaje))

    while numero < minimo or numero > maximo:
        iteraciones += 1

        print(mensaje_error)
        if iteraciones == reintentos:
            print('Se acabaron sus intentos.')
            return None
        
        numero = int(input(mensaje))


pedir_numero_e('Ingrese un número entero: ', 'El número ingresado no es válido...', 1, 100, 3)



def pedir_numero_f(mensaje:str, mensaje_error:str, minimo:float, maximo:float, reintentos:int) -> float|None:
    '''
    mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
    mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
    mínimo: valor mínimo admitido (inclusive)
    máximo: valor máximo admitido (inclusive) 
    reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.
    '''
    iteraciones = 0

    numero = float(input(mensaje))

    while numero < minimo or numero > maximo:
        iteraciones += 1

        print(mensaje_error)

        if iteraciones == reintentos:
            print('Se acabaron sus intentos.')
            return None
        
        numero = float(input(mensaje))


pedir_numero_f('Ingrese cualquier número: ', 'El número ingresado no es válido...', 1, 100, 3)



def pedir_cadena(mensaje:str, mensaje_error:str, longitud:int, reintentos:int) -> str | None:
    '''
    mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
    mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
    longitud: cantidad de caracteres en una cadena (string).
    reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.
    '''
    iteraciones = 0

    cadena = input(mensaje)
    cadena = len(cadena)

    while cadena == None or cadena > longitud:
        iteraciones += 1

        print(mensaje_error)

        if iteraciones == reintentos:
            print('Se acabaron sus intentos.')
            return None
        
        cadena = input(mensaje)
    
pedir_cadena('Ingrese una cadena de caracteres: ', 'El número ingresado no es válido...', 5, 3)