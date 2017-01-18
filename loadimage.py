import pygame

img = pygame.image.load('SP1.png')

black = (0, 0, 0)
width = 640
heigth = 480
size = (width, heigth)
screen = pygame.display.set_mode(size)
screen.fill((black))
running = 1

class Sprite(object):
    def __init__(self):
        self.image = img
        self.x = 0
        self.y = 0

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= 1
        elif keys[pygame.K_RIGHT]:
            self.x += 1
        if keys[pygame.K_UP]:
            self.y -= 1
        elif keys[pygame.K_DOWN]:
            self.y += 1

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

sprite = Sprite()

while True:
    screen.fill((black))
    screen.blit(img,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    sprite.draw(screen)
    sprite.handle_keys()
    pygame.display.flip()



