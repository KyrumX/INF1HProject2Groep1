import textbox
import pygame
pygame.init()

# Create TextInput-object
def textinput():
    textinput = textbox.TextInput()

    screen = pygame.display.set_mode((1000, 200))
    clock = pygame.time.Clock()

    loop = True
    while loop:
        screen.fill((225, 225, 225))

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        # Blit its surface onto the screen
        screen.blit(textinput.get_surface(), (10, 10))

        pygame.display.update()
        clock.tick(30)


        if textinput.update(events):
            loop = False

    return(textinput.get_text())
