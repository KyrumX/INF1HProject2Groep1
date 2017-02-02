import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
import sys

#Timed, voor openvragen:
def get_key2(start_ticks, screen, font, brownbar, white, timer):
    while 1:
        mils = timer - ((pygame.time.get_ticks() - start_ticks) / 1000)
        seconds = int(mils)
        if seconds == -1:
            return K_RETURN
        elif seconds < timer:
            screen.blit(brownbar, (216, 460))
            timerLabel = font.render("Timer: " + str(seconds), True, white)
            screen.blit(timerLabel, (216, 465))
            pygame.display.update()
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key
        else:
            pass

def display_box2(screen, message):
    fontobject = pygame.font.Font(None,30)
    pygame.draw.rect(screen, (74, 110, 134), (37,518,550,30), 0)
    if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (255,255,255)), (39,520))
        pygame.display.flip()

def ask2(screen, question, font, greenbar, black, timer):
    start_ticks = pygame.time.get_ticks()
    pygame.font.init()
    current_string = []
    display_box2(screen, question + ": " + "".join(current_string))
    while 1:
        inkey = get_key2(start_ticks, screen, font, greenbar, black, timer)
        if inkey == K_BACKSPACE:
            current_string = current_string[0:-1]
        elif inkey == K_ESCAPE:
            sys.exit("Esc has been pressed")
        elif inkey == K_RETURN:
            break
        elif inkey == K_MINUS:
            current_string.append("_")
        elif inkey <= 127:
            x = len(current_string)
            if x > 26:
                pass
            else:
                current_string.append(chr(inkey))
        display_box2(screen, question + ": " + "".join(current_string))
    return "".join(current_string)


#Non timed:
def get_key():
    while 1:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key
        else:
            pass

def display_box(screen, message):
    fontobject = pygame.font.Font(None,30)
    pygame.draw.rect(screen, (42, 40, 40), (200, 320,500,30), 0)
    if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (255,255,255)), (200, 320))
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
            sys.exit("Esc has been pressed")
        elif inkey == K_RETURN:
            break
        elif inkey == K_MINUS:
            current_string.append("_")
        elif inkey <= 127:
            x = len(current_string)
            if x > 20:
                pass
            else:
                current_string.append(chr(inkey))
        display_box(screen, question + ": " + "".join(current_string))
    return "".join(current_string)
