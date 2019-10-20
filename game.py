import pygame, sys
from pygame.locals import *
import boid as rules

# create boids
class Boid():
    def __init__(self,position,velocity):
        self.position = position # (x, y)
        self.velocity = velocity # (dx, dy)

    def update(self, newPosition, newVelocity):
        self.oldPosition = self.position
        self.oldVelocity = self.velocity
        self.position = newPosition
        self.velocity = newVelocity

        x,y = self.oldPosition
        oldPos = int(x), int(y)

        x,y = self.position
        pos = int(x), int(y)

        pygame.draw.circle(DISPLAYSURF, WHITE, oldPos, 3)
        pygame.draw.circle(DISPLAYSURF, RED, pos, 3)

    def destroy(self):
        pygame.draw.circle(DISPLAYSURF, WHITE, self.position, 3)

pygame.init()
size = width, height = 500,500
DISPLAYSURF = pygame.display.set_mode(size)
pygame.display.set_caption('Commuter Chaos')

DISPLAYSURF.fill((255,255,255))

WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)

mousecounter = 0 # track how many frames it's been since the last mouse click

# create a city layout with block size of 100, spacing of 50
blockSize = 100
spacing = 50
buildings = [(i,j,blockSize,blockSize) for i in range(spacing,width,blockSize+spacing) for j in range(spacing,height,blockSize + spacing)]

# buildings = [(10,10,40,40),(60,10,40,40),(10,60,40,40),(60,60,40,40)]

map = []
for building in buildings:
    map.append(pygame.draw.rect(DISPLAYSURF,BLACK,building))

# create a bunch of boids
# boids = [Boid((100+i*10,100+j*10),(0,0)) for i in range(7) for j in range(7)]
# boids = [Boid((250,250),(0,0)), Boid((250,255),(0,0))]
boids = [Boid((40,25),(0,0)) for i in range(5)]

while True:
    if mousecounter > 0:
        mousecounter -=1
        rules.moveallboids(boids,map,mousepos=mouseposin)
    else:
        rules.moveallboids(boids,map)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONUP:
            mouseposin= list(event.pos)
            rules.moveallboids(boids,buildings,mousepos=mouseposin)
            mousecounter = 15

    pygame.display.update()
    pygame.time.Clock().tick(1)
