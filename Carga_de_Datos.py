'''
La división de higiene está trabajando en un control de stock para productos sanitarios. 
Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos:
El tipo (validar "barbijo", "jabón" o "alcohol")
El precio: (validar entre 100 y 300)
La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
La marca y el Fabricante.
  
Se debe informar lo siguiente:
Del más caro de los barbijos, la cantidad de unidades y el fabricante.
Del ingreso con más unidades, el fabricante.
Cuántas unidades de jabones hay en total.
'''

precio_max = 0

contador_b = 0
acumulador_j = 0
contador_a = 0

cantidad_b_max = 0
cantidad_max = 0



for i in range(5):
    tipo = input('Coloque el producto de prevención: ')
    
    while tipo != 'barbijo' or tipo != 'jabon' or tipo != 'alcohol':
        tipo = input('Coloque el producto de prevención: ')


    precio = input('Coloque el precio del producto: ')
    precio = float(precio)

    while 100 <= precio <= 300:
        break

    
    cantidad = input('Coloque la cantidad de productos: ')
    cantidad = int(cantidad)

    while cantidad > 0:
        break


    marca = input('Coloque la marca/fabricante del producto: ')

match tipo:
    case 'barbijo':
        contador_b += 1

        if  contador_b == 1 or precio > precio_max:
            precio_max = precio
            marca_b_max = marca
            cantidad_b_max = cantidad
    
    case 'jabon':
        acumulador_j += cantidad

    case 'alcohol':
        contador_a += contador_a

if i == 0 or cantidad > cantidad_max:
    cantidad_max = cantidad
    marca_max = marca

print(f'El más caro de los barbijos tiene una cantidad de: {cantidad_b_max}, y es fabricado por {marca_b_max} al precio de ${precio_max}.')
print(f'La marca que más cantidad vendió fue {marca_max} y vendió {cantidad_max} unidades.')
print(f'Se vendieron un total de {acumulador_j} jabones.')