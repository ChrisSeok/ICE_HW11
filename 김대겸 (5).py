#5번_B735042_김대겸

class CPoint: 
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def move(self, dx, dy):
        rx = self.x + dx
        ry = self.y + dy
        return CPoint(rx, ry)
    def __str__(self):
        return f'pos({self.x},{self.y})'

class Shape():
    def __init__(self, color='yellow', filled=True, x=0, y=0):
        self.__color = color
        self.__filled = filled
        self.x = x
        self.y = y

    def move(self, dx, dy):
        rx = self.x + dx
        ry = self.y + dy

    def __str__(self):
        return f'pos({self.x},{self.y})({self.__color},{self.__filled})'

class Circle(Shape):
    def __init__(self, color='yellow', filled=True, radius=0):
        super().__init__(color, filled)            
        self.radius = radius
    def area(self):
        return ((self.radius**2) * 3.14)
    def __str__(self):
        return f'{super().__str__()}(radius = {self.radius})'

class Rectangle(Shape):
    def __init__(self, color='yellow', filled=True, width=0, height=0):
        super().__init__(color, filled)
        self.width = width
        self.height = height
    def area(self):
        return (self.width * self.height)
    def __str__(self):
        return f'{super().__str__()}({self.width},{self.height})'    


def main():
    a = Shape()
    b = Shape("red")
    cpoint = CPoint(4,7)
    c = Shape("black",False,cpoint)
    print(a)
    print(b)
    print(c)
    a.move(2,3)
    print(a)
    print(b.move(4,5))
    d = Circle("blue",False,10).move(3,4)
    print(d)
    e = Rectangle("blue",False,10,20)
    print(e.move(7,8))

main()