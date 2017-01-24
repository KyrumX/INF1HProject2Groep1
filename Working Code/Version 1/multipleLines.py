from itertools import chain
import pygame

clock = pygame.time.Clock()
def truncline(text, font, maxwidth):
        real=len(text)       
        stext=text           
        l=font.size(text)[0]
        cut=0
        a=0                  
        done=1
        old = None
        while l > maxwidth:
            a=a+1
            n=text.rsplit(None, a)[0]
            if stext == n:
                cut += 1
                stext= n[:-cut]
            else:
                stext = n
            l=font.size(stext)[0]
            real=len(stext)               
            done=0                        
        return real, done, stext             
        
def wrapline(text, font, maxwidth): 
    done=0                      
    wrapped=[]                  
                               
    while not done:             
        nl, done, stext=truncline(text, font, maxwidth) 
        wrapped.append(stext.strip())                  
        text=text[nl:]                                 
    return wrapped
 
 
def wrap_multi_line(text, font, maxwidth):
    """ returns text taking new lines into account.
    """
    lines = chain(*(wrapline(line, font, maxwidth) for line in text.splitlines()))
    return list(lines)

# while True:
#     pygame.init()
#
#     clock.tick(5)
#     font=pygame.font.Font(None, 17)
#     black = (0, 0, 0)
#     red = (255, 0, 0)
#     green = (0, 255, 0)
#     width = 1920
#     height = 1080
#     size = (width, height)
#     x = wrapline("Now is the time for all good men to come to the aid of their country", font, 120)
#     screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
#     lenx = len(x)
#     y = 50
#     print(lenx)
#     print(x[0])
#     print(x[1])
#     print(x[2])
#     print(x[3])
#     if lenx > 0:
#         labelCP = font.render(x[0], True, red)
#         screen.blit(labelCP, (7, 7))
#         pygame.display.update()
#         if lenx > 1:
#                 labelCP = font.render(x[1], True, red)
#                 screen.blit(labelCP, (7, 25))
#                 pygame.display.update()
#                 if lenx > 2:
#                         labelCP = font.render(x[2], True, red)
#                         screen.blit(labelCP, (7, 42))
#                         pygame.display.update()
