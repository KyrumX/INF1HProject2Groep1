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

def text(msg, pos, size=30):
    white = (255, 255, 255)
    font = pygame.font.Font(None, size)
    label = font.render(msg, True, white)
    screen.blit(label, pos)


prachtig = (66, 170, 244)
screen.fill(prachtig)
menu = True
statusbar = pygame.image.load("Afbeeldingen/statusbar.png")
Play = False
Rules = False
BackRules = False
BackHighscore = False
BackSettings = False
Highscore = False
Settings = False
Hard = False
Easy = False
Normal = False
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
            Play = True
            menu = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1516 and mouse[0] < 1920 and mouse[1] > 200 and mouse[1] < 350 and menu == True:
            Rules = True
            menu = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 0 and mouse[0] < 400 and mouse[1] > 195 and mouse[1] < 340 and menu == True:
            Highscore = True
            menu = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 30 and mouse[0] < 300 and mouse[1] > 1000 and mouse[1] < 1080 and Rules == True:
            BackRules = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1670 and mouse[0] < 1910 and mouse[1] > 980 and mouse[1] < 1060 and Highscore == True:
            BackHighscore = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1570 and mouse[0] < 1890 and mouse[1] > 965 and mouse[1] < 1060 and Settings == True:
            BackSettings = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1516 and mouse[0] < 1920 and mouse[1] > 0 and mouse[1] < 150 and menu == True:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1516 and mouse[0] < 1920 and mouse[1] > 390 and mouse[1] < 530 and menu == True:
            Settings = True
            menu = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 150 and mouse[0] < 550 and mouse[1] > 677 and mouse[1] < 777 and Settings == True:
            Hard = True
            screen.blit(statusbar, (310, 0))
            text("De spelmodus staat nu op moeilijk!", (500, 12))
            pygame.display.update()
            pygame.time.delay(1500)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 150 and mouse[0] < 550 and mouse[1] > 386 and mouse[1] < 488 and Settings == True:
            Easy = True
            screen.blit(statusbar, (310, 0))
            text("De spelmodus staat nu op makkelijk!", (500, 12))
            pygame.display.update()
            pygame.time.delay(1500)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 150 and mouse[0] < 550 and mouse[1] > 530 and mouse[1] < 630 and Settings == True:
            screen.blit(statusbar, (310, 0))
            text("De spelmodus staat nu op normaal!", (500, 12))
            pygame.display.update()
            pygame.time.delay(1500)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 981 and mouse[0] < 1190 and mouse[1] > 380 and mouse[1] < 525 and Settings == True:
            MusicOn = True
            screen.blit(statusbar, (310, 0))
            text("Geluid staat nu aan!", (600, 12))
            pygame.display.update()
            pygame.time.delay(1500)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 983 and mouse[0] < 1190 and mouse[1] > 627 and mouse[1] < 769 and Settings == True:
            MusicOff = True
            screen.blit(statusbar, (310, 0))
            text("Geluid staat nu uit!", (600, 12))
            pygame.display.update()
            pygame.time.delay(1500)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 175 and mouse[0] < 540 and mouse[1] > 700 and mouse[1] < 830 and menu == False and Settings == False:
            program(2, timer)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 770 and mouse[0] < 1130 and mouse[1] > 700 and mouse[1] < 830 and menu == False and Settings == False:
            program(3, timer)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1360 and mouse[0] < 1770 and mouse[1] > 700 and mouse[1] < 830 and menu == False and Settings == False:
            program(4, timer)


    k = pygame.key.get_pressed()
    if k[K_ESCAPE]:
        pygame.quit()
        sys.exit()
    if menu == True:
        background = pygame.image.load('Afbeeldingen/euromastspelbgwtext.png')
        background = pygame.transform.scale(background, (1920, 1080))
        screen.blit(background, (0, 0))
    elif Rules == True:
        background = pygame.image.load('Afbeeldingen/spelregelsbg.png')
        background = pygame.transform.scale(background, (1920, 1080))
        screen.blit(background, (0, 0))
        if BackRules == True:
           BackRules = False
           Rules = False
           menu = True
    elif Highscore == True:
        background = pygame.image.load('Afbeeldingen/highscoresbg.png')
        background = pygame.transform.scale(background, (1920, 1080))
        screen.blit(background, (0, 0))
        highscoreRetrieve(screen)
        if BackHighscore == True:
           BackHighscore = False
           Highscore = False
           menu = True
    elif Settings == True:
        background = pygame.image.load('Afbeeldingen/instellingen.png')
        background = pygame.transform.scale(background, (1920, 1080))
        screen.blit(background, (0, 0))
        if Normal == True:
            timer = 50
            Normal = False
        elif Hard == True:
            timer = 30
            Hard = False
        elif Easy == True:
            timer = 80
            Easy = False
        elif BackSettings == True:
           BackSettings = False
           Settings = False
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
