import pygame, sys
from pygame.locals import *

pygame.init()
size = width, height = 500,500
DISPLAYSURF = pygame.display.set_mode(size)
pygame.display.set_caption('Commuter Chaos')

DISPLAYSURF.fill((255,255,255))

# create a city layout
buildings = [(i,j,100,100) for i in range(50,width,150) for j in range(50,height,150)]

# buildings = [(10,10,40,40),(60,10,40,40),(10,60,40,40),(60,60,40,40)]
for building in buildings:
    pygame.draw.rect(DISPLAYSURF,(0,0,0),building)

# create boids
class Boid():
    def __init__(self,position,velocity):
        self.position = position
        self.velocity = velocity

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
