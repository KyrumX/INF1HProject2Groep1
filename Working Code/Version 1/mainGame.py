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

def getQuestion():
    questionList = get_questions()
    questionPicked = random.choice(questionList)
    questionID = questionPicked[0]
    return questionID

class Player:
    def __init__(self, x, y, image, player):
        self.x = x
        self.y = y
        self.player = player
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
    main = pygame.image.load("Afbeeldingen/gameboardMain.png")
    img1 = pygame.image.load("Afbeeldingen/SP1.png")
    img2 = pygame.image.load("Afbeeldingen/SP2.png")
    img3 = pygame.image.load("Afbeeldingen/SP3.png")
    img4 = pygame.image.load("Afbeeldingen/SP4.png")


    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    font = pygame.font.Font(None, 30)

    def text(msg, pos, size=30):
        black = (0, 0, 0)
        font = pygame.font.Font(None, size)
        label = font.render(msg, True, black)
        screen.blit(label, pos)

    if maxp >= 2:
        playerOne = Player(819, 1007, img1, 1)
        playerTwo = Player(900, 1007, img2, 2)
    if maxp >= 3:
        playerThree = Player(981, 1007, img3, 3)
    if maxp == 4:
        playerFour = Player(1062, 1007, img4, 4)

    screen.blit(main, (0, 0))
    cp = 1


    winnerfound = False
    mainloop = True
    x = True
    questionAnswered = False

    while mainloop:
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

        labelCP = font.render("Speler " + str(cp) + " is.", True, black)
        labelCat = font.render("De categorie is: " + questionCat, True, black)
        labelQw = font.render("Beantwoord de onderstaande vraag correct:", True, black)
        randomQuestionID = getQuestion()
        vraag = interact_with_database("SELECT Question FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
        labelshowvraag = font.render(vraag, True, black)
        optie1 = interact_with_database("SELECT awnser1 FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
        optie2 = interact_with_database("SELECT awnser2 FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
        optie3 = interact_with_database("SELECT awnser3 FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
        labelOptie1 = font.render(optie1, True, black)
        labelOptie2 = font.render(optie2, True, black)
        labelOptie3 = font.render(optie3, True, black)
        screen.blit(main, (0, 0))
        screen.blit(labelCP, (7, 7))
        screen.blit(labelCat, (7, 30))
        screen.blit(labelQw, (7, 80))
        screen.blit(labelshowvraag, (7, 100))
        screen.blit(labelOptie1, (7, 380))
        screen.blit(labelOptie2, (7, 410))
        screen.blit(labelOptie3, (7, 440))
        dobbelloop = False
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
        questionCorrect = interact_with_database("SELECT correct_awnser FROM QnA WHERE Question_ID = {}".format(randomQuestionID))
        questionABC = True

        #Check gebruikers antwoord bij MEERKEUZEvraag
        while questionABC == True:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                print(mouse)
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




        if questionCorrect != cpKeuze:
            questionFalse = font.render("Uw keuze was incorrect.", True, red)
            screen.blit(questionFalse, (7, 500))
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
            continueDobbel = font.render("U kunt nu de dobbelsteen gooien.", True, black)
            screen.blit(questionTrue, (7, 500))
            screen.blit(continueDobbel, (7, 525))
            pygame.display.update()
            dobbelloop = True



        #Unlock de dobbelsteen
        while dobbelloop == True:
            #Mainloop code for input
            k = pygame.key.get_pressed()
            if k[K_ESCAPE]:
                mainloop = False
            for event in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    mainloop = False
                #elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 64 and mouse[0] < 188 and mouse[1] > 841 and mouse[1] < 958:
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse[0] > 1539 and mouse[0] < 1776 and mouse[1] > 434 and mouse[1] < 662:
                    if winnerfound == False:
                        cg = diceThrow()
                        if cg == 1:
                            screen.blit(background1, (0, 0))
                        elif cg == 2:
                            screen.blit(background2, (0, 0))
                        else:
                            screen.blit(background3, (0, 0))
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
                        dobbelloop = False

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

