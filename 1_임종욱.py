#1번 C111152 임종욱

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

class Circle(Shape):
    def __init__(self,color,filled,radius):
        super().__init__(color,filled)
        self.radius = radius
    def area(self):
        Area = 3.14*(self.radius)**2
        return Area
    def __str__(self):
       return f'{Shape.__str__(self)}(radius = {self.radius})'

def main() :
    a = Shape()
    b = Shape("red")
    print(a,b)
    c = Circle("blue",False,10)
    print(c)
    print(c.area())

main()
