import sys
import pygame
import random

screenX = 300
screenY = 300
numParticles = 50
particles = []

class Particle:
    def __init__(self, pos, col):
        self.pos = pos
        self.col = col
    def Draw(self, surface):
        surface.set_at(self.pos, self.col)

pygame.init()
surface = pygame.display.set_mode((screenX, screenY))

#Create the particles
for particleIndex in range(numParticles):
    particles.append(Particle((random.randint(0, screenX - 1), random.randint(0, screenY - 1)), (255,0,0)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill((0,0,0))
    for particle in particles:
        particle.Draw(surface)

    pygame.display.update()

