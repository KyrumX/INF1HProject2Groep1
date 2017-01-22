import pygame
import sys
import time
from pygame.locals import *
from mainGame import *

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

black = (0, 0, 0)
green = (47, 214, 127)
red = (255, 0, 0)
white = (255, 255, 255)
darkgrey = (95, 77, 77)
darkblue = (70, 120, 201)

resolution = (1920, 1080)
screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
pygame.display.set_caption("Euromast Spel")

myfont = pygame.font.SysFont('Comic Sans MS', 70)
myfont2 = pygame.font.SysFont('Comic Sans MS', 100)
label = myfont.render('Spelen', True, black)
label2 = myfont.render('Spel sluiten', True, white)
label3 = myfont2.render('Het Euromast spel', True, white)
playgametext = myfont.render('Hier wordt het spel gespeeld!', True, white)

class Button:
    def __init__(self, msg, fontsize, x, y, rectanglecolor=green, textcolor=black, h=100, w=600): # Optionele waardes hier zijn rectanglecolor, textcolor en de dimensies van de rectangle
        self.msg = msg
        self.fonttype = "Comic Sans MS"
        self.textcolor = textcolor
        self.rectanglecolor = rectanglecolor
        self.fontsize = fontsize
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def button(self, scalehelper=40): # de button functie zorgt ervoor dat de button getekend word met gecentreerde text
        design = pygame.draw.rect(screen, self.rectanglecolor, [self.x, self.y, self.w, self.h])
        myfont = pygame.font.SysFont(self.fonttype, self.fontsize)
        label = myfont.render(self.msg, True, self.textcolor)
        xcalc = ((design.right - design.left) / 2) + design.left
        ycalc = -0.5 * self.fontsize + scalehelper
        if self.fontsize < 70:
            y_is = design.top + ycalc
        else:
            ycalc = -1 * self.fontsize + 70
            y_is = design.top + ycalc
        div = int(myfont.size(self.msg)[0] / 2)
        finalx = xcalc - div
        labelpos = (finalx, y_is)
        screen.blit(label, labelpos)
    def press(self):
        self.rectanglecolor = black

def drawtext(msg, fontsize, textcolor, x, y):
    myfont = pygame.font.SysFont("Comic Sans MS", fontsize)
    label = myfont.render(msg, True, textcolor)
    labelpos = (x, y)
    screen.blit(label, labelpos)

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_ps()
    click = pygame.mouse.get_pressed()
    print(click)
prachtig = (66, 170, 244)
screen.fill(prachtig)
menu = True
clicked = False
while True:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1244 and mouse[0] < 1712 and mouse[1] > 349 and mouse[1] < 470 and menu == True:
            clicked = True
            menu = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1245 and mouse[0] < 1711 and mouse[1] > 534 and mouse[1] < 657 and menu == True:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1384 and mouse[0] < 1461 and mouse[1] > 617 and mouse[1] < 686 and menu == False:
            program(2)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1534 and mouse[0] < 1609 and mouse[1] > 617 and mouse[1] < 686 and menu == False:
            program(3)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1684 and mouse[0] < 1761 and mouse[1] > 617 and mouse[1] < 688 and menu == False:
            program(4)

    k = pygame.key.get_pressed()
    if k[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    if menu == True:
        background = pygame.image.load('Afbeeldingen/euro.jpg')
        background = pygame.transform.scale(background, (1920, 1080))
        screen.blit(background, (0, 0))
        bg = pygame.image.load('Afbeeldingen/menubg.png')
        screen.blit(bg, (1230, 200))
        if clicked == False:
            spelen = pygame.image.load('Afbeeldingen/spelen.png')
            screen.blit(spelen, (1245, 350))
            afsluiten = pygame.image.load('Afbeeldingen/afsluiten.png')
            screen.blit(afsluiten, (1245, 534))
        else:
            afsluiten = pygame.image.load('Afbeeldingen/afsluiten.png')
            spelen = pygame.image.load('Afbeeldingen/spelenpressed.png')
            pygame.time.wait(10000)

    else:
        background = pygame.image.load('Afbeeldingen/playercount.png')
        background = pygame.transform.scale(background, (1920, 1080))
        screen.blit(background, (0, 0))
    pygame.display.update()
