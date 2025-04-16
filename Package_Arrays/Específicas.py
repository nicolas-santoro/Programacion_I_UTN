def  determinar_positividad(number: int) -> bool:
    retorno = None

    if number > 0:
        retorno = True

    elif number < 0:
        retorno = False

    return retorno



def validar_paridad(numero: int) -> bool:
    par = False

    if numero % 2 == 0:
        par = True
    
    return par



def mayor_impar(lista: list) -> int:
    mayor = None

    for i in lista:
        if i % 2 != 0:
            if mayor == None or i > mayor:
                mayor = i
    
    return mayor



def listar_pares(lista: list) -> None:
    pares = [i for i in lista if validar_paridad(i)]

    print("Números pares:", pares)



def listar_indices_impares(lista: list) -> None:
    indices_impares = [lista[i] for i in range(1, len(lista), 2)]

    print("Números en índices impares:", indices_impares)