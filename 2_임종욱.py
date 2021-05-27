# 2번 C111152 임종욱

class Shape:
    def __init__(self, color = "yellow", filled = True):
        self.__color = color
        self.__filled = filled 
    def getColor(self):
        return self.__color
    def getFilled(self):
        return self.__filled
    def __str__(self):
        return f'({self.__color},{self.__filled})'

class Rectangle(Shape):
    def __init__(self,color,filled,width,height):
        super().__init__(color,filled)
        self.width = width
        self.height = height
    def area(self):
        Area = self.width * self.height
        return Area
    def __str__(self):
       return f'{Shape.__str__(self)}({self.width},{self.height})'


def main() :
    c = Rectangle("blue",False,10,20)
    print(c)
    print(c.area())

main()
