import sys
import pygame
import random
from Particles import *
from Vectors import *

screenX = 300
screenY = 300
numParticles = 50
particles = []
time = 0

pygame.init()
surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
(screenX,screenY) = surface.get_size()

#Create the particles
for i in range(numParticles):
    position = Vector2(random.randint(0, screenX - 1), random.randint(0, screenY - 1))
    velocity = Vector2(random.uniform(-5, 5), random.uniform(-5, 5))
    particles.append(Particle(position, (255,255,255), velocity))

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
        particle.update(deltaTime, screenX, screenY)
        particle.Draw(surface)

    pygame.display.update()

