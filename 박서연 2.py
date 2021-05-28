#2번문제. C111061 박서연.

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
    c = Rectangle("blue",False,10,20)
    print(c)
    print(c.area())
    
main()