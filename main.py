# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    pygame.draw.rect(screen, "red", (
        800 / 2 - 400 / 2,
        800 / 2 - 400 / 2,
        400,
        400
    ), 10, 50)

    texto = pygame.font.SysFont("Fira Code", 36)
    texto_renderizado = texto.render("Hola Mundo", True, "White")

    screen.blit(texto_renderizado, (
            800 / 2 - texto_renderizado.get_width() / 2,
            800 / 2 - texto_renderizado.get_height() / 2
    ))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()