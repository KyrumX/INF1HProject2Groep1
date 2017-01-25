import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *

def get_key():
    while 1:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key
        else:
            pass

def display_box(screen, message):
    fontobject = pygame.font.Font(None,30)
    pygame.draw.rect(screen, (0, 0, 0), (298,158,500,30), 0)
    pygame.draw.rect(screen, (0, 0, 0), (296,156,504,32), 1)
    if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (255,255,255)), (300,160))
        pygame.display.flip()

def ask(screen, question):
    pygame.font.init()
    current_string = []
    display_box(screen, question + ": " + "".join(current_string))
    while 1:
        inkey = get_key()
        if inkey == K_BACKSPACE:
            current_string = current_string[0:-1]
        elif inkey == K_ESCAPE:
            pygame.quit()
        elif inkey == K_RETURN:
            break
        elif inkey == K_MINUS:
            current_string.append("_")
        elif inkey <= 127:
            current_string.append(chr(inkey))
        display_box(screen, question + ": " + "".join(current_string))
    return "".join(current_string)

def main():
    background = pygame.image.load('Afbeeldingen/gameboard2.png')
    background = pygame.transform.scale(background, (1920, 1080))
    resolution = (1920,1080)
    screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
    screen.blit(background, (0, 0))

    k = pygame.key.get_pressed()

main()