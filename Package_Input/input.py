from .validate import *

def get_int(mensaje: str, minimo: int, maximo: int, mensaje_error: str, reintentos: int) -> int | None:
    numero = int(input(mensaje))

    numero = validate_number(numero, mensaje_error, minimo, maximo, reintentos, 'int')

    return numero


def get_float(mensaje: str, minimo: float, maximo: float, mensaje_error: str, reintentos: int) -> float | None:
    numero = float(input(mensaje))

    numero = validate_number(numero, mensaje_error, minimo, maximo, reintentos, 'float')

    return numero


def get_str(mensaje: str, longitud: int, mensaje_error: str, reintentos: int) -> str | None:
    cadena = input(mensaje)
    cadena = len(cadena)

    cadena = validate_length(mensaje, cadena, mensaje_error, longitud, reintentos)

    return cadena