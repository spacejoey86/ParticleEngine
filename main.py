import sys
import pygame
import random
from Particles import *
from Vectors import *

screenX = 300
screenY = 300
numParticles = 50
particles = []

pygame.init()
surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
(screenX,screenY) = surface.get_size()

#Create the particles
for particleIndex in range(numParticles):
    position = Vector2(random.randint(0, screenX - 1), random.randint(0, screenY - 1))
    particles.append(Particle(position, (255,0,0)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill((0,0,0))
    for particle in particles:
        particle.Draw(surface)

    pygame.display.update()

