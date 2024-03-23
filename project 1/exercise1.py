class polygon:
    import math

    def __init__(self, edge, circumradius):
        self.edge = edge
        self.vertices = edge
        self.circumradius = circumradius

    def InteriorAngle(self):
        self.InteriorAngle = (self.edge - 2) * (180/self.edge)
        return self.InteriorAngle

    def edgelength(self):
        self.edgelength = 2 * self.circumradius * math.sin(math.pi/self.edge)
        return self.edgelength

    def apothem(self):
        self.apothem = self.circumradius * math.cos(math.pi/self.edge)
        return self.apothem

    def area(self):
        self.area = self.vertices * self.edgelength() * self.apothem
        return self.area

    def perimeter(self):
        self.perimeter = self.edge * self.edgelength()
        return self.perimeter

    def __repr__(self):
        return f"Polygon(edge={self.edge}, circumradius = {self.circumradius}"

    def __eq__(self, other):
        if self.edge == other.edge and self.circumradius == other.circumradius:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.edge > other.edge and self.circumradius > other.circumradius:
            return True
        else:
            return False



from collections import namedtuple

s_polygon = namedtuple("s_polygon", 'edge, circumradius')

p1 = s_polygon(5,6)
print(p1)

#how do I make a tuple take in sequence of data