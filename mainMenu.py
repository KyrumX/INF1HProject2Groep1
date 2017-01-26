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
rules = False
terug = False

while True:
    mouse = pygame.mouse.get_pos()
    print(mouse)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 0 and mouse[0] < 400 and mouse[1] > 0 and mouse[1] < 150 and menu == True:
            clicked = True
            menu = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1516 and mouse[0] < 1920 and mouse[1] > 200 and mouse[1] < 350 and menu == True:
            rules = True
            menu = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 30 and mouse[0] < 300 and mouse[1] > 1000 and mouse[1] < 1080 and rules == True:
            terug = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1516 and mouse[0] < 1920 and mouse[1] > 0 and mouse[1] < 150 and menu == True:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 175 and mouse[0] < 540 and mouse[1] > 700 and mouse[1] < 830 and menu == False:
            program(2)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 770 and mouse[0] < 1130 and mouse[1] > 700 and mouse[1] < 830 and menu == False:
            program(3)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1360 and mouse[0] < 1770 and mouse[1] > 700 and mouse[1] < 830 and menu == False:
            program(4)



    k = pygame.key.get_pressed()
    if k[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    if menu == True:
        background = pygame.image.load('Afbeeldingen/euromastspelbgwmenu.png')
        background = pygame.transform.scale(background, (1920, 1080))
        screen.blit(background, (0, 0))

    elif rules == True:
        background = pygame.image.load('Afbeeldingen/spelregelsbg.png')
        background = pygame.transform.scale(background, (1920, 1080))
        screen.blit(background, (0, 0))
        if terug == True:
            terug = False
            rules = False
            menu = True



    else:
        background = pygame.image.load('Afbeeldingen/hvlspelers.png')
        background = pygame.transform.scale(background, (1920, 1080))
        screen.blit(background, (0, 0))








    pygame.display.update()
