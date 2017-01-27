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

    def updatef(self, cg):
        while cg > 0 and self.y > 0:
            if self.y == 477:
                if self.x == 805 or self.x == 865:
                    self.x = 930
                    self.y = 333
                elif self.x == 925 or self.x == 985:
                    self.x = 990
                    self.y = 333
                elif self.x == 1045 or self.x == 1105:
                    self.x = 1050
                    self.y = 333
                elif self.x == 1165 or self.x == 1225:
                    self.x = 1110
                    self.y = 333
            else:
                self.y -= 57
            cg -= 1

    def updatel(self, cg):
        while cg > 0:
            if self.x < 865 and self.y > 333:
                self.x = 1225
            else:
                self.x -= 60
            cg -= 1

    def updater(self, cg):
        while cg > 0:
            if self.x > 1165 and self.y > 333:
                self.x = 805
            else:
                self.x += 60
            cg -= 1

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


def program(maxp):
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    white = (255, 255, 255)
    width = 1920
    height = 1080
    size = (width, height)
    background1 = pygame.image.load("Afbeeldingen/gamebackgroundred.png")
    background2 = pygame.image.load("Afbeeldingen/gamebackgroundyellow.png")
    background3 = pygame.image.load("Afbeeldingen/gamebackgroundgreen.png")
    background4 = pygame.image.load("Afbeeldingen/gamebackgroundblue.png")
    nameInputBack = pygame.image.load("Afbeeldingen/naamInput.jpg")
    img1 = pygame.image.load("Afbeeldingen/SP1.png")
    img2 = pygame.image.load("Afbeeldingen/SP2.png")
    img3 = pygame.image.load("Afbeeldingen/SP3.png")
    img4 = pygame.image.load("Afbeeldingen/SP4.png")
    greenbar = pygame.image.load("Afbeeldingen/greenbar.png")
    brownbar = pygame.image.load("Afbeeldingen/brownbar.png")
    buttoncover = pygame.image.load("Afbeeldingen/buttoncover.png")
    d1 = pygame.image.load("Afbeeldingen/DS1.png")
    d2 = pygame.image.load("Afbeeldingen/DS2.png")
    d3 = pygame.image.load("Afbeeldingen/DS3.png")
    d4 = pygame.image.load("Afbeeldingen/DS4.png")
    d5 = pygame.image.load("Afbeeldingen/DS5.png")
    d6 = pygame.image.load("Afbeeldingen/DS6.png")
    dn = pygame.image.load("Afbeeldingen/DS0.png")


    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    font = pygame.font.Font(None, 30)
    font2 = pygame.font.Font(None, 50)

    def text(msg, pos, size=30):
        black = (0, 0, 0)
        font = pygame.font.Font(None, size)
        label = font.render(msg, True, black)
        screen.blit(label, pos)

    screen.blit(nameInputBack, (0, 0))

    errorName = font.render("Naam is al in gebruik! Vul een andere naam in!", True, red)


    player1name = (ask(screen, "Naam speler 1"))
    player2name = (ask(screen, "Naam speler 2"))
    while True:
        if player1name == player2name:
            screen.blit(errorName, (300, 130))
            pygame.display.update()
            player2name = (ask(screen, "Naam speler 2"))
        else:
            screen.blit(nameInputBack, (0, 0))
            break
    if maxp == 3:
        player3name = (ask(screen, "Naam speler 3"))
        while True:
            if player3name == player2name or player3name == player1name:
                screen.blit(errorName, (300, 130))
                pygame.display.update()
                player2name = (ask(screen, "Naam speler 3"))
            else:
                screen.blit(nameInputBack, (0, 0))
                break
    if maxp == 4:
        player3name = (ask(screen, "Naam speler 3"))
        while True:
            if player3name == player2name or player3name == player1name:
                screen.blit(errorName, (300, 130))
                pygame.display.update()
                player2name = (ask(screen, "Naam speler 3"))
            else:
                screen.blit(nameInputBack, (0, 0))
                break
        player4name = (ask(screen, "Naam speler 4"))
        while True:
            if player4name == player1name or player4name == player2name or player4name == player3name:
                screen.blit(errorName, (300, 130))
                pygame.display.update()
                player4name = (ask(screen, "Naam speler 4"))
            else:
                screen.blit(nameInputBack, (0, 0))
                break

    if maxp >= 2:
        playerOne = Player(805, 990, img1, player1name)
        playerTwo = Player(925, 990, img2, player2name)
    if maxp >= 3:
        playerThree = Player(1045, 990, img3, player3name)
    if maxp == 4:
        playerFour = Player(1165, 990, img4, player4name)

    cp = 1
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
            if playerOne.x == 805 or playerOne.x == 865:
                questionCat = "Entertainment"
                screen.blit(background1, (0,0))
            elif playerOne.x == 925 or playerOne.x == 985:
                questionCat = "History"
                screen.blit(background2, (0, 0))
            elif playerOne.x == 1045 or playerOne.x == 1105:
                questionCat = "Geography"
                screen.blit(background3, (0, 0))
            elif playerOne.x == 1165 or playerOne.x == 1225:
                questionCat = "Sport"
                screen.blit(background4, (0, 0))
        elif cp == 2:
            if playerTwo.x == 805 or playerTwo.x == 865:
                questionCat = "Entertainment"
                screen.blit(background1, (0,0))
            elif playerTwo.x == 925 or playerTwo.x == 985:
                questionCat = "History"
                screen.blit(background2, (0, 0))
            elif playerTwo.x == 1045 or playerTwo.x == 1105:
                questionCat = "Geography"
                screen.blit(background3, (0, 0))
            elif playerTwo.x == 1165 or playerTwo.x == 1225:
                questionCat = "Sport"
                screen.blit(background4, (0, 0))
        elif cp == 3:
            if playerThree.x == 805 or playerThree.x == 865:
                questionCat = "Entertainment"
                screen.blit(background1, (0, 0))
            elif playerThree.x == 925 or playerThree.x == 985:
                questionCat = "History"
                screen.blit(background2, (0, 0))
            elif playerThree.x == 1045 or playerThree.x == 1105:
                questionCat = "Geography"
                screen.blit(background3, (0, 0))
            elif playerThree.x == 1165 or playerThree.x == 1225:
                questionCat = "Sport"
                screen.blit(background4, (0, 0))
        elif cp == 4:
            if playerFour.x == 805 or playerFour.x == 865:
                questionCat = "Entertainment"
                screen.blit(background1, (0, 0))
            elif playerFour.x == 925 or playerFour.x == 985:
                questionCat = "History"
                screen.blit(background2, (0, 0))
            elif playerFour.x == 1045 or playerFour.x == 1105:
                questionCat = "Geography"
                screen.blit(background3, (0, 0))
            elif playerFour.x == 1165 or playerFour.x == 1225:
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
        screen.blit(labelCP, (40, 43))
        screen.blit(labelCat, (49, 145))
        screen.blit(labelQw, (49, 165))
        screen.blit(dn, (1510,470))

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
                        # keren = [5, 6, 7, 8, 9, 10]
                        # dobbelsteenZijde = [d1, d2, d3, d4, d5, d6]
                        # aantalKeer = random.choice(keren)
                        # for i in range(0, aantalKeer):
                        #     zijde = random.choice(dobbelsteenZijde)
                        if True:
                            if questionCat == "Entertainment":
                                screen.blit(background1, (0, 0))
                            elif questionCat == "History":
                                screen.blit(background2, (0, 0))
                            elif questionCat == "Geography":
                                screen.blit(background3, (0, 0))
                            else:
                                screen.blit(background4, (0, 0))
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
                            # screen.blit(zijde, (1510,470))
                            screen.blit(labelCP, (40, 43))
                            screen.blit(labelCat, (49, 145))
                            screen.blit(labelQw, (49, 165))
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
                                questionCorrect = interact_with_database("SELECT correct_answer FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
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
            mils = 50 - ((pygame.time.get_ticks() - start_ticks) / 1000)
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
            if seconds > 50:
                cpKeuze = " "
                questionABC = False
            elif seconds <= 50:
                screen.blit(brownbar, (216,460))
                timerLabel = font.render("Timer: "+ str(seconds), True, white)
                screen.blit(timerLabel, (216, 465))
                pygame.display.update()

        while questionOPEN == True:
            cpKeuze = ask2(screen, "Antwoord", font, brownbar, white)
            questionOPEN = False


        # if questionCorrect != cpKeuze:
        #     questionFalse = font2.render("Uw keuze was incorrect.", True, red)
        #     screen.blit(questionFalse, (49, 390))
        #     pygame.display.update()
        #     time.sleep(3)
        #     if cp == 1:
        #         cp += 1
        #     elif cp == 2:
        #         if maxp > 2:
        #             cp += 1
        #         else:
        #             cp -= 1
        #     elif cp == 3:
        #         if maxp > 3:
        #             cp += 1
        #         else:
        #             cp -= 2
        #     elif cp == 4:
        #         cp -= 3
        if True == True:
            questionTrue = font2.render("Uw keuze was correct.", True, green)
            continueDobbel = font2.render("U kunt nu een richting kiezen.", True, black)
            screen.blit(questionTrue, (49, 360))
            screen.blit(continueDobbel, (49, 390))
            pygame.display.update()
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
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1474 and mouse[0] < 1590 and mouse[1] > 931 and mouse[1] < 1045:
                        if cp == 1:
                            playerOne.updatel(cg)
                            cp += 1
                        elif cp == 2:
                            playerTwo.updatel(cg)
                            if maxp > 2:
                                cp += 1
                            else:
                                cp -= 1
                        elif cp == 3:
                            playerThree.updatel(cg)
                            if maxp > 3:
                                cp += 1
                            else:
                                cp -= 2
                        elif cp == 4:
                            playerFour.updatel(cg)
                            cp -= 3
                        movement = False
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1603 and mouse[0] < 1727 and mouse[1] > 775 and mouse[1] < 898:
                        if cp == 1:
                            playerOne.updatef(1)
                            cp += 1
                            if playerOne.y < 121:
                                winner = "Player 1"
                                winnerfound = True
                        elif cp == 2:
                            playerTwo.updatef(1)
                            if maxp > 2:
                                cp += 1
                            else:
                                cp -= 1
                            if playerTwo.y < 121:
                                winner = "Player 2"
                                winnerfound = True
                        elif cp == 3:
                            playerThree.updatef(cg)
                            if maxp > 3:
                                cp += 1
                            else:
                                cp -= 2
                            if playerThree.y < 121:
                                winnerfound = True
                                winner = "Player 3"
                        elif cp == 4:
                            playerFour.updatef(cg)
                            cp -= 3
                            if playerFour.y < 121:
                                winner = "Player 4"
                                winnerfound = True
                        movement = False
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1737 and mouse[0] < 1857 and mouse[1] > 926 and mouse[1] < 1046:
                        if cp == 1:
                            playerOne.updater(cg)
                            cp += 1
                        elif cp == 2:
                            playerTwo.updater(cg)
                            if maxp > 2:
                                cp += 1
                            else:
                                cp -= 1
                        elif cp == 3:
                            playerThree.updater(cg)
                            if maxp > 3:
                                cp += 1
                            else:
                                cp -= 2
                        elif cp == 4:
                            playerFour.updater(cg)
                            cp -= 3
                        movement = False

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
        pygame.display.update()
        dobbelloop = True
        questionABC = False

