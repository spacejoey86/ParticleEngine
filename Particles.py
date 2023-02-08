import pygame
from Vectors import *
class Particle:
    forceMulArray = [[0.3, 0.5, -0.2],
                 [-0.8, 0, -0.4],
                 [-0.1, 0.3, 0.8]]
    def __init__(self, pos, typ, vel):
        self.pos = pos #position
        self.typ = typ #colour
        self.col = (255, 255, 255)
        # vel has unit pixel/sec 
        self.vel = vel
        self.force = Vector2(0,0)
    def Draw(self, surface):
        pygame.draw.circle(surface, self.col, self.pos.getTuple(), 1)
    def update(self, deltaTime, screenX, screenY):
        # update vel
        acceleration = self.force * 1
        self.vel += acceleration * deltaTime * 0.001
        # update pos
        self.pos += self.vel * deltaTime * 0.001
        if (self.pos.x > screenX or self.pos.x < 0) or (self.pos.y > screenY or self.pos.y < 0):
            if (self.pos.x > screenX):
                self.pos.x -= screenX
            elif (self.pos.x < 0):
                self.pos.x += screenX
            elif (self.pos.y > screenY):
                self.pos.y -= screenY
            else:
                self.pos.y += screenY
    def resetForce(self):
        self.force = Vector2(0,0)
    def addForce(self, force):
        self.force += force

    #gets the force and individual particle puts on another
    def getForce(particle1, particle2):
        # force = forceMultiplier / radius^2
        force = particle1.getForceMultiplier(particle2) / (particle1.pos.distance(particle2.pos) ** 2)
        # in the direction of the other particle
        # get the unit vector
        direction = (particle2.pos - particle1.pos).unit_vector()

        return direction * force
    def getForceMultiplier(particle1, particle2):
        return Particle.forceMulArray[particle1.typ][particle2.typ]
