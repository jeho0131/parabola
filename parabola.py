import sys
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, MOUSEBUTTONDOWN
import math
import time

pygame.init()
WINDOWSURFACE = pygame.display.set_mode((1000, 500))
FPSCLOCK = pygame.time.Clock()

boom = pygame.image.load("boom.png")
smallboom = pygame.transform.scale(boom,(30,30))

def main():
    dir = 45
    speed = 30
    vox = 0
    voy = 0
    xdis = 0
    ydis = 0
    timer = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    if dir < 90:
                        dir += 5
                elif event.key == K_DOWN:
                    if 0 < dir:
                        dir -= 5
                elif event.key == K_RIGHT:
                    if speed < 70:
                        speed += 1
                elif event.key == K_LEFT:
                    if 20 < speed:
                        speed -= 1

            vox = math.cos(math.pi*dir/180)*speed
            voy = math.sin(math.pi*dir/180)*speed

            if event.type == MOUSEBUTTONDOWN:
                xdis = vox * timer
                ydis = (voy * timer) + (timer * timer * -5)

        print(time.time())

        WINDOWSURFACE.fill((255,255,255))
        WINDOWSURFACE.blit(smallboom,(50,450))
        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__=='__main__':
    main()
