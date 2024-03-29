import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.set_at([1279, 719], [255, 0, 0])

    pygame.display.flip()
