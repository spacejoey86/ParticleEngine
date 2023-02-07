import sys
import pygame
import random
import Particles

screenX = 300
screenY = 300
numParticles = 50
particles = []

pygame.init()
surface = pygame.display.set_mode((screenX, screenY))

#Create the particles
for particleIndex in range(numParticles):
    particles.append(Particles.Particle((random.randint(0, screenX - 1), random.randint(0, screenY - 1)), (255,0,0)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill((0,0,0))
    for particle in particles:
        particle.Draw(surface)

    pygame.display.update()

