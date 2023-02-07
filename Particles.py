import pygame
from Vectors import *
class Particle:
    def __init__(self, pos, col, vel):
        self.pos = pos #position
        self.col = col #colour
        # vel has unit pixel/sec 
        self.vel = vel
    def Draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), self.pos.getTuple(), 3)
    def update(self, deltaTime, screenX, screenY):
        # update vel
        force = Vector2(0, 0.5)
        
        self.vel += force * deltaTime * 0.001
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