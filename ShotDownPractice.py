import sys
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, MOUSEBUTTONDOWN
import math
import time

pygame.init()
WINDOWSURFACE = pygame.display.set_mode((1300, 650))
FPSCLOCK = pygame.time.Clock()

boom = pygame.image.load("boom.png")
smallboom = pygame.transform.scale(boom,(30,30))

def main():
    direction = 0
    speed = 100
    vox = 0
    voy = 0
    xdis = 0
    ydis = 0
    linex = 0
    liney = 0
    boomx = 0
    boomy = 620
    timesave = 0
    timer = 0
    goal

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            goal = int(input("목표 지점을 입력하시오"))
            
            vox = math.cos(math.pi*direction/180)*speed
            voy = math.sin(math.pi*direction/180)*speed
            
            timesave = time.time()
            while True:
                linex = xdis + boomx
                liney = ydis * -1 + 640
                xdis = vox * timer
                ydis = (voy * timer) + (timer * timer * -4.9)
                WINDOWSURFACE.fill((255,255,255))
                WINDOWSURFACE.blit(smallboom,(xdis + boomx,ydis * -1 + boomy))
                timer = time.time() - timesave
                #pygame.draw.line(WINDOWSURFACE, (255,0,0), (linex, liney), (xdis, ydis * -1 + 640))
                #print(xdis + 20, "\t", (ydis + 450))
                pygame.display.update()
                FPSCLOCK.tick(30)
                if ydis < 0:
                    boomx = xdis + boomx
                    boomy = ydis * -1 + boomy
                    break

        WINDOWSURFACE.fill((255,255,255))
        WINDOWSURFACE.blit(smallboom,(boomx,boomy))
        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__=='__main__':
    main()
