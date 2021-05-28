#1번문제. C111061 박서연.

class Shape:
    def __init__(self, color = 'yellow', filled = True):
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
        
    def __str__(self):
        return f'({self.__color},{self.__filled})'
    

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
    
    
def main():
    a = Shape()
    b = Shape("red")
    print(a,b)
    c = Circle("blue",False,10)
    print(c)
    print(c.area())
    
main()
