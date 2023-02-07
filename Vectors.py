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
        else:
            x = other - self.x
            y = other - self.y
        return Vector2(x, y)

    def __mul__(self, other):
        if isinstance(other, Vector2):
            x = self.x * other.x
            y = self.y * other.y
        else:
            x = self.x * other
            y = self.y * other
        return Vector2(x, y)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, Vector2):
            x = self.x / other.x
            y = self.y / other.y
        else:
            x = self.x / other
            y = self.y / other
            z = self.z / other
        return Vector2(x, y)

    def __rtruediv__(self, other):
        if isinstance(other, Vector2):
            x = other.x / self.x
            y = other.y / self.y
        else:
            x = other / self.x
            y = other / self.y
        return Vector2(x, y)

    def magnitude(self):
        x = self.x**2
        y = self.y**2
        return sqrt(x + y)

    def dot(self, other):
        a = self.x * other.x
        b = self.y * other.y
        return a + b

    def cross(self, other):
        x = (self.y * other.z) - (self.z * other.y)
        y = (self.z * other.x) - (self.x * other.z)
        return Vector2(x, y)

    def unit_vector(self):
        return self / self.magnitude()

    def clamplerp(self, v2, t):
        to = v2 - self
        tval = min(1, max(0, t))
        return self + to * tval

    def getTuple(self):
        return (int(self.x), int(self.y))