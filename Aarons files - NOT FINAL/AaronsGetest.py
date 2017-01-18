"""Copryright 2017, Project 2 Groep 1"""

import pygame
import time
clock = pygame.time.Clock()
maxp = int(input("SELECTEER MAX AANTAL SPELERS"))

class Player:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def update(self):
        self.y -= 50

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))



def program():
    width = 1920
    height = 1080
    size = (width, height)
    background = pygame.image.load("Afbeeldingen/menuscreen.png")
    img1 = pygame.image.load("Afbeeldingen/SP1.png")
    img2 = pygame.image.load("Afbeeldingen/SP2.png")
    img3 = pygame.image.load("Afbeeldingen/SP3.png")
    img4 = pygame.image.load("Afbeeldingen/SP4.png")

    pygame.init()

    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    font = pygame.font.Font(None, 30)

    playerOne = Player(width * 0.2, 900, img1)
    playerTwo = Player(width * 0.4, 900, img2)
    playerThree = Player(width * 0.6, 900, img3)
    playerFour = Player(width * 0.8, 900, img4)
    ant = "1999"
    cp = 1


    mainloop = True
    while mainloop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("Spatie")
                # playerAnt = input("Antwoord")
                # if playerAnt == ant:
                if cp == 1:
                    playerOne.update()
                    cp += 1
                elif cp == 2:
                    playerTwo.update()
                    if maxp > 2:
                        cp += 1
                    else:
                        cp -= 1
                elif cp == 3:
                    playerThree.update()
                    if maxp > 3:
                        cp += 1
                    else:
                        cp -= 2
                elif cp == 4:
                    playerFour.update()
                    cp -= 3
        print(cp)
        screen.blit(background, (0,0))
        playerOne.draw(screen)
        playerTwo.draw(screen)
        playerThree.draw(screen)
        playerFour.draw(screen)
        clock.tick(60)
        pygame.display.flip()


program()