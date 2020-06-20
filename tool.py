import pygame
import random
from pygame import surfarray
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((280,280))
run = True
last = None
down = False
color = (255,255,255)
while run:
    pygame.time.delay(100)
    clock = pygame.time.Clock()
    clock.tick(900)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            down = True
        if event.type == pygame.MOUSEMOTION:
            if (down):
                mouse_pos = pygame.mouse.get_pos()
                if last is not None:
                    pygame.draw.aaline(screen, color, mouse_pos, last)
                last = mouse_pos
        if pygame.key.get_pressed()[K_SPACE]:
            screen.fill((0,0,0))
        if pygame.key.get_pressed()[K_KP_ENTER]:
            draw()
        if event.type == pygame.MOUSEBUTTONUP:
            down = False
            last = None
                
        def draw():
            num = surfarray.array2d(screen)
            print(num.shape)
                
    pygame.display.update()
    
pygame.quit()
