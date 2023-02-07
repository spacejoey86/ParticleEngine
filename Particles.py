class Particle:
    def __init__(self, pos, col, vel):
        self.pos = pos #position
        self.col = col #colour
        # vel has unit pixel/sec 
        self.vel = vel
    def Draw(self, surface):
        surface.set_at(self.pos.getTuple(), self.col)
    def update(self, deltaTime):
        # update vel
        force = Vector2(2, 1.5)
        
        self.vel += force * deltaTime
        # update pos
        self.pos += self.vel * deltaTime