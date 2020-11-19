import sys
import time
from math import sin, cos, radians, asin, acos
import pygame
from pygame.locals import QUIT,Rect

pygame.init()
w = 600
h = 600
SURFACE = pygame.display.set_mode((w, h))
FPSCLOCK = pygame.time.Clock()
boom = pygame.image.load("boom.png")
smallboom = pygame.transform.scale(boom,(30,30))
x_t = int(input("적의 위치는? : "))
v0 = int(input("대포의 초기값은? : "))

def main():
    t = time.time()
    sinValue = x_t*9.8/(v0*v0)

    SURFACE.fill((255,255,255))

    if(sinValue <= 1.0):
        theta1 = asin(x_t*9.8/(v0*v0))/2
        theta2 = 3.14/2 - asin(x_t*9.8/(v0*v0))/2

        rad1 = radians(theta1)
        v0_x1 = v0*cos(theta1)
        v0_y1 = v0*sin(theta1)

        rad2 = radians(theta2)
        v0_x2 = v0*cos(theta2)
        v0_y2 = v0*sin(theta2)

        xpoint1 = 0
        ypoint1 = 0
        xpoint2 = 0
        ypoint2 = 0

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if ypoint1 >= 0:
                #old_xpoint1 = xpoint1
                #old_ypoint1 = ypoint1
                xpoint1 = v0_x1*(time.time() - t)
                ypoint1 = v0_x1*(time.time() - t) - 9.8*(time.time() - t)* (time.time() - t)/2
                SURFACE.fill((255,255,255))
                SURFACE.blit(smallboom,(xpoint1, 500-ypoint1))
                print(xpoint1, 500-ypoint1)

        pygame.display.update()
        FPSCLOCK.tick(50)

if __name__ == '__main__':
    main()
