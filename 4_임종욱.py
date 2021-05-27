#4번 c111152 임종욱

class CPoint():
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

    def move(self,x,y):
        self.x += x
        self.y += y
        return self
    def __str__(self):
        return f'pos({self.x},{self.y})'

class Shape(CPoint):
    def __init__(self, color = "yellow", filled = True ,x = 0,y = 0):
        super().__init__(x,y)
        self.__color = color
        self.__filled = filled
    def getColor(self):
        return self.__color
    def getFilled(self):
        return self.__filled
    def __str__(self):
        return f'{CPoint.__str__(self)}({self.__color},{self.__filled})'

class Circle(Shape):
    def __init__(self,color,filled,radius):
        super().__init__(color,filled)
        self.radius = radius
    def area(self):
        Area = 3.14*(self.radius)**2
        return Area
    def __str__(self):
       return f'{Shape.__str__(self)}(radius = {self.radius})'
    

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

def main():
    a = Shape()
    b = Shape("red")
    c = Shape("black",False,1,2)
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