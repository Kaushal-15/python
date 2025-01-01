class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius**2

    
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

c = Circle.from_diameter(10)
print("Area of the circle:", c.area())
