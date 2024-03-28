import pygame

pygame.init()

screen = pygame.display.set_mode((600, 700))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.line(screen, [255, 255, 0], [150, 550], [450, 150])
    pygame.display.flip()