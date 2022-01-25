import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * math.pi

    def perimeter(self):
        return self.radius * 2 * math.pi


circle1 = Circle(radius=1)
print(f"{circle1.area():.2f}")
print(f"{circle1.perimeter():.2f}")

circle1 = Circle(radius=3)
print(f"{circle1.area():.2f}")
print(f"{circle1.perimeter():.2f}")
