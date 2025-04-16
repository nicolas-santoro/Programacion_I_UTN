import pygame

pygame.init()

pygame.display.set_mode((500, 500))
pygame.display.set_caption('Mi Primer Ventana')


bandera = True

while bandera == True:
    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            bandera = False

pygame.quit()