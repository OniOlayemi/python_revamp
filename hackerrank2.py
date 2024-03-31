import math

class rectangle:
    def __init__(self, x, y):
        self.length1 = x
        self.length2 = y

    @property
    def area(self):
        print(self.length1 * self.length2)
        return self.length1 * self.length2


re = rectangle(2,2)
re.area


class circle:

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        print(math.pi * self.radius**2)
        return(math.pi * self.radius**2)

c = circle(3)
c.area