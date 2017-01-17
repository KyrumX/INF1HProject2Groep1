"""Copryright 2017, Project 2 Groep 1"""

import pygame
import time
c= 0
b = 0
questions = ["a", "b", "c"]
answers = ["a", "b", "c"]
levels = [0, 100, 200]

class Tower:
    def __init__(self):
        self.levels[b]


class Player:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def update(self):
            self.y -= 50

    def makequestion(question, array):
        useranswer = input("{}".format(array[c]))
        if useranswer == array[c]:
            c += 1

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), (int(self.x), int(self.y)), int(self.r))


def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Give the signal to quit
            return True

    return False

def program():
    width = 640
    height = 480
    size = (width, height)

    pygame.init()

    screen = pygame.display.set_mode(size)
    font = pygame.font.Font(None, 30)

    playerOne = Player(width * 0.2, height * 0.9, width * 0.1)
    playerTwo = Player(width * 0.4, height * 0.9, width * 0.1)
    playerThree = Player(width * 0.6, height * 0.9, width * 0.1)
    playerFour = Player(width * 0.8, height * 0.9, width * 0.1)
    ant = "1999"
    cp = 0
    while not process_events():
        print(cp)
        if cp == 0:
            screen.fill((0, 0, 0))
            playerOne.draw(screen)
            playerTwo.draw(screen)
            playerThree.draw(screen)
            playerFour.draw(screen)
            cp = 1
        elif cp == 1:
            #vraagAnt = input("Wat is het jaar waarin Aaron geboren is?")
            #if vraagAnt == ant:
            time.sleep(2)
            playerOne.update()
            screen.fill((0, 0, 0))
            playerOne.draw(screen)
            playerTwo.draw(screen)
            playerThree.draw(screen)
            playerFour.draw(screen)
            cp = 2
        elif cp == 2:
            time.sleep(2)
            playerTwo.update()
            screen.fill((0, 0, 0))
            playerOne.draw(screen)
            playerTwo.draw(screen)
            playerThree.draw(screen)
            playerFour.draw(screen)
            cp = 3
        elif cp == 3:
            time.sleep(2)
            playerThree.update()
            screen.fill((0, 0, 0))
            playerOne.draw(screen)
            playerTwo.draw(screen)
            playerThree.draw(screen)
            playerFour.draw(screen)
            cp = 4
        elif cp == 4:
            time.sleep(2)
            playerFour.update()
            screen.fill((0, 0, 0))
            playerOne.draw(screen)
            playerTwo.draw(screen)
            playerThree.draw(screen)
            playerFour.draw(screen)
            cp = 1
        pygame.display.flip()


program()