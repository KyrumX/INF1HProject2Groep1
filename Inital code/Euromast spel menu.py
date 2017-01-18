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
playgametext = myfont.render('Hier wordt het spel gespeeld!', True, white)

class Button: # Button class. Nog toe te voegen: klik functie
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

    def button(self): # de button functie zorgt ervoor dat de button getekend word met gecentreerde text
        design = pygame.draw.rect(screen, self.rectanglecolor, [self.x, self.y, self.w, self.h])
        myfont = pygame.font.SysFont(self.fonttype, self.fontsize)
        label = myfont.render(self.msg, True, self.textcolor)
        xcalc = ((design.right - design.left) / 2) + design.left
        ycalc = -0.5 * self.fontsize + 40
        if self.fontsize < 70:
            y_is = design.top + ycalc
        else:
            ycalc = -1 * self.fontsize + 70
            y_is = design.top + ycalc
        div = int(myfont.size(self.msg)[0] / 2)
        finalx = xcalc - div
        labelpos = (finalx, y_is)
        screen.blit(label, labelpos)


def box(color, x, y, w, h): # Een box sprite
    c = pygame.draw.rect(screen, color, [x, y, w, h])
    return c

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_ps()
    click = pygame.mouse.get_pressed()
    print(click)
prachtig = (66, 170, 244)
screen.fill(prachtig)
menu = True
while True:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 650 and mouse[0] < 1250 and mouse[1] > 650 and mouse[1] < 750:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 650 and mouse[0] < 1250 and mouse[1] > 450 and mouse[1] < 550:
            menu = False
    k = pygame.key.get_pressed()
    if k[K_ESCAPE]:
        pygame.quit()
        sys.exit()
    if menu == True:
        Button("Test Button Class", 70, 650, 780, black, white).button() # Om de button class te testen
        screen.blit(label3, (540,210))
        a = pygame.draw.rect(screen, (0, 255, 0), [650, 450, 600, 100])
        screen.blit(label, (830, 440))
        b = pygame.draw.rect(screen, red, [650, 650, 600, 100])
        screen.blit(label2, (760, 640))
    else:
        screen.fill(green)
        screen.blit(playgametext, (540, 210))

    pygame.display.update()
