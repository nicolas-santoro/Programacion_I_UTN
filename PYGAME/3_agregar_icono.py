import pygame

pygame.init()

ventana = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Mi Primer Ventana')

ventana.fill((43, 110, 158))


icono = pygame.image.load('PYGAME\IMAGENES\Arma_Escrituras_del_Fluir_Sempiterno.webp')
pygame.display.set_icon(icono)


bandera = True

while bandera == True:
    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            bandera = False
    

    pygame.display.update()

pygame.quit()