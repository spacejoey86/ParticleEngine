class Particle:
    def __init__(self, pos, col):
        self.pos = pos #position
        self.col = col #colour
    def Draw(self, surface):
        surface.set_at(self.pos.getTuple(), self.col)