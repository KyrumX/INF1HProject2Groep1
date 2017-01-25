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
    gooi = [1, 2, 3]
    throw = random.choice(gooi)
    return throw

def getQuestion(questionCat):
    questionList = get_questions(questionCat)
    questionPicked = random.choice(questionList)
    questionID = questionPicked[0]
    return questionID


class Player:
    def __init__(self, x, y, image, name):
        self.x = x
        self.y = y
        self.name = name
        self.image = image

    def update(self, cg):
        while cg > 0 and self.y > 0:
            if self.y <= 386:
                self.x = 940
            self.y -= 69
            cg -= 1

    def draw(self, screen):

        win1 = pygame.image.load("Afbeeldingen/SP1winner.png")
        win2 = pygame.image.load("Afbeeldingen/SP2winner.png")
        win3 = pygame.image.load("Afbeeldingen/SP3winner.png")
        win4 = pygame.image.load("Afbeeldingen/SP4winner.png")

        if self.y < 41:
            if self.player == 1:
                self.image = win1
                print(self.y)
            elif self.player == 2:
                self.image = win2
                print(self.y)
            elif self.player == 3:
                self.image = win3
            else:
                self.image = win4
        screen.blit(self.image, (self.x, self.y))


def program(maxp):
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    width = 1920
    height = 1080
    size = (width, height)
    background1 = pygame.image.load("Afbeeldingen/gameboard.png")
    background2 = pygame.image.load("Afbeeldingen/gameboard2.png")
    background3 = pygame.image.load("Afbeeldingen/gameboard3.png")
    background4 = pygame.image.load("Afbeeldingen/gameboard4.png")
    background5 = pygame.image.load("Afbeeldingen/gameboard5.png")
    background6 = pygame.image.load("Afbeeldingen/gameboard6.png")
    nameInputBack = pygame.image.load("Afbeeldingen/naamInput.jpg")
    main = pygame.image.load("Afbeeldingen/gameboardMain.png")
    img1 = pygame.image.load("Afbeeldingen/SP1.png")
    img2 = pygame.image.load("Afbeeldingen/SP2.png")
    img3 = pygame.image.load("Afbeeldingen/SP3.png")
    img4 = pygame.image.load("Afbeeldingen/SP4.png")
    greenbar = pygame.image.load("Afbeeldingen/greenbar.png")


    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    font = pygame.font.Font(None, 30)

    def text(msg, pos, size=30):
        black = (0, 0, 0)
        font = pygame.font.Font(None, size)
        label = font.render(msg, True, black)
        screen.blit(label, pos)

    screen.blit(nameInputBack, (0, 0))

    if maxp >= 2:
        playerOne = Player(819, 1007, img1, (ask(screen, "Naam speler 1")))
        playerTwo = Player(900, 1007, img2, (ask(screen, "Naam speler 2")))
    if maxp >= 3:
        playerThree = Player(981, 1007, img3, (ask(screen, "Naam speler 3")))
    if maxp == 4:
        playerFour = Player(1062, 1007, img4, (ask(screen, "Naam speler 4")))

    cp = 1
    winnerfound = False
    mainloop = True
    x = True
    dobbelloop = True
    questionABC = False
    len3 = 0


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
            questionCat = "Sport"
        elif cp == 2:
            questionCat = "Entertainment"
        elif cp == 3:
            questionCat = "History"
        else:
            questionCat = "Geography"

        if cp == 1:
            naam = playerOne.name
        elif cp == 2:
            naam = playerTwo.name
        elif cp == 3:
            naam = playerThree.name
        elif cp == 3:
            naam = playerFour.name


        labelCP = font.render(naam + " is nu aan de beurt.", True, black)
        labelCat = font.render("De categorie is: " + questionCat, True, black)
        labelQw = font.render("Beantwoord de onderstaande vraag correct:", True, black)
        screen.blit(main, (0, 0))
        screen.blit(labelCP, (7, 7))
        screen.blit(labelCat, (7, 30))
        screen.blit(labelQw, (7, 80))


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
            #Mainloop code for input
            k = pygame.key.get_pressed()
            for event in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                if k[pygame.K_ESCAPE]:
                    pass
                #elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 64 and mouse[0] < 188 and mouse[1] > 841 and mouse[1] < 958:
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1539 and mouse[0] < 1776 and mouse[1] > 434 and mouse[1] < 662:
                    if winnerfound == False:
                        keren = [5, 6, 7, 8, 9, 10]
                        dobbelsteenZijde = [background1, background2, background3, background4, background5, background6]
                        aantalKeer = random.choice(keren)
                        for i in range(0, aantalKeer):
                            zijde = random.choice(dobbelsteenZijde)
                            screen.blit(zijde, (0,0))
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
                            screen.blit(labelCP, (7, 7))
                            screen.blit(labelCat, (7, 30))
                            screen.blit(labelQw, (7, 80))
                            pygame.display.update()
                            time.sleep(0.5)
                        cg = diceThrow()
                        if cg == 1:
                            screen.blit(background1, (0, 0))
                        elif cg == 2:
                            screen.blit(background2, (0, 0))
                        else:
                            screen.blit(background3, (0, 0))
                        if cp == 1:
                            randomQuestionID = getQuestion(questionCat)
                            vraag = interact_with_database("SELECT Question FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                            questionList = wrapline(vraag, font, 500)
                            lenq = len(questionList)
                            optie1 = interact_with_database("SELECT awnser1 FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                            optie2 = interact_with_database("SELECT awnser2 FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                            optie3 = interact_with_database("SELECT awnser3 FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
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
                            questionCorrect = interact_with_database("SELECT correct_awnser FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                            questionABC = True
                            dobbelloop = False
                        elif cp == 2:
                            randomQuestionID = getQuestion(questionCat)
                            vraag = interact_with_database("SELECT Question FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                            questionList = wrapline(vraag, font, 500)
                            lenq = len(questionList)
                            optie1 = interact_with_database("SELECT awnser1 FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                            optie2 = interact_with_database("SELECT awnser2 FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                            optie3 = interact_with_database("SELECT awnser3 FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                            if optie3 is not None:
                                optie3list = wrapline(optie3, font, 500)
                                len3 = len(optie3list)
                            else:
                                optie3list = ""
                                len3 = len(optie3list)
                            optie1list = wrapline(optie1, font, 500)
                            optie2list = wrapline(optie2, font, 500)
                            len1 = len(optie2list)
                            len2 = len(optie2list)
                            len3 = len(optie3list)
                            questionCorrect = interact_with_database("SELECT correct_awnser FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                            questionABC = True
                            dobbelloop = False
                        elif cp == 3:
                            randomQuestionID = getQuestion(questionCat)
                            vraag = interact_with_database("SELECT Question FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                            questionList = wrapline(vraag, font, 500)
                            lenq = len(questionList)
                            optie1 = interact_with_database("SELECT awnser1 FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                            optie2 = interact_with_database("SELECT awnser2 FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                            optie3 = interact_with_database("SELECT awnser3 FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                            optie1list = wrapline(optie1, font, 500)
                            optie2list = wrapline(optie2, font, 500)
                            if optie3 is not None:
                                optie3list = wrapline(optie3, font, 500)
                                len3 = len(optie3list)
                            else:
                                optie3list = ""
                                len3 = len(optie3list)
                            len1 = len(optie2list)
                            len2 = len(optie2list)
                            questionCorrect = interact_with_database("SELECT correct_awnser FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                            questionABC = True
                            dobbelloop = False
                        elif cp == 4:
                            randomQuestionID = getQuestion(questionCat)
                            vraag = interact_with_database("SELECT Question FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                            questionList = wrapline(vraag, font, 500)
                            lenq = len(questionList)
                            optie1 = interact_with_database("SELECT awnser1 FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                            optie2 = interact_with_database("SELECT awnser2 FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                            optie3 = interact_with_database("SELECT awnser3 FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                            optie1list = wrapline(optie1, font, 500)
                            optie2list = wrapline(optie2, font, 500)
                            if optie3 is not None:
                                optie3list = wrapline(optie3, font, 500)
                                len3 = len(optie3list)
                            else:
                                optie3list = ""
                                len3 = len(optie3list)
                            len1 = len(optie2list)
                            len2 = len(optie2list)
                            questionCorrect = interact_with_database("SELECT correct_awnser FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
                            questionABC = True
                            dobbelloop = False


        #Start timer
        start_ticks = pygame.time.get_ticks()
        #Check gebruikers antwoord bij MEERKEUZEvraag
        if cg == 1:
            screen.blit(background1, (0, 0))
        elif cg == 2:
            screen.blit(background2, (0, 0))
        elif cg == 3:
            screen.blit(background3, (0, 0))
        screen.blit(labelCP, (7, 7))
        screen.blit(labelCat, (7, 30))
        screen.blit(labelQw, (7, 80))
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
            screen.blit(labelq, (7, 100))
            if lenq > 1:
                labelq = font.render(questionList[1], True, black)
                screen.blit(labelq, (7, 117))
                if lenq > 2:
                    label1 = font.render(questionList[2], True, black)
                    screen.blit(labelq, (7, 134))
        if len1 > 0:
            label1 = font.render(optie1list[0], True, black)
            screen.blit(label1, (7, 380))
            if len1 > 1:
                label1 = font.render(optie1list[1], True, black)
                screen.blit(label1, (7, 397))
                if len1 > 2:
                    label1 = font.render(optie1list[2], True, black)
                    screen.blit(label1, (7, 414))
        if len2 > 0:
            labelOptie2 = font.render(optie2list[0], True, black)
            screen.blit(labelOptie2, (7, 448))
            if len2 > 1:
                labelOptie2 = font.render(optie2list[1], True, black)
                screen.blit(labelOptie2, (7, 465))
                if len2 > 2:
                    labelOptie2 = font.render(optie2list[2], True, black)
                    screen.blit(labelOptie2, (7, 482))
        if len3 > 0:
            labelOptie3 = font.render(optie3list[0], True, black)
            screen.blit(labelOptie3, (7, 522))
            if len3 > 1:
                labelOptie3 = font.render(optie3list[1], True, black)
                screen.blit(labelOptie3, (7, 539))
                if len3 > 2:
                    labelOptie3 = font.render(optie3list[2], True, black)
                    screen.blit(labelOptie3, (7, 556))
        pygame.display.update()


        while questionABC == True:
            seconds = (pygame.time.get_ticks() - start_ticks) / 1000
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 65 and mouse[0] < 190 and mouse[1] > 842 and mouse[1] < 959:
                    print("A")
                    cpKeuze = "A"
                    questionABC = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 211 and mouse[0] < 332 and mouse[1] > 842 and mouse[1] < 959:
                    print("B")
                    cpKeuze = "B"
                    questionABC = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 357 and mouse[0] < 482 and mouse[1] > 842 and mouse[1] < 959:
                    print("C")
                    cpKeuze = "C"
                    questionABC = False
            if seconds > 50:
                cpKeuze = " "
                questionABC = False
            elif seconds <= 50:
                screen.blit(greenbar, (7,320))
                timerLabel = font.render("Timer: "+ str(seconds), True, black)
                screen.blit(timerLabel, (7, 330))
                pygame.display.update()


        if questionCorrect != cpKeuze:
            questionFalse = font.render("Uw keuze was incorrect.", True, red)
            screen.blit(questionFalse, (7, 690))
            pygame.display.update()
            time.sleep(3)
            if cp == 1:
                cp += 1
            elif cp == 2:
                if maxp > 2:
                    cp += 1
                else:
                    cp -= 1
            elif cp == 3:
                if maxp > 3:
                    cp += 1
                else:
                    cp -= 2
            elif cp == 4:
                cp -= 3
        else:
            questionTrue = font.render("Uw keuze was correct.", True, green)
            continueDobbel = font.render("U zult nu bewegen.", True, black)
            screen.blit(questionTrue, (7, 670))
            screen.blit(continueDobbel, (7, 690))
            pygame.display.update()
            time.sleep(3)
            if cp == 1:
                playerOne.update(cg)
                cp += 1
                if playerOne.y < 41:
                    winner = "Player 1"
                    winnerfound = True
            elif cp == 2:
                playerTwo.update(cg)
                if maxp > 2:
                    cp += 1
                else:
                    cp -= 1
                if playerTwo.y < 41:
                    winner = "Player 2"
                    winnerfound = True
            elif cp == 3:
                playerThree.update(cg)
                if maxp > 3:
                    cp += 1
                else:
                    cp -= 2
                if playerThree.y < 41:
                    winnerfound = True
                    winner = "Player 3"
            elif cp == 4:
                playerFour.update(cg)
                cp -= 3
                if playerFour.y < 41:
                    winner = "Player 4"
                    winnerfound = True

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

