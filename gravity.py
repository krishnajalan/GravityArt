import pygame
import os
from pygame.locals import *
from pygame.math import Vector2
from pygame.draw import *
from random import randint, random
from math import e,sin,pi,cos

WINSIZE = 1280,720
DEFACC = 0.025
FORCE = 0.025

class Rocket:
    def __init__(self):
        self.pos = Vector2(randint(0,WINSIZE[0]), randint(0,WINSIZE[1]))
        self.vel = Vector2(0,0)

    def update(self, x, y):
        
        temp = Vector2(x, y)
        acc = temp - self.pos
        acc = acc.normalize()
        acc *= FORCE
        self.vel += acc
        if self.vel.length() > 5:
            self.vel = self.vel.normalize()
            self.vel *= 5
                
        self.pos += self.vel

    def show(self, screen, col):
        circle(screen, col, (int(self.pos.x), int(self.pos.y)), 9)



def fade(screen):
    s = pygame.Surface((WINSIZE[0],WINSIZE[1]))  # the size of your rect
    s.set_alpha(18)                # alpha level
    s.fill((0,0,0))           # this fills the entire surface
    screen.blit(s, (0,0)) 


def colorFade(x, rgb):

    N = x/1000
    
    if rgb == "r" :
        x = 255 * abs(sin(N*pi)) 
    elif rgb == "g" :
        x = 255 * abs(sin(N*pi+ pi/3)) 
    elif rgb == "b" :
        x = 255 * abs(sin(N*pi+2*pi/3)) 

    return int(x)

def main():
    global FORCE
    global DEFACC
    pygame.init()
    scr_inf = pygame.display.Info()
    os.environ['SDL_VIDEO_WINDOW_POS'] = '{}, {}'.format(scr_inf.current_w // 2 - WINSIZE[0] // 2,
                                                         scr_inf.current_h // 2 - WINSIZE[1] // 2)
    screen = pygame.display.set_mode(WINSIZE)
    pygame.display.set_caption('gravity')
    screen.fill((0, 0, 0))
    clock = pygame.time.Clock()
    
    rockets = []
    N = 1000
    for i in range(N):
        rockets.append(Rocket())

    done = 0
    c1 = randint(50,255)
    base = int(c1)
    c2 = randint(50,255)
    c3 = randint(50,255)
    rev = False
    X = 0
    while not done:

        if pygame.mouse.get_pressed()[0] :
            FORCE += 0.01
        elif pygame.mouse.get_pressed()[2] :
            FORCE -= 0.01
        elif pygame.mouse.get_pressed()[1]:
            FORCE = DEFACC

        fade(screen)
        c1 = colorFade(X,"r")
        c3 = colorFade(X,"b")
        c2 = colorFade(X,"g")
        x, y = pygame.mouse.get_pos()
        col = c1, c2, c3
        print(col,X)
        for i in range(N):
            rockets[i].update(x, y)
            rockets[i].show(screen, col)    
        
        for e in pygame.event.get():
            if e.type == QUIT:  
                done = 1

        pygame.display.update()
        clock.tick(60)
        X += 1
        X %= 1000


main()