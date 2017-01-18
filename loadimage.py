import pygame

img = pygame.image.load('2sprites.png')

black = (0, 0, 0)
width = 640
heigth = 480
size = (width, heigth)
screen = pygame.display.set_mode(size)
screen.fill((black))
running = 1

while running:
    screen.fill((black))
    screen.blit(img,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.flip()

