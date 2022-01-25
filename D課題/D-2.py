import math


class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def diagonal(self):
        return math.sqrt(self.height ** 2 + self.width ** 2)


rectangle1 = Rectangle(5, 6)
print(f"{rectangle1.area():.2f}")
print(f"{rectangle1.diagonal():.2f}")

rectangle2 = Rectangle(3, 3)
print(f"{rectangle2.area():.2f}")
print(f"{rectangle2.diagonal():.2f}")
