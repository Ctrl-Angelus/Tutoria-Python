
import pygame


pygame.init()
ventana = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True

y = 20
x = 100

x_final = 800
y_final = 800

imagen = pygame.transform.scale(pygame.image.load("objeto.png"), (256, 256))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x <= 0:
                    continue
                x -= 10
            if event.key == pygame.K_RIGHT:
                if x + 256 >= 400 and y < 420:
                    continue
                x += 10
            if event.key == pygame.K_DOWN:
                y += 10
            if event.key == pygame.K_UP:
                y -= 10


    ventana.fill("white")

    pygame.draw.rect(ventana, "red", (400, 20, 20, 400))

    ventana.blit(imagen, (x, y))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()