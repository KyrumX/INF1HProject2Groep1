"""Copryright 2017, Project 2 Groep 1"""

import pygame

b = 0
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
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.y -= 1
        else:
            self.x += 0

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

    playerOne = Player(width * 0.2, height * 0.5, width * 0.1)
    playerTwo = Player(width * 0.8, height * 0.5, width * 0.1)





program()
