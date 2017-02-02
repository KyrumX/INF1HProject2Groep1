"""Copryright 2017, Project 2 Groep 1"""

import ctypes
import pygame
from pygame.locals import *
import time
import random
import psycopg2
from database import *
import sys
from multipleLines import *
from textInput import *
import ctypes
import pygame
from pygame.locals import *
import time
import random
import psycopg2
from database import *
import sys
from multipleLines import *
from textInput import *

clock = pygame.time.Clock()
# Fix voor het voorkomen van stretchen wat je resolutie verpest
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()


def diceThrow():
    gooi = [1, 2, 3, 4, 5, 6]
    throw = random.choice(gooi)
    return throw

def getQuestion(questionCat, cg):
    if cg == 2 or cg == 4 or cg == 6:
        questionList = get_questions(questionCat)
        questionPicked = random.choice(questionList)
        questionID = questionPicked[0]
        return questionID
    else:
        questionList = get_questions2(questionCat)
        questionPicked = random.choice(questionList)
        questionID = questionPicked[0]
        return questionID


class Player:
    def __init__(self, x, y, image, name):
        self.x = x
        self.y = y
        self.name = name
        self.image = image
        self.score = 0

    def updatef(self, cg):
        while cg > 0 and self.y > 0:
            if self.y == 477:
                if self.x == 805 or self.x == 865:
                    self.x = 926
                    self.y = 333
                elif self.x == 925 or self.x == 985:
                    self.x = 986
                    self.y = 333
                elif self.x == 1045 or self.x == 1105:
                    self.x = 1046
                    self.y = 333
                elif self.x == 1165 or self.x == 1225:
                    self.x = 1106
                    self.y = 333
            else:
                self.y -= 57
            cg -= 1

    def updatel(self, cg):
        while cg > 0:
            self.x -= 60
            if self.x == 745 and self.y > 333:
                self.x = 1225
            elif self.x == 866 and self.y <= 333:
                self.x = 1106
            cg -= 1

    def updater(self, cg):
        while cg > 0:
            self.x += 60
            if self.x == 1285 and self.y > 333:
                self.x = 805
            elif self.x == 1166 and self.y <= 333:
                self.x = 926
            cg -= 1

    def updateb(self, cg):
        while cg > 0:
            if self.y == 990:
                break
            self.y += 57
            if self.y > 333:
                if self.x == 926:
                    self.x = 805
                    self.y = 477
                elif self.x == 987:
                    self.x = 925
                    self.y = 477
                elif self.x == 1046:
                    self.x = 1045
                    self.y = 477
                elif self.x == 1106:
                    self.x = 1165
                    self.y = 477
            cg -= 1

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def addScore(self):
        self.score += 10


    def winnerScore(self):
        self.score += 100

def program(maxp, timer):
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    white = (255, 255, 255)
    width = 1920
    height = 1080
    size = (width, height)
    QuestionRight = pygame.mixer.Sound("Geluiden/Ding.wav")
    QuestionWrong = pygame.mixer.Sound("Geluiden/buzzer.wav")
    background1 = pygame.image.load("Afbeeldingen/gamebackgroundred.png")
    background2 = pygame.image.load("Afbeeldingen/gamebackgroundyellow.png")
    background3 = pygame.image.load("Afbeeldingen/gamebackgroundgreen.png")
    background4 = pygame.image.load("Afbeeldingen/gamebackgroundblue.png")
    nameInputBack = pygame.image.load("Afbeeldingen/avatarks.png")
    img1 = pygame.image.load("Afbeeldingen/SP1.png")
    img2 = pygame.image.load("Afbeeldingen/SP2.png")
    img3 = pygame.image.load("Afbeeldingen/SP3.png")
    img4 = pygame.image.load("Afbeeldingen/SP4.png")
    brownbar = pygame.image.load("Afbeeldingen/brownbar.png")
    buttoncover = pygame.image.load("Afbeeldingen/buttoncover.png")
    d1 = pygame.image.load("Afbeeldingen/DS1.png")
    d2 = pygame.image.load("Afbeeldingen/DS2.png")
    d3 = pygame.image.load("Afbeeldingen/DS3.png")
    d4 = pygame.image.load("Afbeeldingen/DS4.png")
    d5 = pygame.image.load("Afbeeldingen/DS5.png")
    d6 = pygame.image.load("Afbeeldingen/DS6.png")
    dn = pygame.image.load("Afbeeldingen/DS0.png")
    dz1 = pygame.image.load("Afbeeldingen/diceOne.png")
    dz2 = pygame.image.load("Afbeeldingen/diceTwo.png")
    dz3 = pygame.image.load("Afbeeldingen/diceThree.png")
    dz4 = pygame.image.load("Afbeeldingen/diceFour.png")
    dz5 = pygame.image.load("Afbeeldingen/diceFive.png")
    dz6 = pygame.image.load("Afbeeldingen/diceSix.png")
    dz0 = pygame.image.load("Afbeeldingen/diceZero.png")
    terminationscreen = pygame.image.load("Afbeeldingen/gameover.png")
    orderPlayers2 = pygame.image.load("Afbeeldingen/2persoonstart.png")
    orderPlayers3 = pygame.image.load("Afbeeldingen/3persoonstart.png")
    orderPlayers4 = pygame.image.load("Afbeeldingen/4persoonstart.png")
    dobbelBeurt = pygame.image.load("Afbeeldingen/gooidobbelsteen.png")
    keuzeimg = pygame.image.load("Afbeeldingen/kiezen.png")
    gekozen = pygame.image.load("Afbeeldingen/gekozen.png")
    gekozen2 = pygame.image.load("Afbeeldingen/gekozen2.png")
    gekozen3 = pygame.image.load("Afbeeldingen/gekozen3.png")
    gekozen4 = pygame.image.load("Afbeeldingen/gekozen4.png")
    kiecat = pygame.image.load("Afbeeldingen/kiescategorie.png")

    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    font = pygame.font.Font(None, 30)
    font2 = pygame.font.Font(None, 50)

    def text(msg, pos, size=30):
        white = (255, 255, 255)
        font = pygame.font.Font(None, size)
        label = font.render(msg, True, white)
        screen.blit(label, pos)

    screen.blit(nameInputBack, (0, 0))

    player1name = (ask(screen, "Naam speler 1"))
    screen.blit(nameInputBack, (0, 0))
    pygame.display.update()

    while len(player1name) < 1:
        player1name = (ask(screen, "Naam te kort. Naam speler 1"))
        screen.blit(nameInputBack, (0, 0))
        pygame.display.update()
    screen.blit(nameInputBack, (0, 0))
    pygame.display.update()

    player2name = (ask(screen, "Naam speler 2"))
    screen.blit(nameInputBack, (0, 0))
    while player2name == player1name:
        player2name = (ask(screen, "Een medespeler heeft deze naam al gekozen. Naam speler 2"))
    screen.blit(nameInputBack, (0, 0))
    pygame.display.update()

    if maxp == 3:
        player3name = (ask(screen, "Naam speler 3"))
        screen.blit(nameInputBack, (0, 0))
        pygame.display.update()
        while player3name == player1name or player3name == player2name:
            player3name = (ask(screen, "Een medespeler heeft deze naam al gekozen. Naam speler 3"))
        screen.blit(nameInputBack, (0, 0))
        pygame.display.update()
    elif maxp == 4:
        player3name = (ask(screen, "Naam speler 3"))
        screen.blit(nameInputBack, (0, 0))
        pygame.display.update()

        while player3name == player1name or player3name == player2name:
            player3name = (ask(screen, "Een medespeler heeft deze naam al gekozen. Naam speler 3"))
        screen.blit(nameInputBack, (0, 0))
        pygame.display.update()

        player4name = (ask(screen, "Naam speler 4"))
        screen.blit(nameInputBack, (0, 0))
        pygame.display.update()
        while player4name == player1name or player4name == player2name or player4name == player3name:
            player3name = (ask(screen, "Een medespeler heeft deze naam al gekozen. Naam speler 4"))
        screen.blit(nameInputBack, (0, 0))
        pygame.display.update()

    p1choosing = True
    p2choosing = False
    p3choosing = False
    p4choosing = False
    choosing = True
    beginning = True
    xk = 0
    xg = 0
    screen.blit(keuzeimg, (100, 420))
    screen.blit(keuzeimg, (437, 420))
    screen.blit(keuzeimg, (800, 420))
    screen.blit(keuzeimg, (1170, 420))
    pygame.display.update()
    while choosing:
        mouse = pygame.mouse.get_pos()
        print(mouse)
        if p1choosing == True:
            pygame.display.update()
            text("{}, kies je avatar".format(player1name), (200, 320))
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 114 and mouse[0] < 281 and mouse[1] > 429 and mouse[1] < 486:
                    playerOneAfb = img1
                    char1chosen = True
                    char2chosen = False
                    char3chosen = False
                    char4chosen = False
                    p1choosing = False
                    p2choosing = True
                elif event.type == MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 445 and mouse[0] < 623 and mouse[1] > 422 and mouse[1] < 474:
                    playerOneAfb = img2
                    char1chosen = False
                    char2chosen = True
                    char3chosen = False
                    char4chosen = False
                    p1choosing = False
                    p2choosing = True
                elif event.type == MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 813 and mouse[0] < 986 and mouse[1] > 422 and mouse[1] < 474:
                    playerOneAfb = img3
                    char1chosen = False
                    char2chosen = False
                    char3chosen = True
                    char4chosen = False
                    p1choosing = False
                    p2choosing = True
                elif event.type == MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1183 and mouse[0] < 1356 and mouse[1] > 422 and mouse[1] < 474:
                    playerOneAfb = img4
                    char1chosen = False
                    char2chosen = False
                    char3chosen = False
                    char4chosen = True
                    p1choosing = False
                    p2choosing = True


        elif p2choosing == True:
            if xk == 0:
                screen.blit(nameInputBack, (0, 0))
                pygame.display.update()
                text("{}, kies je avatar".format(player2name), (200, 320))
                if char1chosen:
                    screen.blit(gekozen2, (100, 420))
                    screen.blit(keuzeimg, (437, 420))
                    screen.blit(keuzeimg, (800, 420))
                    screen.blit(keuzeimg, (1170, 420))
                    pygame.display.update()
                elif char2chosen:
                    screen.blit(keuzeimg, (100, 420))
                    screen.blit(gekozen3, (437, 420))
                    screen.blit(keuzeimg, (800, 420))
                    screen.blit(keuzeimg, (1170, 420))
                    pygame.display.update()
                elif char3chosen:
                    screen.blit(keuzeimg, (100, 420))
                    screen.blit(keuzeimg, (437, 420))
                    screen.blit(gekozen, (800, 420))
                    screen.blit(keuzeimg, (1170, 420))
                    pygame.display.update()
                elif char4chosen:
                    screen.blit(keuzeimg, (100, 420))
                    screen.blit(keuzeimg, (437, 420))
                    screen.blit(keuzeimg, (800, 420))
                    screen.blit(gekozen4, (1170, 420))
                    pygame.display.update()
                xk += 1

            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 114 and mouse[0] < 276 and mouse[1] > 429 and mouse[1] < 486 and char1chosen == False:
                    playerTwoAfb = img1
                    char1chosen = True
                    if maxp > 2:
                        p3choosing = True
                        p2choosing = False
                    else:
                        screen.blit(gekozen2, (100, 420))
                        pygame.display.update()
                        pygame.time.delay(1000)
                        choosing = False
                elif event.type == MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 445 and mouse[0] < 623 and mouse[1] > 422 and mouse[1] < 474 and char2chosen == False:
                    playerTwoAfb = img2
                    char2chosen = True
                    if maxp > 2:
                        p3choosing = True
                        p2choosing = False
                    else:
                        screen.blit(gekozen3, (437, 420))
                        pygame.display.update()
                        pygame.time.delay(1000)
                        choosing = False
                elif event.type == MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 813 and mouse[0] < 986 and mouse[1] > 422 and mouse[1] < 474 and char3chosen == False:
                    playerTwoAfb = img3
                    char3chosen = True
                    if maxp > 2:
                        p3choosing = True
                        p2choosing = False
                    else:
                        screen.blit(gekozen, (800, 420))
                        pygame.display.update()
                        pygame.time.delay(1000)
                        choosing = False
                elif event.type == MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1183 and mouse[0] < 1356 and mouse[1] > 422 and mouse[1] < 474 and char4chosen == False:
                    playerTwoAfb = img4
                    char4chosen = True
                    if maxp > 2:
                        p3choosing = True
                        p2choosing = False
                    else:
                        screen.blit(gekozen4, (1170, 420))
                        pygame.display.update()
                        pygame.time.delay(1000)
                        choosing = False
        elif p3choosing == True:
            if xg == 0:
                screen.blit(nameInputBack, (0, 0))
                pygame.display.update()
                text("{}, kies je avatar".format(player3name), (200, 320))
                if char1chosen == True and char2chosen == True:
                    screen.blit(gekozen2, (100, 420))
                    screen.blit(gekozen3, (437, 420))
                    screen.blit(keuzeimg, (800, 420))
                    screen.blit(keuzeimg, (1170, 420))
                    pygame.display.update()
                elif char1chosen and char3chosen:
                    screen.blit(gekozen2, (100, 420))
                    screen.blit(keuzeimg, (437, 420))
                    screen.blit(gekozen, (800, 420))
                    screen.blit(keuzeimg, (1170, 420))
                    pygame.display.update()
                elif char1chosen and char4chosen:
                    screen.blit(gekozen2, (100, 420))
                    screen.blit(keuzeimg, (437, 420))
                    screen.blit(keuzeimg, (800, 420))
                    screen.blit(gekozen4, (1170, 420))
                    pygame.display.update()
                elif char2chosen and char3chosen:
                    screen.blit(keuzeimg, (100, 420))
                    screen.blit(gekozen3, (437, 420))
                    screen.blit(gekozen, (800, 420))
                    screen.blit(keuzeimg, (1170, 420))
                    pygame.display.update()
                elif char2chosen and char4chosen:
                    screen.blit(keuzeimg, (100, 420))
                    screen.blit(gekozen3, (437, 420))
                    screen.blit(keuzeimg, (800, 420))
                    screen.blit(gekozen4, (1170, 420))
                    pygame.display.update()
                elif char3chosen and char4chosen:
                    screen.blit(keuzeimg, (100, 420))
                    screen.blit(keuzeimg, (437, 420))
                    screen.blit(gekozen, (800, 420))
                    screen.blit(gekozen4, (1170, 420))
                    pygame.display.update()
                xg += 1
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 114 and mouse[0] < 276 and mouse[1] > 429 and mouse[1] < 486 and char1chosen == False:
                    playerThreeAfb = img1
                    char1chosen = True
                    if maxp > 3:
                        p4choosing = True
                        p3choosing = False
                    else:
                        screen.blit(gekozen2, (100, 420))
                        pygame.display.update()
                        pygame.time.delay(1000)
                        pygame.display.update()
                        choosing = False
                elif event.type == MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 445 and mouse[0] < 623 and mouse[1] > 422 and mouse[1] < 474 and char2chosen == False:
                    playerThreeAfb = img2
                    char2chosen = True
                    if maxp > 3:
                        p4choosing = True
                        p3choosing = False
                    else:
                        screen.blit(gekozen3, (437, 420))
                        pygame.display.update()
                        pygame.time.delay(1000)
                        pygame.display.update()
                        choosing = False
                elif event.type == MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 813 and mouse[0] < 986 and mouse[1] > 422 and mouse[1] < 474 and char3chosen == False:
                    playerThreeAfb = img3
                    char3chosen = True
                    if maxp > 3:
                        p4choosing = True
                        p3choosing = False
                    else:
                        screen.blit(gekozen, (800, 420))
                        pygame.display.update()
                        pygame.time.delay(1000)
                        pygame.display.update()
                        choosing = False
                elif event.type == MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1183 and mouse[0] < 1356 and mouse[1] > 422 and mouse[1] < 474 and char4chosen == False:
                    playerThreeAfb = img4
                    char4chosen = True
                    if maxp > 3:
                        p4choosing = True
                        p3choosing = False
                    else:
                        screen.blit(gekozen4, (1170, 420))
                        pygame.display.update()
                        pygame.time.delay(1000)
                        pygame.display.update()
                        screen.blit(gekozen, (1170, 420))
                        choosing = False

        elif p4choosing == True:
            print("checkpoint 4")
            screen.blit(nameInputBack, (0, 0))
            if char1chosen and char2chosen and char3chosen:
                text("{}, jij krijgt avatar 4".format(player4name), (200, 320))
                screen.blit(gekozen2, (100, 420))
                screen.blit(gekozen3, (437, 420))
                screen.blit(gekozen, (800, 420))
                screen.blit(gekozen, (1170, 420))
                playerFourAfb = img4
                pygame.display.update()
                pygame.time.delay(3000)
                pygame.display.update()
            elif char2chosen and char3chosen and char4chosen:
                text("{}, jij krijgt avatar 1".format(player4name), (200, 320))
                screen.blit(gekozen2, (100, 420))
                screen.blit(gekozen3, (437, 420))
                screen.blit(gekozen, (800, 420))
                screen.blit(gekozen4, (1170, 420))
                playerFourAfb = img1
                pygame.display.update()
                pygame.time.delay(3000)
                pygame.display.update()
            elif char1chosen and char3chosen and char4chosen:
                text("{}, jij krijgt avatar 2".format(player4name), (200, 320))
                screen.blit(gekozen2, (100, 420))
                screen.blit(gekozen3, (437, 420))
                screen.blit(gekozen, (800, 420))
                screen.blit(gekozen4, (1170, 420))
                playerFourAfb = img2
                pygame.display.update()
                pygame.time.delay(3000)
                pygame.display.update()
            elif char1chosen and char2chosen and char4chosen:
                text("{}, jij krijgt avatar 3".format(player4name), (200, 320))
                screen.blit(gekozen2, (100, 420))
                screen.blit(gekozen3, (437, 420))
                screen.blit(gekozen, (800, 420))
                screen.blit(gekozen4, (1170, 420))
                playerFourAfb = img3
                pygame.display.update()
                pygame.time.delay(3000)
                pygame.display.update()

                # screen.blit(keuzeimg, (100, 420))
                # screen.blit(keuzeimg, (450, 420))
                # screen.blit(keuzeimg, (810, 420))
                # screen.blit(keuzeimg, (1180, 420))


            choosing = False


    #BEPALEN WELKE SPELER MAG BEGINNEN
    dtp = 1
    pl4throw = 0
    pl3throw = 0
    pl2throw = 0
    pl1throw = 0
    screen.blit(dobbelBeurt, (0,0))
    if maxp == 2:
        screen.blit(dz0, (35,507))
        screen.blit(dz0, (500,507))
    if maxp == 3:
        screen.blit(dz0, (35,507))
        screen.blit(dz0, (500,507))
        screen.blit(dz0, (965,507))
    if maxp == 4:
        screen.blit(dz0, (35,507))
        screen.blit(dz0, (500,507))
        screen.blit(dz0, (965,507))
        screen.blit(dz0, (1430,507))
    for i in range(1, maxp+1):
        if i is 1:
            gooiBericht = font2.render(player1name + " mag nu gooien.", True, white)
            screen.blit(gooiBericht, (35, 470))
        elif i is 2:
            gooiBericht = font2.render(player2name + " mag nu gooien.", True, white)
            screen.blit(gooiBericht, (500, 470))
        elif i is 3:
            gooiBericht = font2.render(player3name + " mag nu gooien.", True, white)
            screen.blit(gooiBericht, (965, 470))
        elif i is 4:
            gooiBericht = font2.render(player4name + " mag nu gooien.", True, white)
            screen.blit(gooiBericht, (1430, 470))
        pygame.display.update()
        getorder = True
        if dtp == 1:
            while getorder == True:
                k = pygame.key.get_pressed()
                for event in pygame.event.get():
                    mouse = pygame.mouse.get_pos()
                    print(mouse)
                    if k[pygame.K_ESCAPE]:
                        sys.exit("Escape was pressed")
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 35 and mouse[0] < 451 and mouse[1] > 507 and mouse[1] < 923:
                        keren = [5, 6, 7, 8, 9, 10]
                        dobbelsteenZijde = [dz1, dz2, dz3, dz4, dz5, dz6]
                        aantalKeer = random.choice(keren)
                        for i in range(0, aantalKeer):
                            zijde = random.choice(dobbelsteenZijde)
                            screen.blit(zijde, (35, 507))
                            pygame.display.update()
                            time.sleep(0.5)
                        pl1throw = diceThrow()
                        print(pl1throw)
                        if pl1throw == 2:
                            screen.blit(dz2, (35, 507))
                        elif pl1throw == 4:
                            screen.blit(dz4, (35, 507))
                        elif pl1throw == 6:
                            screen.blit(dz6, (35, 507))
                        elif pl1throw == 1:
                            screen.blit(dz1, (35, 507))
                        elif pl1throw == 3:
                            screen.blit(dz3, (35, 507))
                        elif pl1throw == 5:
                            screen.blit(dz5, (35, 507))
                        getorder = False
        elif dtp == 2:
            while getorder == True:
                k = pygame.key.get_pressed()
                for event in pygame.event.get():
                    mouse = pygame.mouse.get_pos()
                    if k[pygame.K_ESCAPE]:
                        sys.exit("Escape was pressed")
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 500 and mouse[0] < 916 and mouse[1] > 507 and mouse[1] < 923:
                        keren = [5, 6, 7]
                        dobbelsteenZijde = [dz1, dz2, dz3, dz4, dz5, dz6]
                        aantalKeer = random.choice(keren)
                        for i in range(0, aantalKeer):
                            zijde = random.choice(dobbelsteenZijde)
                            screen.blit(zijde, (500, 507))
                            pygame.display.update()
                            time.sleep(0.5)
                        pl2throw = diceThrow()
                        print(pl2throw)
                        if pl2throw == 2:
                            screen.blit(dz2, (500, 507))
                        elif pl2throw == 4:
                            screen.blit(dz4, (500, 507))
                        elif pl2throw == 6:
                            screen.blit(dz6, (500, 507))
                        elif pl2throw == 1:
                            screen.blit(dz1, (500, 507))
                        elif pl2throw == 3:
                            screen.blit(dz3, (500, 507))
                        elif pl2throw == 5:
                            screen.blit(dz5, (500, 507))
                        getorder = False
        if dtp == 3:
            while getorder == True:
                k = pygame.key.get_pressed()
                for event in pygame.event.get():
                    mouse = pygame.mouse.get_pos()
                    if k[pygame.K_ESCAPE]:
                        sys.exit("Escape was pressed")
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 965 and mouse[0] < 1381 and mouse[1] > 507 and mouse[1] < 923:
                        keren = [5, 6, 7]
                        dobbelsteenZijde = [dz1, dz2, dz3, dz4, dz5, dz6]
                        aantalKeer = random.choice(keren)
                        for i in range(0, aantalKeer):
                            zijde = random.choice(dobbelsteenZijde)
                            screen.blit(zijde, (965, 507))
                            pygame.display.update()
                            time.sleep(0.5)
                        pl3throw = diceThrow()
                        print(pl3throw)
                        if pl3throw == 2:
                            screen.blit(dz2, (965, 507))
                        elif pl3throw == 4:
                            screen.blit(dz4, (965, 507))
                        elif pl3throw == 6:
                            screen.blit(dz6, (965, 507))
                        elif pl3throw == 1:
                            screen.blit(dz1, (965, 507))
                        elif pl3throw == 3:
                            screen.blit(dz3, (965, 507))
                        elif pl3throw == 5:
                            screen.blit(dz5, (965, 507))
                        getorder = False
        if dtp == 4:
            while getorder == True:
                k = pygame.key.get_pressed()
                for event in pygame.event.get():
                    mouse = pygame.mouse.get_pos()
                    if k[pygame.K_ESCAPE]:
                        sys.exit("Escape was pressed")
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1430 and mouse[0] < 1846 and mouse[1] > 507 and mouse[1] < 923:
                        keren = [5, 6, 7]
                        dobbelsteenZijde = [dz1, dz2, dz3, dz4, dz5, dz6]
                        aantalKeer = random.choice(keren)
                        for i in range(0, aantalKeer):
                            zijde = random.choice(dobbelsteenZijde)
                            screen.blit(zijde, (1430, 507))
                            pygame.display.update()
                            time.sleep(0.5)
                        pl4throw = diceThrow()
                        print(pl4throw)
                        if pl4throw == 2:
                            screen.blit(dz2, (1430, 507))
                        elif pl4throw == 4:
                            screen.blit(dz4, (1430, 507))
                        elif pl4throw == 6:
                            screen.blit(dz6, (1430, 507))
                        elif pl4throw == 1:
                            screen.blit(dz1, (1430, 507))
                        elif pl4throw == 3:
                            screen.blit(dz3, (1430, 507))
                        elif pl4throw == 5:
                            screen.blit(dz5, (1430, 507))
                        getorder = False
        dtp +=1
    maxThrow = max(pl1throw, pl2throw, pl3throw, pl4throw)
    if pl1throw == maxThrow:
        cp = 1
    elif pl2throw == maxThrow:
        cp = 2
    elif pl3throw == maxThrow:
        cp = 3
    elif pl4throw == maxThrow:
        cp = 4
    #EINDE VAN BEPALEN 1E SPELER

    #LAAT SPELERS CATEGORIE KIEZEN:
    if maxp == 2:
        aantKeuze = 2
    elif maxp == 3:
        aantKeuze = 3
    elif maxp == 4:
        aantKeuze = 4

    sp = cp

    screen.blit(kiecat, (0,0))
    pygame.display.update()
    entAllowed = True
    sportAllowed = True
    hisAllowed = True
    geoAllowed = True
    assignCat = True
    cnt = 0


    while assignCat == True:
        while not cnt == maxp:
            k = pygame.key.get_pressed()
            for event in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                if k[pygame.K_ESCAPE]:
                    sys.exit("Escape was pressed")
                elif entAllowed == True:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1012 and mouse[0] < 1405 and mouse[1] > 449 and mouse[1] < 883:
                        if sp == 1:
                            kiezCat = font.render("Gekozen door Speler 1", True, black)
                            screen.blit(kiezCat, (1045, 600))
                            pygame.display.update()
                            sp1c = 805
                            entAllowed = False
                            sp += 1
                            cnt += 1
                            break
                        elif sp == 2:
                            kiezCat = font.render("Gekozen door Speler 2", True,black)
                            screen.blit(kiezCat, (1045, 600))
                            pygame.display.update()
                            sp2c = 805
                            entAllowed = False
                            if maxp > 2:
                                sp += 1
                                cnt += 1
                                break
                            else:
                                cnt += 1
                                sp -= 1
                                break
                        elif sp == 3:
                            kiezCat = font.render("Gekozen door Speler 3", True,black)
                            screen.blit(kiezCat, (1045, 600))
                            pygame.display.update()
                            sp3c = 805
                            entAllowed = False
                            if maxp > 3:
                                sp += 1
                                cnt += 1
                                break
                            else:
                                sp = 1
                                cnt += 1
                                break
                        elif sp == 4:
                            kiezCat = font.render("Gekozen door Speler 4", True,black)
                            screen.blit(kiezCat, (1045, 600))
                            pygame.display.update()
                            sp4c = 805
                            sp = 1
                            entAllowed = False
                            cnt += 1
                            break
                    else:
                        pass
                if hisAllowed == True:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 35 and mouse[0] < 437 and mouse[1] > 445 and mouse[1] < 885:
                        if sp == 1:
                            kiezCat = font.render("Gekozen door Speler 1", True,black)
                            screen.blit(kiezCat, (75, 600))
                            pygame.display.update()
                            sp1c = 925
                            hisAllowed = False
                            sp += 1
                            cnt += 1
                            break
                        elif sp == 2:
                            kiezCat = font.render("Gekozen door Speler 2", True,black)
                            screen.blit(kiezCat, (75, 600))
                            pygame.display.update()
                            sp2c = 925
                            hisAllowed = False
                            if maxp > 2:
                                sp += 1
                                cnt += 1
                                break
                            else:
                                sp -= 1
                                cnt += 1
                                break
                        elif sp == 3:
                            kiezCat = font.render("Gekozen door Speler 3", True,black)
                            screen.blit(kiezCat, (75, 600))
                            pygame.display.update()
                            sp3c = 925
                            hisAllowed = False
                            if maxp > 3:
                                sp += 1
                                cnt += 1
                                break
                            else:
                                sp = 1
                                cnt += 1
                                break
                        elif sp == 4:
                            kiezCat = font.render("Gekozen door Speler 4", True,black)
                            screen.blit(kiezCat, (75, 600))
                            pygame.display.update()
                            sp4c = 925
                            sp = 1
                            hisAllowed = False
                            cnt += 1
                            break
                    else:
                        pass
                if sportAllowed:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1487 and mouse[0] < 1882 and mouse[1] > 444 and mouse[1] < 833:
                        if sp == 1:
                            kiezCat = font.render("Gekozen door Speler 1", True,black)
                            screen.blit(kiezCat, (1520, 600))
                            pygame.display.update()
                            sp1c = 1165
                            sportAllowed = False
                            sp += 1
                            cnt += 1
                            break
                        elif sp == 2:
                            kiezCat = font.render("Gekozen door Speler 2", True,black)
                            screen.blit(kiezCat, (1520, 600))
                            pygame.display.update()
                            sp2c = 1165
                            sportAllowed = False
                            if maxp > 2:
                                sp += 1
                                cnt += 1
                                break
                            else:
                                sp -= 1
                                cnt += 1
                                break
                        elif sp == 3:
                            kiezCat = font.render("Gekozen door Speler 3", True,black)
                            screen.blit(kiezCat, (1520, 600))
                            pygame.display.update()
                            sp3c = 1165
                            sportAllowed = False
                            if maxp > 3:
                                sp += 1
                                cnt += 1
                                break
                            else:
                                sp = 1
                                cnt += 1
                                break
                        elif sp == 4:
                            kiezCat = font.render("Gekozen door Speler 4", True,black)
                            screen.blit(kiezCat, (1520, 600))
                            pygame.display.update()
                            sp4c = 1165
                            sp = 1
                            sportAllowed = False
                            cnt += 1
                            break
                    else:
                        pass
                if geoAllowed == True:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 525 and mouse[0] < 920 and mouse[1] > 466  and mouse[1] < 887:
                        if sp == 1:
                            kiezCat = font.render("Gekozen door Speler 1", True,black)
                            screen.blit(kiezCat, (550, 600))
                            pygame.display.update()
                            sp1c = 1045
                            geoAllowed = False
                            sp += 1
                            cnt += 1
                            break
                        elif sp == 2:
                            kiezCat = font.render("Gekozen door Speler 2", True,black)
                            screen.blit(kiezCat, (550, 600))
                            pygame.display.update()
                            sp2c = 1045
                            geoAllowed = False
                            if maxp > 2:
                                sp += 1
                                cnt += 1
                                break
                            else:
                                sp -= 1
                                cnt += 1
                                break
                        elif sp == 3:
                            kiezCat = font.render("Gekozen door Speler 3", True,black)
                            screen.blit(kiezCat, (550, 600))
                            pygame.display.update()
                            sp3c = 1045
                            geoAllowed = False
                            if maxp > 3:
                                sp += 1
                                cnt += 1
                                break
                            else:
                                sp = 1
                                cnt += 1
                                break
                        elif sp == 4:
                            kiezCat = font.render("Gekozen door Speler 4", True,black)
                            screen.blit(kiezCat, (550, 600))
                            pygame.display.update()
                            sp4c = 1045
                            sp = 1
                            geoAllowed = False
                            cnt += 1
                            break
                    else:
                        pass
        else:
            time.sleep(5)
            assignCat = False


    if maxp >= 2:
        playerOne = Player(sp1c, 990, playerOneAfb, player1name) #805, 990
        playerTwo = Player(sp2c, 990, playerTwoAfb, player2name) #925, 990
    if maxp >= 3:
        playerThree = Player(sp3c, 990, playerThreeAfb, player3name) #1045, 990
    if maxp == 4:
        playerFour = Player(sp4c, 990, playerFourAfb, player4name) #1165, 990

    winnerfound = False
    mainloop = True
    x = True
    dobbelloop = True
    questionABC = False
    len3 = 0
    meerkeuzeLoop = False
    openvraagLoop = False
    questionOPEN = False
    optie3 = None
    richtingLoop = True

    while mainloop:
        clock.tick(60)
        #Exit:
        k = pygame.key.get_pressed()
        if k[K_ESCAPE]:
            mainloop = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop = False


        #Kijken of er een winnaar is
        if winnerfound == False:
            pass
        else:
            while x == True:

                mouse = pygame.mouse.get_pos()
                text("De winnaar is {}!".format(winner), (7, 7), 60)
                mainbutton = pygame.image.load("Afbeeldingen/mainbutton.png")
                screen.blit(mainbutton, (1500, 50))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1502 and mouse[0] < 1798 and mouse[1] > 53 and mouse[1] < 149:
                        winnerfound = False
                        program(maxp)
                pygame.display.update()

        if cp == 1:
            if playerOne.x == 805 or playerOne.x == 865 or playerOne.x == 926:
                questionCat = "Entertainment"
                screen.blit(background1, (0,0))
            elif playerOne.x == 925 or playerOne.x == 985 or playerOne.x == 986:
                questionCat = "History"
                screen.blit(background2, (0, 0))
            elif playerOne.x == 1045 or playerOne.x == 1105 or playerOne.x == 1046:
                questionCat = "Geography"
                screen.blit(background3, (0, 0))
            elif playerOne.x == 1165 or playerOne.x == 1225 or playerOne.x == 1106:
                questionCat = "Sport"
                screen.blit(background4, (0, 0))
        elif cp == 2:
            if playerTwo.x == 805 or playerTwo.x == 865 or playerTwo.x == 926:
                questionCat = "Entertainment"
                screen.blit(background1, (0,0))
            elif playerTwo.x == 925 or playerTwo.x == 985 or playerTwo.x == 986:
                questionCat = "History"
                screen.blit(background2, (0, 0))
            elif playerTwo.x == 1045 or playerTwo.x == 1105 or playerTwo.x == 1046:
                questionCat = "Geography"
                screen.blit(background3, (0, 0))
            elif playerTwo.x == 1165 or playerTwo.x == 1225 or playerTwo.x == 1106:
                questionCat = "Sport"
                screen.blit(background4, (0, 0))
        elif cp == 3:
            if playerThree.x == 805 or playerThree.x == 865 or playerThree.x == 926:
                questionCat = "Entertainment"
                screen.blit(background1, (0, 0))
            elif playerThree.x == 925 or playerThree.x == 985 or playerThree.x == 986:
                questionCat = "History"
                screen.blit(background2, (0, 0))
            elif playerThree.x == 1045 or playerThree.x == 1105 or playerThree.x == 1046:
                questionCat = "Geography"
                screen.blit(background3, (0, 0))
            elif playerThree.x == 1165 or playerThree.x == 1225 or playerThree.x == 1106:
                questionCat = "Sport"
                screen.blit(background4, (0, 0))
        elif cp == 4:
            if playerFour.x == 805 or playerFour.x == 865 or playerFour.x == 926:
                questionCat = "Entertainment"
                screen.blit(background1, (0, 0))
            elif playerFour.x == 925 or playerFour.x == 985 or playerFour.x == 986:
                questionCat = "History"
                screen.blit(background2, (0, 0))
            elif playerFour.x == 1045 or playerFour.x == 1105 or playerFour.x == 1046:
                questionCat = "Geography"
                screen.blit(background3, (0, 0))
            elif playerFour.x == 1165 or playerFour.x == 1225 or playerFour.x == 1106:
                questionCat = "Sport"
                screen.blit(background4, (0, 0))


        if cp == 1:
            naam = playerOne.name
        elif cp == 2:
            naam = playerTwo.name
        elif cp == 3:
            naam = playerThree.name
        elif cp == 4:
            naam = playerFour.name


        labelCP = font.render(naam + " is nu aan de beurt.", True, black)
        labelCat = font.render("De categorie is: " + questionCat, True, black)
        labelQw = font.render("Beantwoord de onderstaande vraag correct:", True, black)
        labelScore = font.render("Scores:", True, black)
        labelRichtingKiezen = font.render("Kies eerst een richting voordat", True, black)
        labelRichtingKiezen2 = font.render("u de dobbelsteen gooit.", True, black)
        screen.blit(labelCP, (40, 43))
        screen.blit(labelCat, (49, 145))
        screen.blit(labelQw, (49, 165))
        screen.blit(labelScore, (1446, 43))
        screen.blit(labelRichtingKiezen, (1446, 370))
        screen.blit(labelRichtingKiezen2, (1446, 390))
        if maxp == 2:
            scoreP1 = font.render(playerOne.name + ": " + str(playerOne.score), True, black)
            scoreP2 = font.render(playerTwo.name + ": " + str(playerTwo.score), True, black)
        elif maxp == 3:
            scoreP1 = font.render(playerOne.name + ": " + str(playerOne.score), True, black)
            scoreP2 = font.render(playerTwo.name + ": " + str(playerTwo.score), True, black)
            scoreP3 = font.render(playerThree.name + ": " + str(playerThree.score), True, black)
        elif maxp == 4:
            scoreP1 = font.render(playerOne.name + ": " + str(playerOne.score), True, black)
            scoreP2 = font.render(playerTwo.name + ": " + str(playerTwo.score), True, black)
            scoreP3 = font.render(playerThree.name + ": " + str(playerThree.score), True, black)
            scoreP4 = font.render(playerFour.name + ": " + str(playerFour.score), True, black)


        if maxp <= 2:
            playerOne.draw(screen)
            playerTwo.draw(screen)
            screen.blit(scoreP1, (1446, 63))
            screen.blit(scoreP2, (1446, 83))
        elif maxp == 3:
            playerOne.draw(screen)
            playerTwo.draw(screen)
            playerThree.draw(screen)
            screen.blit(scoreP1, (1446, 63))
            screen.blit(scoreP2, (1446, 83))
            screen.blit(scoreP3, (1446, 103))
        else:
            playerOne.draw(screen)
            playerTwo.draw(screen)
            playerThree.draw(screen)
            playerFour.draw(screen)
            screen.blit(scoreP1, (1446, 63))
            screen.blit(scoreP2, (1446, 83))
            screen.blit(scoreP3, (1446, 103))
            screen.blit(scoreP4, (1446, 123))
        pygame.display.update()

        while richtingLoop == True:
            mouse = pygame.mouse.get_pos()
            k = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
                elif k[pygame.K_ESCAPE]:
                    sys.exit("Escape was pressed")
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1474 and mouse[0] < 1590 and mouse[1] > 931 and mouse[1] < 1045:
                    richting = "links"
                    richtingLabel = font.render("Uw gekozen richting: " + str(richting), True, black)
                    richtingLoop = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1603 and mouse[0] < 1727 and mouse[1] > 775 and mouse[1] < 898:
                    richting = "omhoog"
                    richtingLabel = font.render("Uw gekozen richting: " + str(richting), True, black)
                    richtingLoop = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1737 and mouse[0] < 1857 and mouse[1] > 926 and mouse[1] < 1046:
                    richting = "rechts"
                    richtingLabel = font.render("Uw gekozen richting: " + str(richting), True, black)
                    richtingLoop = False

        if questionCat == "Entertainment":
            screen.blit(background1, (0, 0))
        elif questionCat == "History":
            screen.blit(background2, (0, 0))
        elif questionCat == "Geography":
            screen.blit(background3, (0, 0))
        else:
            screen.blit(background4, (0, 0))
        screen.blit(dn, (1510,470))
        screen.blit(labelCP, (40, 43))
        screen.blit(labelCat, (49, 145))
        screen.blit(labelQw, (49, 165))
        screen.blit(labelScore, (1446, 43))
        screen.blit(richtingLabel, (1446, 410))
        if maxp <= 2:
            playerOne.draw(screen)
            playerTwo.draw(screen)
            screen.blit(scoreP1, (1446, 63))
            screen.blit(scoreP2, (1446, 83))
        elif maxp == 3:
            playerOne.draw(screen)
            playerTwo.draw(screen)
            playerThree.draw(screen)
            screen.blit(scoreP1, (1446, 63))
            screen.blit(scoreP2, (1446, 83))
            screen.blit(scoreP3, (1446, 103))
        else:
            playerOne.draw(screen)
            playerTwo.draw(screen)
            playerThree.draw(screen)
            playerFour.draw(screen)
            screen.blit(scoreP1, (1446, 63))
            screen.blit(scoreP2, (1446, 83))
            screen.blit(scoreP3, (1446, 103))
            screen.blit(scoreP4, (1446, 123))
        pygame.display.update()

        #Unlock de dobbelsteen
        while dobbelloop == True:
            #Mainloop voor dobbelsteen
            k = pygame.key.get_pressed()
            for event in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                if k[pygame.K_ESCAPE]:
                    sys.exit("Escape was pressed")
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1516 and mouse[0] < 1705 and mouse[1] > 471 and mouse[1] < 664:
                    if winnerfound == False:
                        keren = [5, 6, 7, 8, 9, 10]
                        dobbelsteenZijde = [d1, d2, d3, d4, d5, d6]
                        aantalKeer = random.choice(keren)
                        for i in range(0, aantalKeer):
                            zijde = random.choice(dobbelsteenZijde)
                            screen.blit(zijde, (1510,470))
                            pygame.display.update()
                            time.sleep(0.5)
                        cg = diceThrow()
                        if cg == 2 or cg == 4 or cg == 6:
                            if cg == 2:
                                screen.blit(d2, (1510, 470))
                            elif cg == 4:
                                screen.blit(d4, (1510, 470))
                            elif cg == 6:
                                screen.blit(d6, (1510, 470))
                            meerkeuzeLoop = True
                            openvraagLoop = False
                        elif cg == 1 or cg == 3 or cg == 5:
                            if cg == 1:
                                screen.blit(d1, (1510, 470))
                            elif cg == 3:
                                screen.blit(d3, (1510, 470))
                            elif cg == 5:
                                screen.blit(d5, (1510, 470))
                            openvraagLoop = True
                            meerkeuzeLoop = False

                        if meerkeuzeLoop == True:
                            if cp == 1 or cp == 2 or cp == 3 or cp == 4:
                                randomQuestionID = getQuestion(questionCat, cg)
                                vraag = interact_with_database("SELECT Question FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                                questionList = wrapline(vraag, font, 500)
                                lenq = len(questionList)
                                optie1 = interact_with_database("SELECT answer1 FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                                optie2 = interact_with_database("SELECT answer2 FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                                optie3 = interact_with_database("SELECT answer3 FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                                optie1list = wrapline(optie1, font, 500)
                                optie2list = wrapline(optie2, font, 500)
                                if optie3 is not None:
                                    optie3list = wrapline(optie3, font, 500)
                                    len3 = len(optie3list)
                                else:
                                    optie3list = ""
                                    len3 = len(optie3list)
                                len1 = len(optie1list)
                                len2 = len(optie2list)
                                questionCorrect = interact_with_database("SELECT correct_answer FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                                questionCorrect2 = '123456789123456789123456789123456789'
                                questionCorrect3 = '123456789123456789123456789123456789'
                                questionCorrect4 = '123456789123456789123456789123456789'
                                questionCorrect1 = '123456789123456789123456789123456789'
                                questionABC = True
                                dobbelloop = False
                                questionOPEN = False
                        elif openvraagLoop == True:
                            if cp == 1 or cp == 2 or cp == 3 or cp == 4:
                                randomQuestionID = getQuestion(questionCat, cg)
                                vraag = interact_with_database("SELECT Question FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                                questionList = wrapline(vraag, font, 500)
                                lenq = len(questionList)
                                len1 = 0
                                len2 = 0
                                len3 = 0
                                questionCorrect1 = interact_with_database("SELECT correct_answer FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                                questionCorrect2 = interact_with_database("SELECT correct_answer2 FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                                questionCorrect3 = interact_with_database("SELECT correct_answer3 FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                                questionCorrect4 = interact_with_database("SELECT correct_answer4 FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                                if questionCorrect2 is None:
                                    questionCorrect2 = '123456789123456789123456789123456789'
                                if questionCorrect3 is None:
                                    questionCorrect3 = '123456789123456789123456789123456789'
                                if questionCorrect4 is None:
                                    questionCorrect4 = '123456789123456789123456789123456789'
                                questionABC = False
                                questionOPEN = True
                                dobbelloop = False


        #Start timer
        start_ticks = pygame.time.get_ticks()
        #Check gebruikers antwoord bij MEERKEUZEvraag
        if questionCat == "Entertainment":
            screen.blit(background1, (0, 0))
        elif questionCat == "History":
            screen.blit(background2, (0, 0))
        elif questionCat == "Geography":
            screen.blit(background3, (0, 0))
        else:
            screen.blit(background4, (0, 0))
        if cg == 2:
            screen.blit(d2, (1510, 470))
        elif cg == 4:
            screen.blit(d4, (1510, 470))
        elif cg == 6:
            screen.blit(d6, (1510, 470))
        elif cg == 1:
            screen.blit(d1, (1510, 470))
        elif cg == 3:
            screen.blit(d3, (1510, 470))
        elif cg == 5:
            screen.blit(d5, (1510, 470))
        screen.blit(labelCP, (40, 43))
        screen.blit(labelCat, (49, 145))
        screen.blit(labelQw, (49, 165))
        screen.blit(labelScore, (1446, 43))
        screen.blit(richtingLabel, (1446, 410))
        if maxp <= 2:
            playerOne.draw(screen)
            playerTwo.draw(screen)
            screen.blit(scoreP1, (1446, 63))
            screen.blit(scoreP2, (1446, 83))
        elif maxp == 3:
            playerOne.draw(screen)
            playerTwo.draw(screen)
            playerThree.draw(screen)
            screen.blit(scoreP1, (1446, 63))
            screen.blit(scoreP2, (1446, 83))
            screen.blit(scoreP3, (1446, 103))
        else:
            playerOne.draw(screen)
            playerTwo.draw(screen)
            playerThree.draw(screen)
            playerFour.draw(screen)
            screen.blit(scoreP1, (1446, 63))
            screen.blit(scoreP2, (1446, 83))
            screen.blit(scoreP3, (1446, 103))
            screen.blit(scoreP4, (1446, 123))
        if lenq > 0:
            labelq = font.render(questionList[0], True, black)
            screen.blit(labelq, (49, 200))
            if lenq > 1:
                labelq = font.render(questionList[1], True, black)
                screen.blit(labelq, (49, 220))
                if lenq > 2:
                    labelq = font.render(questionList[2], True, black)
                    screen.blit(labelq, (49, 240))
        if len1 > 0:
            label1 = font.render(optie1list[0], True, black)
            screen.blit(label1, (49, 520))
            if len1 > 1:
                label1 = font.render(optie1list[1], True, black)
                screen.blit(label1, (49, 540))
                if len1 > 2:
                    label1 = font.render(optie1list[2], True, black)
                    screen.blit(label1, (49, 560))
        if len2 > 0:
            labelOptie2 = font.render(optie2list[0], True, black)
            screen.blit(labelOptie2, (49, 620))
            if len2 > 1:
                labelOptie2 = font.render(optie2list[1], True, black)
                screen.blit(labelOptie2, (49, 640))
                if len2 > 2:
                    labelOptie2 = font.render(optie2list[2], True, black)
                    screen.blit(labelOptie2, (49, 660))
        if len3 > 0:
            labelOptie3 = font.render(optie3list[0], True, black)
            screen.blit(labelOptie3, (49, 740))
            if len3 > 1:
                labelOptie3 = font.render(optie3list[1], True, black)
                screen.blit(labelOptie3, (49, 760))
                if len3 > 2:
                    labelOptie3 = font.render(optie3list[2], True, black)
                    screen.blit(labelOptie3, (49, 780))
        if optie3 is None:
            screen.blit(buttoncover, (410,910))
        if questionABC == False:
            screen.blit(buttoncover, (410, 910))
            screen.blit(buttoncover, (10, 910))
            screen.blit(buttoncover, (200, 910))
        pygame.display.update()


        while questionABC == True:
            mils = timer - ((pygame.time.get_ticks() - start_ticks) / 1000)
            seconds = int(mils)
            mouse = pygame.mouse.get_pos()
            k = pygame.key.get_pressed()
            if optie3 is not None:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        mainloop = False
                    elif k[pygame.K_ESCAPE]:
                        sys.exit("Escape was pressed")
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 24 and mouse[0] < 190 and mouse[1] > 922 and mouse[1] < 1035:
                        print("A")
                        cpKeuze = "A"
                        questionABC = False
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 227 and mouse[0] < 390 and mouse[1] > 922 and mouse[1] < 1035:
                        print("B")
                        cpKeuze = "B"
                        questionABC = False
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 430 and mouse[0] < 590 and mouse[1] > 922 and mouse[1] < 1035:
                        print("C")
                        cpKeuze = "C"
                        questionABC = False
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        mainloop = False
                    elif k[pygame.K_ESCAPE]:
                        sys.exit("Escape was pressed")
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 24 and mouse[0] < 190 and mouse[1] > 922 and mouse[1] < 1035:
                        print("A")
                        cpKeuze = "A"
                        questionABC = False
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 227 and mouse[0] < 390 and mouse[1] > 922 and mouse[1] < 1035:
                        print("B")
                        cpKeuze = "B"
                        questionABC = False
            if seconds == -1:
                cpKeuze = " "
                questionABC = False
            elif seconds <= timer:
                screen.blit(brownbar, (216,460))
                timerLabel = font.render("Timer: "+ str(seconds), True, white)
                screen.blit(timerLabel, (216, 465))
                pygame.display.update()

        while questionOPEN == True:
            questionCorrect = interact_with_database("SELECT correct_answer FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
            cpKeuze = ask2(screen, "Antwoord", font, brownbar, white, timer)
            if questionCorrect1 == cpKeuze or questionCorrect2 == cpKeuze or questionCorrect3 == cpKeuze or questionCorrect4 == cpKeuze:
                cpKeuze = interact_with_database("SELECT correct_answer FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
            else:
                cpKeuze = "123456789123456789123456789"
            questionOPEN = False

        if questionCorrect != cpKeuze:
            QuestionWrong.play()
            questionFalse = font2.render("Uw keuze was incorrect.", True, red)
            screen.blit(questionFalse, (49, 390))
            pygame.display.update()
            time.sleep(3)
        else:
            QuestionRight.play()
            if cp == 1:
                playerOne.addScore()
            elif cp == 2:
                playerTwo.addScore()
            elif cp == 3:
                playerThree.addScore()
            elif cp == 4:
                playerFour.addScore()
            questionTrue = font2.render("Uw keuze was correct.", True, green)
            continueDobbel = font.render("U zult nu in de gekozen richting bewegen.", True, black)
            screen.blit(questionTrue, (49, 350))
            screen.blit(continueDobbel, (49, 390))
            screen.blit(richtingLabel, (1446, 410))
            pygame.display.update()
            time.sleep(2)
            if cg == 1 or cg == 2:
                cg = 1
            elif cg == 3 or cg == 4:
                cg = 2
            elif cg == 5 or cg == 6:
                cg = 3
            movement = True
            while movement == True:
                mouse = pygame.mouse.get_pos()
                k = pygame.key.get_pressed()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        mainloop = False
                    elif k[pygame.K_ESCAPE]:
                        sys.exit("Escape was pressed")
                if richting == "links":
                    if cp == 1:
                        playerOne.updatel(cg)
                    elif cp == 2:
                        playerTwo.updatel(cg)
                    elif cp == 3:
                        playerThree.updatel(cg)
                    else:
                        playerFour.updatel(cg)
                    movement = False
                elif richting == "omhoog":
                    if cp == 1:
                        playerOne.updatef(cg)
                        if playerOne.y <= 48:
                            winner = 1
                            termination = True
                            mainloop = False
                    elif cp == 2:
                        playerTwo.updatef(cg)
                        if playerTwo.y <= 48:
                            winner = 2
                            termination = True
                            mainloop = False
                    elif cp == 3:
                        playerThree.updatef(cg)
                        if playerThree.y <= 48:
                            winner = 3
                            termination = True
                            mainloop = False
                    elif cp == 4:
                        playerFour.updatef(cg)
                        if playerFour.y <= 48:
                            winner = 4
                            termination = True
                            mainloop = False
                    movement = False
                elif richting == "rechts":
                    if cp == 1:
                        playerOne.updater(cg)
                    elif cp == 2:
                        playerTwo.updater(cg)
                    elif cp == 3:
                        playerThree.updater(cg)
                    elif cp == 4:
                        playerFour.updater(cg)
                    movement = False

        if questionCat == "Entertainment":
            screen.blit(background1, (0, 0))
        elif questionCat == "History":
            screen.blit(background2, (0, 0))
        elif questionCat == "Geography":
            screen.blit(background3, (0, 0))
        else:
            screen.blit(background4, (0, 0))
        screen.blit(labelCP, (40, 43))
        screen.blit(labelCat, (49, 145))
        screen.blit(labelQw, (49, 165))
        screen.blit(labelScore, (1446, 43))
        if maxp <= 2:
            playerOne.draw(screen)
            playerTwo.draw(screen)
            screen.blit(scoreP1, (1446, 63))
            screen.blit(scoreP2, (1446, 83))
        elif maxp == 3:
            playerOne.draw(screen)
            playerTwo.draw(screen)
            playerThree.draw(screen)
            screen.blit(scoreP1, (1446, 63))
            screen.blit(scoreP2, (1446, 83))
            screen.blit(scoreP3, (1446, 103))
        else:
            playerOne.draw(screen)
            playerTwo.draw(screen)
            playerThree.draw(screen)
            playerFour.draw(screen)
            screen.blit(scoreP1, (1446, 63))
            screen.blit(scoreP2, (1446, 83))
            screen.blit(scoreP3, (1446, 103))
            screen.blit(scoreP4, (1446, 123))

        pygame.display.update()
        dobbelloop = True
        questionABC = False
        moveBackLoop = False
        richtingLoop = True

        if cp == 1:
            if playerOne.x == playerTwo.x and playerOne.y == playerTwo.y:
                mb = 2
                moveBackLabel = font.render(playerOne.name + " staat op " + playerTwo.name, True, black)
                moveBackLabel2 = font.render(playerTwo.name + " zal nu achteruit moeten gaan.", True, black)
                moveBackLabel3 = font.render("Druk op de dobbelsteen om te zien hoeveel stappen", True, black)
                moveBackLabel4 = font.render("je achteruit zal gaan.", True, black)
                screen.blit(moveBackLabel, (49, 520))
                screen.blit(moveBackLabel2, (49, 540))
                screen.blit(moveBackLabel3, (49, 560))
                screen.blit(moveBackLabel4, (49, 580))
                pygame.display.update()
                moveBackLoop = True
            if maxp > 2:
                if playerOne.x == playerThree.x and playerOne.y == playerThree.y:
                    mb = 3
                    moveBackLabel = font.render(playerOne.name + " staat op " + playerThree.name, True, black)
                    moveBackLabel2 = font.render(playerThree.name + " zal nu achteruit moeten gaan.", True, black)
                    moveBackLabel3 = font.render("Druk op de dobbelsteen om te zien hoeveel stappen", True, black)
                    moveBackLabel4 = font.render("je achteruit zal gaan.", True, black)
                    screen.blit(moveBackLabel, (49, 520))
                    screen.blit(moveBackLabel2, (49, 540))
                    screen.blit(moveBackLabel3, (49, 560))
                    screen.blit(moveBackLabel4, (49, 580))
                    pygame.display.update()
                    moveBackLoop = True
                if maxp > 3:
                    if playerOne.x == playerFour.x and playerOne.y == playerFour.y:
                        mb = 4
                        moveBackLabel = font.render(playerOne.name + " staat op " + playerFour.name, True, black)
                        moveBackLabel2 = font.render(playerFour.name + " zal nu achteruit moeten gaan.", True, black)
                        moveBackLabel3 = font.render("Druk op de dobbelsteen om te zien hoeveel stappen", True, black)
                        moveBackLabel4 = font.render("je achteruit zal gaan.", True, black)
                        screen.blit(moveBackLabel, (49, 520))
                        screen.blit(moveBackLabel2, (49, 540))
                        screen.blit(moveBackLabel3, (49, 560))
                        screen.blit(moveBackLabel4, (49, 580))
                        pygame.display.update()
                        moveBackLoop = True
                        print("IK ZIT HIERO")
        elif cp == 2:
            if playerTwo.x == playerOne.x and playerTwo.y == playerOne.y:
                mb = 1
                moveBackLabel = font.render(playerTwo.name + " staat op " + playerOne.name, True, black)
                moveBackLabel2 = font.render(playerOne.name + " zal nu achteruit moeten gaan.", True, black)
                moveBackLabel3 = font.render("Druk op de dobbelsteen om te zien hoeveel stappen", True, black)
                moveBackLabel4 = font.render("je achteruit zal gaan.", True, black)
                screen.blit(moveBackLabel, (49, 520))
                screen.blit(moveBackLabel2, (49, 540))
                screen.blit(moveBackLabel3, (49, 560))
                screen.blit(moveBackLabel4, (49, 580))
                pygame.display.update()
                moveBackLoop = True
            if maxp > 2:
                if playerTwo.x == playerThree.x and playerTwo.y == playerThree.y:
                    mb = 3
                    moveBackLabel = font.render(playerTwo.name + " staat op " + playerThree.name, True, black)
                    moveBackLabel2 = font.render(playerThree.name + " zal nu achteruit moeten gaan.", True, black)
                    moveBackLabel3 = font.render("Druk op de dobbelsteen om te zien hoeveel stappen", True, black)
                    moveBackLabel4 = font.render("je achteruit zal gaan.", True, black)
                    screen.blit(moveBackLabel, (49, 520))
                    screen.blit(moveBackLabel2, (49, 540))
                    screen.blit(moveBackLabel3, (49, 560))
                    screen.blit(moveBackLabel4, (49, 580))
                    pygame.display.update()
                    moveBackLoop = True
                if maxp > 3:
                    if playerTwo.x == playerFour.x and playerTwo.y == playerFour.y:
                        mb = 4
                        moveBackLabel = font.render(playerTwo.name + " staat op " + playerFour.name, True, black)
                        moveBackLabel2 = font.render(playerFour.name + " zal nu achteruit moeten gaan.", True, black)
                        moveBackLabel3 = font.render("Druk op de dobbelsteen om te zien hoeveel stappen", True, black)
                        moveBackLabel4 = font.render("je achteruit zal gaan.", True, black)
                        screen.blit(moveBackLabel, (49, 520))
                        screen.blit(moveBackLabel2, (49, 540))
                        screen.blit(moveBackLabel3, (49, 560))
                        screen.blit(moveBackLabel4, (49, 580))
                        pygame.display.update()
                        moveBackLoop = True
        elif cp == 3:
            if playerThree.x == playerOne.x and playerThree.y == playerOne.y:
                mb = 1
                moveBackLabel = font.render(playerThree.name + " staat op " + playerOne.name, True, black)
                moveBackLabel2 = font.render(playerOne.name + " zal nu achteruit moeten gaan.", True, black)
                moveBackLabel3 = font.render("Druk op de dobbelsteen om te zien hoeveel stappen", True, black)
                moveBackLabel4 = font.render("je achteruit zal gaan.", True, black)
                screen.blit(moveBackLabel, (49, 520))
                screen.blit(moveBackLabel2, (49, 540))
                screen.blit(moveBackLabel3, (49, 560))
                screen.blit(moveBackLabel4, (49, 580))
                pygame.display.update()
                moveBackLoop = True
            elif playerThree.x == playerTwo.x and playerThree.y == playerTwo.y:
                mb = 2
                moveBackLabel = font.render(playerThree.name + " staat op " + playerTwo.name, True, black)
                moveBackLabel2 = font.render(playerTwo.name + " zal nu achteruit moeten gaan.", True, black)
                moveBackLabel3 = font.render("Druk op de dobbelsteen om te zien hoeveel stappen", True, black)
                moveBackLabel4 = font.render("je achteruit zal gaan.", True, black)
                screen.blit(moveBackLabel, (49, 520))
                screen.blit(moveBackLabel2, (49, 540))
                screen.blit(moveBackLabel3, (49, 560))
                screen.blit(moveBackLabel4, (49, 580))
                pygame.display.update()
                moveBackLoop = True
            if maxp > 3:
                if playerThree.x == playerFour.x and playerThree.y == playerFour.y:
                    mb = 4
                    moveBackLabel = font.render(playerThree.name + " staat op " + playerFour.name, True, black)
                    moveBackLabel2 = font.render(playerFour.name + " zal nu achteruit moeten gaan.", True, black)
                    moveBackLabel3 = font.render("Druk op de dobbelsteen om te zien hoeveel stappen", True, black)
                    moveBackLabel4 = font.render("je achteruit zal gaan.", True, black)
                    screen.blit(moveBackLabel, (49, 520))
                    screen.blit(moveBackLabel2, (49, 540))
                    screen.blit(moveBackLabel3, (49, 560))
                    screen.blit(moveBackLabel4, (49, 580))
                    pygame.display.update()
                    moveBackLoop = True
        elif cp == 4:
            if playerFour.x == playerOne.x and playerFour.y == playerOne.y:
                mb = 1
                moveBackLabel = font.render(playerFour.name + " staat op " + playerOne.name, True, black)
                moveBackLabel2 = font.render(playerOne.name + " zal nu achteruit moeten gaan.", True, black)
                moveBackLabel3 = font.render("Druk op de dobbelsteen om te zien hoeveel stappen", True, black)
                moveBackLabel4 = font.render("je achteruit zal gaan.", True, black)
                screen.blit(moveBackLabel, (49, 520))
                screen.blit(moveBackLabel2, (49, 540))
                screen.blit(moveBackLabel3, (49, 560))
                screen.blit(moveBackLabel4, (49, 580))
                pygame.display.update()
                moveBackLoop = True
            elif playerFour.x == playerThree.x and playerFour.y == playerThree.y:
                mb = 3
                moveBackLabel = font.render(playerFour.name + " staat op " + playerThree.name, True, black)
                moveBackLabel2 = font.render(playerThree.name + " zal nu achteruit moeten gaan.", True, black)
                moveBackLabel3 = font.render("Druk op de dobbelsteen om te zien hoeveel stappen", True, black)
                moveBackLabel4 = font.render("je achteruit zal gaan.", True, black)
                screen.blit(moveBackLabel, (49, 520))
                screen.blit(moveBackLabel2, (49, 540))
                screen.blit(moveBackLabel3, (49, 560))
                screen.blit(moveBackLabel4, (49, 580))
                pygame.display.update()
                moveBackLoop = True
            elif playerFour.x == playerTwo.x and playerFour.y == playerTwo.y:
                mb = 2
                moveBackLabel = font.render(playerFour.name + " staat op " + playerTwo.name, True, black)
                moveBackLabel2 = font.render(playerTwo.name + " zal nu achteruit moeten gaan.", True, black)
                moveBackLabel3 = font.render("Druk op de dobbelsteen om te zien hoeveel stappen", True, black)
                moveBackLabel4 = font.render("je achteruit zal gaan.", True, black)
                screen.blit(moveBackLabel, (49, 520))
                screen.blit(moveBackLabel2, (49, 540))
                screen.blit(moveBackLabel3, (49, 560))
                screen.blit(moveBackLabel4, (49, 580))
                pygame.display.update()
                moveBackLoop = True


        while moveBackLoop == True:
            screen.blit(dn, (1510, 470))
            pygame.display.update()
            for event in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                k = pygame.key.get_pressed()
                if k[pygame.K_ESCAPE]:
                    sys.exit("Escape was pressed")
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1516 and mouse[0] < 1705 and mouse[1] > 471 and mouse[1] < 664:
                    keren = [5, 6, 7, 8, 9, 10]
                    dobbelsteenZijde = [d1, d2, d3, d4, d5, d6]
                    aantalKeer = random.choice(keren)
                    for i in range(0, aantalKeer):
                        zijde = random.choice(dobbelsteenZijde)
                        screen.blit(zijde, (1510,470))
                        pygame.display.update()
                        time.sleep(0.5)
                    cg = diceThrow()
                    if cg == 2:
                        screen.blit(d2, (1510, 470))
                    elif cg == 4:
                        screen.blit(d4, (1510, 470))
                    elif cg == 6:
                        screen.blit(d6, (1510, 470))
                    elif cg == 1:
                        screen.blit(d1, (1510, 470))
                    elif cg == 3:
                        screen.blit(d3, (1510, 470))
                    elif cg == 5:
                        screen.blit(d5, (1510, 470))
                    moveBackLabel5 = font.render("Je hebt " + str(cg) + " gegooid.", True, black)
                    screen.blit(moveBackLabel5, (49, 620))
                    if cg == 1 or cg == 2:
                        cg = 1
                    elif cg == 3 or cg == 4:
                        cg = 2
                    elif cg == 5 or cg == 6:
                        cg = 3
                    moveBackLabel6 = font.render("Je zal nu " + str(cg) + " stap(pen) achteruit gaan.", True, black)
                    screen.blit(moveBackLabel6, (49, 640))
                    pygame.display.update()
                    time.sleep(2)
                    if mb == 1:
                        playerOne.updateb(cg)
                        moveBackLoop = False
                    elif mb == 2:
                        playerTwo.updateb(cg)
                        moveBackLoop = False
                    elif mb == 3:
                        playerThree.updateb(cg)
                        moveBackLoop = False
                    elif mb == 4:
                        playerFour.updateb(cg)
                        moveBackLoop = False

        if maxp <= 2:
            playerOne.draw(screen)
            playerTwo.draw(screen)
            screen.blit(scoreP1, (1446, 63))
            screen.blit(scoreP2, (1446, 83))
        elif maxp == 3:
            playerOne.draw(screen)
            playerTwo.draw(screen)
            playerThree.draw(screen)
            screen.blit(scoreP1, (1446, 63))
            screen.blit(scoreP2, (1446, 83))
            screen.blit(scoreP3, (1446, 103))
        else:
            playerOne.draw(screen)
            playerTwo.draw(screen)
            playerThree.draw(screen)
            playerFour.draw(screen)
            screen.blit(scoreP1, (1446, 63))
            screen.blit(scoreP2, (1446, 83))
            screen.blit(scoreP3, (1446, 103))
            screen.blit(scoreP4, (1446, 123))
        pygame.display.update()

        if cp == 1:
            cp += 1
        elif cp == 2:
            if maxp > 2:
                cp += 1
            else:
                cp = 1
        elif cp == 3:
            if maxp > 3:
                cp += 1
            else: cp = 1
        else:
            cp = 1

    #Termination Screen
    if winnerfound == True:
        time.sleep(2)
        termination = True

    uploadScore = True
    while termination == True:
        screen.blit(terminationscreen, (0, 0))
        labelScore = font2.render("Eindscore:", True, white)
        screen.blit(labelScore, (130, 450))
        if maxp == 2:
            scoreP1 = font2.render(playerOne.name + ": " + str(playerOne.score), True, white)
            scoreP2 = font2.render(playerTwo.name + ": " + str(playerTwo.score), True, white)
        elif maxp == 3:
            scoreP1 = font2.render(playerOne.name + ": " + str(playerOne.score), True, white)
            scoreP2 = font2.render(playerTwo.name + ": " + str(playerTwo.score), True, white)
            scoreP3 = font2.render(playerThree.name + ": " + str(playerThree.score), True, white)
        elif maxp == 4:
            scoreP1 = font2.render(playerOne.name + ": " + str(playerOne.score), True, white)
            scoreP2 = font2.render(playerTwo.name + ": " + str(playerTwo.score), True, white)
            scoreP3 = font2.render(playerThree.name + ": " + str(playerThree.score), True, white)
            scoreP4 = font2.render(playerFour.name + ": " + str(playerFour.score), True, white)
        if maxp <= 2:
            screen.blit(scoreP1, (130, 500))
            screen.blit(scoreP2, (130, 540))
        elif maxp == 3:
            screen.blit(scoreP1, (130, 500))
            screen.blit(scoreP2, (130, 540))
            screen.blit(scoreP3, (130, 580))
        else:
            screen.blit(scoreP1, (130, 500))
            screen.blit(scoreP2, (130, 540))
            screen.blit(scoreP3, (130, 580))
            screen.blit(scoreP4, (130, 620))
        if winner == 1:
            winner = font2.render("De winnaar is: " + playerOne.name, True, black)
            screen.blit(winner, (130, 320))
        elif winner == 2:
            winner = font2.render("De winnaar is: " + playerTwo.name, True, white)
            screen.blit(winner, (130, 320))
        elif winner == 3:
            winner = font2.render("De winnaar is: " + playerThree.name, True, white)
            screen.blit(winner, (130, 320))
        elif winner == 4:
            winner = font2.render("De winnaar is: " + playerFour.name, True, white)
            screen.blit(winner, (130, 320))
        if uploadScore == True:
            if winner == 1:
                playerOne.winnerScore()
                if maxp == 2:
                    score(playerOne.name, playerOne.score, 1, 0)
                    score(playerTwo.name, playerTwo.score, 0, 1)
                    uploadScore = False
                elif maxp == 3:
                    score(playerOne.name, playerOne.score, 1, 0)
                    score(playerTwo.name, playerTwo.score, 0, 1)
                    score(playerThree.name, playerThree.score, 0, 1)
                    uploadScore = False
                elif maxp == 4:
                    score(playerOne.name, playerOne.score, 1, 0)
                    score(playerTwo.name, playerTwo.score, 0, 1)
                    score(playerThree.name, playerThree.score, 0, 1)
                    score(playerFour.name, playerFour.score, 0, 1)
                    uploadScore = False
            elif winner == 2:
                playerTwo.winnerScore()
                if maxp == 2:
                    score(playerOne.name, playerOne.score, 0, 1)
                    score(playerTwo.name, playerTwo.score, 1, 0)
                    uploadScore = False
                elif maxp == 3:
                    score(playerOne.name, playerOne.score, 0, 1)
                    score(playerTwo.name, playerTwo.score, 1, 0)
                    score(playerThree.name, playerThree.score, 0, 1)
                    uploadScore = False
                elif maxp == 4:
                    score(playerOne.name, playerOne.score, 0, 1)
                    score(playerTwo.name, playerTwo.score, 1, 0)
                    score(playerThree.name, playerThree.score, 0, 1)
                    score(playerFour.name, playerFour.score, 0, 1)
                    uploadScore = False
            elif winner == 3:
                playerThree.winnerScore()
                if maxp == 3:
                    score(playerOne.name, playerOne.score, 0, 1)
                    score(playerTwo.name, playerTwo.score, 0, 1)
                    score(playerThree.name, playerThree.score, 1, 0)
                    uploadScore = False
                elif maxp == 4:
                    score(playerOne.name, playerOne.score, 0, 1)
                    score(playerTwo.name, playerTwo.score, 0, 1)
                    score(playerThree.name, playerThree.score, 1, 0)
                    score(playerFour.name, playerFour.score, 0, 1)
                    uploadScore = False
            elif winner == 4:
                playerFour.winnerScore()
                score(playerOne.name, playerOne.score, 0, 1)
                score(playerTwo.name, playerTwo.score, 0, 1)
                score(playerThree.name, playerThree.score, 0, 1)
                score(playerFour.name, playerFour.score, 1, 0)
                uploadScore = False
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                    mouse = pygame.mouse.get_pos()
                    k = pygame.key.get_pressed()
                    if k[pygame.K_ESCAPE]:
                        sys.exit("Escape was pressed")
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 180 and mouse[0] < 1895 and mouse[1] > 180 and mouse[1] < 280:
                            pygame.quit()
                            sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1580 and mouse[0] < 1895 and mouse[1] > 30 and mouse[1] < 130:
                            program(maxp)




