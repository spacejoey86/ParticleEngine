from math import sqrt

#Vector3 class from Eris, modified to be a Vector2 class
class Vector2(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

    def __eq__(self, other):
        if not isinstance(other, Vector2):
            return False
        return (self.x == other.x) and (self.y == other.y)

    def __add__(self, other):
        if isinstance(other, Vector2):
            x = self.x + other.x
            y = self.y + other.y
        else:
            x = self.x + other
            y = self.y + other
        return Vector2(x, y)

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, Vector2):
            x = self.x - other.x
            y = self.y - other.y
        else:
            x = self.x - other
            y = self.y - other
        return Vector2(x, y)

    def __rsub__(self, other):
        if isinstance(other, Vector2):
            x = other.x - self.x
            y = other.y - self.y
    def getTuple(self):
        return (self.x, self.y)