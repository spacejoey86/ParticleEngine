import sys
import pygame
import random
from Particles import *
from Vectors import *

screenX = 300
screenY = 300
numParticles = 200
particles = []
time = 0

#Set up the array
numTypes = 3
forceMulArray = [[0.3, 0.5, -0.2],
                 [-0.8, 0, -0.4],
                 [-0.1, 0.3, 0.8]]

pygame.init()
surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
(screenX,screenY) = surface.get_size()

#Create the particles
for i in range(numParticles):
    position = Vector2(random.randint(0, screenX - 1), random.randint(0, screenY - 1))
    velocity = Vector2(random.uniform(-20, 20), random.uniform(-20, 20))
    particles.append(Particle(position, random.randint(0,2), velocity))

while True:
    #handle the close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #refreshes the games ticks
    tempTime = time  
    time = pygame.time.get_ticks()
    deltaTime = time - tempTime

    #drawing and updating physics
    surface.fill((0,0,0))
    for particle in particles:
        particle.resetForce()
        for particle2 in particles:
            if particle == particle2:
                continue
            else:
                force = forceMulArray[particle.typ][particle2.typ]
                denom = ((particle.pos - particle2.pos).square())
                if not (denom == 0 or force == 0):
                    particle.addForce(1 / denom)

        particle.update(deltaTime, screenX, screenY)
        particle.Draw(surface)

    pygame.display.update()

