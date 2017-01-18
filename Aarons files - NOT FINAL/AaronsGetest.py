"""Copryright 2017, Project 2 Groep 1"""

import pygame
import time
clock = pygame.time.Clock()
maxp = int(input("SELECTEER MAX AANTAL SPELERS"))

class Player:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def update(self):
        self.y -= 50

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), (int(self.x), int(self.y)), int(self.r))



def program():
    width = 1920
    height = 1080
    size = (width, height)

    pygame.init()

    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    font = pygame.font.Font(None, 30)

    playerOne = Player(width * 0.2, height * 0.9, width * 0.1)
    playerTwo = Player(width * 0.4, height * 0.9, width * 0.1)
    playerThree = Player(width * 0.6, height * 0.9, width * 0.1)
    playerFour = Player(width * 0.8, height * 0.9, width * 0.1)
    ant = "1999"
    cp = 1


    mainloop = True
    while mainloop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Give the signal to quit
                mainloop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Spatie")
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
        screen.fill((0, 0, 0))
        playerOne.draw(screen)
        playerTwo.draw(screen)
        playerThree.draw(screen)
        playerFour.draw(screen)
        clock.tick(60)
        pygame.display.flip()


program()