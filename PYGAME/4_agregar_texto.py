import pygame

pygame.init()

ventana = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Diario de Neuvillette')

ventana.fill((43, 110, 158))


icono = pygame.image.load('PYGAME\IMAGENES\Arma_Escrituras_del_Fluir_Sempiterno.webp')
pygame.display.set_icon(icono)


fuente = pygame.font.Font('PYGAME\FUENTES\The Bride in Hacienda.ttf', 60) #Pongo ¨.Font¨ en vez de ¨.SysFont¨ para poder poner MIS fuentes.
texto = fuente.render('Furina, quedate quieta por favor', False, (0, 0, 0), None)


bandera = True

while bandera == True:
    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            bandera = False

    
    ventana.blit(texto, (20, 10))
    

    pygame.display.update()

pygame.quit()