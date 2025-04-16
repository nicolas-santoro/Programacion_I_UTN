import pygame



pygame.init()


ancho = 500
alto = 500

dimensiones = (ancho, alto)


ventana = pygame.display.set_mode(dimensiones)
pygame.display.set_caption('Diario de Neuvillette')
ventana.fill((214, 249, 255))


# fondo = pygame.image.load('PYGAME\IMAGENES\Fondo_diario.jpg')
# fondo = pygame.transform.scale(fondo, dimensiones)
# ventana.blit(fondo, (0, 0))


icono = pygame.image.load('PYGAME\IMAGENES\Arma_Escrituras_del_Fluir_Sempiterno.webp')
pygame.display.set_icon(icono)


fuente = pygame.font.Font('PYGAME\FUENTES\The Bride in Hacienda.ttf', 50) #Pongo ¨.Font¨ en vez de ¨.SysFont¨ para poder poner MIS fuentes.


lista_nombres = ['Personas relevantes en Fontaine:', 
                '- Neuvillette', '- Furina','- Arlecchino', '- Clorinde', '- Wriothesley', '- Navia', '- Lyney',]


bandera = True

while bandera == True:
    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            bandera = False


    y = 20
    
    for nombre in lista_nombres:
        texto = fuente.render(nombre, False, (0, 0, 0))

        ventana.blit(texto, (30, y))

        y += 50


    pygame.display.update()


pygame.quit()