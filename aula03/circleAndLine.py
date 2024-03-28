import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.circle(screen, [255, 255, 255], [320, 240], 30)
    pygame.draw.line(screen, [255, 0, 0], [0, 0], [640, 480])
    pygame.display.flip()