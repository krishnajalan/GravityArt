import pygame
import os
from pygame.locals import *
from pygame.math import Vector2
from pygame.draw import *
from random import randint, random
screen = None



class Rocket:
	def __init__(self):
		self.pos = Vector2(randint(0,WINSIZE[0]), randint(0,WINSIZE[1]))
		self.vel = Vector2(0,0)

	def update(self, x, y):
		
		temp = Vector2(x, y)
		acc = temp - self.pos
		acc = acc.normalize()
		acc *= 0.05
		self.vel += acc
		if self.vel.length() > 5:
			self.vel = self.vel.normalize()
			self.vel *= 5
				
		self.pos += self.vel

	def show(self, screen, col):
		circle(screen, col, (int(self.pos.x), int(self.pos.y)), 9)


WINSIZE = 800, 800

def fade(screen):
	s = pygame.Surface((WINSIZE[0],WINSIZE[1]))  # the size of your rect
	s.set_alpha(18)                # alpha level
	s.fill((0,0,0))           # this fills the entire surface
	screen.blit(s, (0,0)) 


def colorFade(c1, base, rev):
    if c1>254 and rev==False:
        rev = True
    
    if rev==False:
        c1+=1
         
    if rev:
        c1-=1
        if c1<base:
            rev = False

    return c1, rev

def main():
    pygame.init()
    scr_inf = pygame.display.Info()
    os.environ['SDL_VIDEO_WINDOW_POS'] = '{}, {}'.format(scr_inf.current_w // 2 - WINSIZE[0] // 2,
                                                         scr_inf.current_h // 2 - WINSIZE[1] // 2)
    screen = pygame.display.set_mode(WINSIZE)
    pygame.display.set_caption('gravity')
    screen.fill((0, 0, 0))
    clock = pygame.time.Clock()
    
    rockets = []
    N = 500
    for i in range(N):
    	rockets.append(Rocket())

    done = 0
    c1 = randint(50,255)
    base = int(c1)
    c2 = randint(50,255)
    c3 = randint(50,255)
    rev = False

    while not done:
    	fade(screen)
    	c1, rev = colorFade(c1, base, rev)
    	x, y = pygame.mouse.get_pos()
    	col = c1, c2, c3
    	for i in range(N):
    		rockets[i].update(x, y)
    		rockets[i].show(screen, col)	
		
    	for e in pygame.event.get():
    		if e.type == QUIT:	
    			done = 1

    	pygame.display.update()
    	clock.tick(60)


main()