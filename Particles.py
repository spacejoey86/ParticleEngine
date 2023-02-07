class Particle:
    def __init__(self, pos, col):
        self.pos = pos
        self.col = col
    def Draw(self, surface):
        surface.set_at(self.pos, self.col)