import sys
import pygame
from pygame.locals import QUIT, Rect
from math import sin, cos, radians, asin, acos
import time

pygame.init()
WINDOWSURFACE = pygame.display.set_mode((1300, 650))
FPSCLOCK = pygame.time.Clock()

boom = pygame.image.load("boom.png")
smallboom = pygame.transform.scale(boom,(30,30))

def main():
    direction = 0
    speed = 50
    vox = 0
    voy = 0
    xdis = 0
    ydis = 0
    linex = 0
    liney = 0
    boomx = 0
    boomy = 640
    timesave = 0
    timer = 0
    goal = 0
    goal = int(input("목표 지점을 입력하시오 : "))
    direction = asin(goal*9.8/(speed*speed))/2
    rad = radians(direction)
    vox = speed*cos(direction)
    voy = speed*sin(direction)
    timesave = time.time()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        linex = xdis + boomx
        liney = ydis * -1 + 640
        xdis = vox * (time.time() - timesave)
        ydis = voy * (time.time() - timesave) - 9.8 * (time.time() - timesave) * (time.time() - timesave) / 2
        WINDOWSURFACE.fill((255,255,255))
        WINDOWSURFACE.blit(smallboom,(xdis,ydis))
        #pygame.draw.line(WINDOWSURFACE, (255,0,0), (linex, liney), (xdis, ydis * -1 + 640))
        print(xdis, "\t", (ydis))
        pygame.display.update()
        FPSCLOCK.tick(30)
        if ydis < 0:
            break

    WINDOWSURFACE.fill((255,255,255))
    WINDOWSURFACE.blit(smallboom,(boomx,boomy))
    pygame.display.update()
    FPSCLOCK.tick(30)

if __name__=='__main__':
    main()
