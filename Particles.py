import pygame
from Vectors import *
class Particle:
    acceleration = Vector2(0,0)
    def __init__(self, pos, typ, vel):
        self.pos = pos #position
        self.typ = typ #colour
        self.col = (255, 255, 255)
        # vel has unit pixel/sec 
        self.vel = vel
    def Draw(self, surface):
        pygame.draw.circle(surface, self.col, self.pos.getTuple(), 1)
    def update(self, deltaTime, screenX, screenY):
        # update vel
        
        self.vel += self.force * deltaTime * 0.001
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