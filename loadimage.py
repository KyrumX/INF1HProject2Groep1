import pygame, sys

pygame.init()
heigth = 640
length = 480
size = (length, heigth)
DISPLAYSURF = pygame.display.set_mode(size, pygame.FULLSCREEN)


black = (0,0,0)
img = pygame.image.load('2sprites.png')
imgx = 10
imgy = 10


while True:
    DISPLAYSURF.fill(black)

    DISPLAYSURF.blit(img, (imgx, imgy))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.flip()


