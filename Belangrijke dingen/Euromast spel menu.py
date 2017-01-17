import pygame
import sys
from pygame.locals import *

pygame.init()
pygame.font.init()
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)

resolution = (1920, 1080)
screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
pygame.display.set_caption("Euromast Spel")

myfont = pygame.font.SysFont('Comic Sans MS', 70)
myfont2 = pygame.font.SysFont('Comic Sans MS', 100)
label = myfont.render('Spelen', True, black)
label2 = myfont.render('Spel sluiten', True, white)
label3 = myfont2.render('Het Euromast spel', True, white)

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_ps()
    click = pygame.mouse.get_pressed()
    print(click)
prachtig = (66, 170, 244)
screen.fill(prachtig)
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    k = pygame.key.get_pressed()
    if k[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    screen.blit(label3, (540,210))
    a = pygame.draw.rect(screen, (0, 255, 0), [650, 450, 600, 100])
    screen.blit(label, (830, 440))
    b = pygame.draw.rect(screen, red, [650, 650, 600, 100])
    screen.blit(label2, (760, 640))

    pygame.display.update()