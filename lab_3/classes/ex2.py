<<<<<<< HEAD
class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print(self.length * self.length)


length = int(input())
area = Square(length)
print(area.area())
=======
class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print(self.length * self.length)


length = int(input())
area = Square(length)
print(area.area())
>>>>>>> 6f223fbdd8a9d8ba6add15e8f64c252c8b468477
