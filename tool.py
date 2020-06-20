import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((280,280))
run = True
last = None
down = False
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            down = True
        if event.type == pygame.MOUSEMOTION:
            if (down):
                mouse_pos = pygame.mouse.get_pos()
                if last is not None:
                    pygame.draw.line(screen, (255,255,255), last, mouse_pos)
                last = mouse_pos
        if event.type == pygame.KEYDOWN:
            if pygame.key == pygame.K_SPACE:
                print("Space")
        if event.type == pygame.MOUSEBUTTONUP:
            down = False
            last = None
                
        def draw():
            pygame.draw.line()
                
    pygame.display.update()
    
pygame.quit()
