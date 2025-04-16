import pygame
import random

pygame.init()

# Ejemplo de una lista que se actualiza (puedes adaptarlo según tus necesidades)
opciones = ["Opción 1", "Opción 2", "Opción 3", "Opción 4"]

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

opcion_aleatoria = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Ejemplo de actualización de la lista mediante un evento de tecla
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Actualiza la lista (aquí puedes modificar cómo se actualiza)
                opciones.append("Opción Nueva")

                # Elegir una opción aleatoria de la lista actualizada
                opcion_aleatoria = random.choice(opciones)
                print("Opción elegida:", opcion_aleatoria)  # Esto es solo para verificar en consola, puedes eliminarlo o adaptarlo

    # Limpiar la pantalla con un color blanco o cualquier otro color de fondo
    screen.fill((255, 255, 255))  # Puedes cambiar (255, 255, 255) por el color de fondo que desees

    # Ejemplo de mostrar la opción aleatoria en pantalla (puedes adaptarlo según tu aplicación)
    if opciones:
        font = pygame.font.Font(None, 36)
        text = font.render(opcion_aleatoria, True, (0, 0, 0))
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)

    # Actualizar la pantalla
    pygame.display.flip()

pygame.quit()