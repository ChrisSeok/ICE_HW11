#5번문제. C111061 박서연.

class CPoint:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def move(self, a, b):
        self.x += a
        self.y += b
        return self
    
    def __str__(self):
        return f'pos({self.x},{self.y})'

class Shape:
    def __init__(self, color = 'yellow', filled = True, cpoint = None):
        if cpoint is None:
            cpoint = CPoint()
        self.cpoint = cpoint
        self.__color = color
        self.__filled = filled
        
    def setColor(self, color):
        self.__color = color
    def setFilled(self, filled):
        self.__filled = filled
    def getColor(self):
        return self.__color
    def getFilled(self):
        return self.__filled
    
    def move(self, x, y):
        self.cpoint.move(x,y)
        return self
    
    def __str__(self):
        return f'{self.cpoint}({self.__color},{self.__filled})'

    
class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.__radius = radius
    
    def setRadius(self, radius):
        self.__radius = radius
    def getRadius(self):
        return self.__radius
    
    def area(self):
       return 3.14*(self.__radius**2)
    
    def __str__(self):
        return super().__str__() + f'(radius = {self.__radius})'
    
class Rectangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.__width = width
        self.__height = height
        
    def setWidth(self, width):
        self.__width = width
    def setHeight(self, height):
        self.__height = height
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height
    
    def area(self):
        return self.__width*self.__height
    
    def __str__(self):
        return super().__str__() + f'({self.__width},{self.__height})'

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
