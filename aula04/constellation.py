import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen, [255, 255, 255], [20, 370, 20, 20])
    pygame.draw.rect(screen, [255, 255, 255], [37, 360, 20, 20])
    pygame.draw.rect(screen, [255, 255, 255], [60, 300, 20, 20])
    pygame.draw.rect(screen, [255, 255, 255], [300, 217, 20, 20])
    pygame.draw.rect(screen, [255, 255, 255], [200, 200, 10, 10])
    pygame.draw.rect(screen, [255, 255, 255], [170, 68, 15, 15])
    pygame.draw.rect(screen, [255, 255, 255], [377, 90, 20, 20])
    pygame.draw.rect(screen, [255, 255, 255], [50, 65, 20, 20])
    pygame.draw.rect(screen, [255, 255, 255], [344, 269, 17, 17])
    pygame.draw.rect(screen, [255, 255, 255], [317, 366, 12, 12])
    pygame.draw.rect(screen, [255, 255, 255], [140, 150, 12, 12])
    pygame.display.flip()