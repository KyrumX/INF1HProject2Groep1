"""Copryright 2017, Project 2 Groep 1"""

import ctypes
import pygame
from pygame.locals import *
import time
import random
import psycopg2
from database import *

clock = pygame.time.Clock()
# Fix voor het voorkomen van stretchen wat je resolutie verpest
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()

def diceThrow():
    gooi = [1, 2, 3]
    throw = random.choice(gooi)
    return throw

class Player:
    def __init__(self, x, y, image, player):
        self.x = x
        self.y = y
        self.image = image

    def update(self, cg):
        while cg > 0:
            if self.y <= 386:

                self.x = 940
            self.y -= 69
            cg -= 1

    def draw(self, screen):
        img1 = pygame.image.load("Afbeeldingen/SP1.png")
        img2 = pygame.image.load("Afbeeldingen/SP2.png")
        img3 = pygame.image.load("Afbeeldingen/SP3.png")
        img4 = pygame.image.load("Afbeeldingen/SP4.png")

        win1 = pygame.image.load("Afbeeldingen/SP1winner.png")
        win2 = pygame.image.load("Afbeeldingen/SP2winner.png")
        win3 = pygame.image.load("Afbeeldingen/SP3winner.png")
        win4 = pygame.image.load("Afbeeldingen/SP4winner.png")

        if self.y < 50:
            if self.player == 1:
                self.image = win1
            elif self.player == 2:
                self.image = win2
            elif self.player == 3:
                self.image = win3
            else:
                self.image = win4
        screen.blit(self.image, (self.x, self.y))

def program(maxp):
    width = 1920
    height = 1080
    size = (width, height)
    background1 = pygame.image.load("Afbeeldingen/gameboard.png")
    background2 = pygame.image.load("Afbeeldingen/gameboard2.png")
    background3 = pygame.image.load("Afbeeldingen/gameboard3.png")
    main = pygame.image.load("Afbeeldingen/gameboardMain.png")
    img1 = pygame.image.load("Afbeeldingen/SP1.png")
    img2 = pygame.image.load("Afbeeldingen/SP2.png")
    img3 = pygame.image.load("Afbeeldingen/SP3.png")
    img4 = pygame.image.load("Afbeeldingen/SP4.png")


    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    font = pygame.font.Font(None, 30)

    if maxp >= 2:
        playerOne = Player(819, 1007, img1, 1)
        playerTwo = Player(900, 1007, img2, 2)
    if maxp >= 3:
        playerThree = Player(981, 1007, img3, 3)
    if maxp == 4:
        playerFour = Player(1062, 1007, img4, 4)

    screen.blit(main, (0, 0))
    cp = 1



    mainloop = True
    while mainloop:
        keuze = 16
        black = (0, 0, 0)
        labelvraag = font.render("Vraag:", True, black)
        screen.blit(labelvraag, (7, 7))
        vraag = str(interact_with_database("SELECT Question FROM QnA WHERE Question_ID = {}".format(keuze)))
        labelshowvraag = font.render(vraag, True, black)
        screen.blit(labelshowvraag, (7, 30))
        mouse = pygame.mouse.get_pos()

        #Mainloop code for input
        k = pygame.key.get_pressed()
        if k[K_ESCAPE]:
            mainloop = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop = False
            #elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 64 and mouse[0] < 188 and mouse[1] > 841 and mouse[1] < 958:
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1539 and mouse[0] < 1776 and mouse[1] > 434 and mouse[1] < 662:
                cg = diceThrow()
                if cg == 1:
                    screen.blit(background1, (0, 0))
                elif cg == 2:
                    screen.blit(background2, (0, 0))
                else:
                    screen.blit(background3, (0, 0))
                if cp == 1:
                    playerOne.update(cg)
                    # if playerOne.y == 5:
                    #     mainloop = False
                    cp += 1
                elif cp == 2:
                    playerTwo.update(cg)
                    if maxp > 2:
                        cp += 1
                    else:
                        cp -= 1
                elif cp == 3:
                    playerThree.update(cg)
                    if maxp > 3:
                        cp += 1
                    else:
                        cp -= 2
                elif cp == 4:
                    playerFour.update(cg)
                    cp -= 3
        print(cp)
        if maxp <= 2:
            playerOne.draw(screen)
            playerTwo.draw(screen)
        elif maxp == 3:
            playerOne.draw(screen)
            playerTwo.draw(screen)
            playerThree.draw(screen)
        else:
            playerOne.draw(screen)
            playerTwo.draw(screen)
            playerThree.draw(screen)
            playerFour.draw(screen)
        clock.tick(60)
        pygame.display.update()

