import pygame

pygame.init()

screen = pygame.display.set_mode([500, 550])

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.polygon(screen, (255, 255, 0), ((70,400), (250,100), (430,400)))
    pygame.display.flip()