import math


class Square:

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def diagonal(self):
        return math.sqrt(2) * self.side


square1 = Square(1.5)
print(f"{square1.area():.2f}")
print(f"{square1.diagonal():.2f}")

square2 = Square(15)
print(f"{square2.area():.2f}")
print(f"{square2.diagonal():.2f}")
