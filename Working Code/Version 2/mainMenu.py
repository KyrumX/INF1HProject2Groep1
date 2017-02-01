import pygame
import sys
import time
from pygame.locals import *
from mainGame import *
from database import *

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
pygame.mixer.init()



black = (0, 0, 0)
green = (47, 214, 127)
red = (255, 0, 0)
white = (255, 255, 255)
darkgrey = (95, 77, 77)
darkblue = (70, 120, 201)

resolution = (1920, 1080)
screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
pygame.display.set_caption("Euromast Spel")


prachtig = (66, 170, 244)
screen.fill(prachtig)
menu = True
clicked = False
rules = False
terug = False
terug2 = False
terug3 = False
highscore = False
instellingen = False
moeilijk = False
makkelijk = False
normaal = False
MusicOff= False
MusicOn = False
timer = 50
MenuMusic = pygame.mixer.Sound("Geluiden/menu.wav")


while True:
    mouse = pygame.mouse.get_pos()
    # print(mouse)
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
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 0 and mouse[0] < 400 and mouse[1] > 195 and mouse[1] < 340 and menu == True:
            highscore = True
            menu = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 30 and mouse[0] < 300 and mouse[1] > 1000 and mouse[1] < 1080 and rules == True:
            terug = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1670 and mouse[0] < 1910 and mouse[1] > 980 and mouse[1] < 1060 and highscore == True:
            terug2 = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1140 and mouse[0] < 1390 and mouse[1] > 380 and mouse[1] < 550 and instellingen == True:
            terug3 = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1516 and mouse[0] < 1920 and mouse[1] > 0 and mouse[1] < 150 and menu == True:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 0 and mouse[0] < 400 and mouse[1] > 350 and mouse[1] < 450 and menu == True:
            instellingen = True
            menu = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1160 and mouse[0] < 1420 and mouse[1] > 140 and mouse[1] < 240 and instellingen == True:
            moeilijk = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 380 and mouse[0] < 650 and mouse[1] > 140 and mouse[1] < 240 and instellingen == True:
            makkelijk = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 740 and mouse[0] < 1000 and mouse[1] > 140 and mouse[1] < 240 and instellingen == True:
            normaal = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 875 and mouse[0] < 955 and mouse[1] > 445 and mouse[1] < 500 and instellingen == True:
            MusicOn = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 740 and mouse[0] < 820 and mouse[1] > 445 and mouse[1] < 500 and instellingen == True:
            MusicOff = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 175 and mouse[0] < 540 and mouse[1] > 700 and mouse[1] < 830 and menu == False:
            MenuMusic.stop()
            program(2, timer)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 770 and mouse[0] < 1130 and mouse[1] > 700 and mouse[1] < 830 and menu == False:
            MenuMusic.stop()
            program(3, timer)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1360 and mouse[0] < 1770 and mouse[1] > 700 and mouse[1] < 830 and menu == False:
            MenuMusic.stop()
            program(4, timer)


    k = pygame.key.get_pressed()
    if k[K_ESCAPE]:
        pygame.quit()
        sys.exit()
    if menu == True:
        background = pygame.image.load('Afbeeldingen/euromastspelbgwtext.png')
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
    elif highscore == True:
        background = pygame.image.load('Afbeeldingen/highscoresbg.png')
        background = pygame.transform.scale(background, (1920, 1080))
        screen.blit(background, (0, 0))
        highscoreRetrieve(screen)
        if terug2 == True:
           terug2 = False
           highscore = False
           menu = True
    elif instellingen == True:
        background = pygame.image.load('Afbeeldingen/instellingen.png')
        background = pygame.transform.scale(background, (1920, 1080))
        screen.blit(background, (0, 0))
        if normaal == True:
            timer = 50
            normaal = False
        elif moeilijk == True:
            timer = 30
            moeilijk = False
        elif makkelijk == True:
            makkelijk = 80
            makkelijk = False
        elif terug3 == True:
           terug3 = False
           instellingen = False
           menu = True
        elif MusicOn == True:
            MenuMusic.play()
            MusicOn = False
        elif MusicOff == True:
            MenuMusic.stop()
            MusicOff = False
    else:
        background = pygame.image.load('Afbeeldingen/hvlspelers2.png')
        background = pygame.transform.scale(background, (1920, 1080))
        screen.blit(background, (0, 0))




    pygame.display.update()
