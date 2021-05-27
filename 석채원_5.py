#5번, B835193 석채원
class CPoint:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def move(self,a,b):
        self.x += a
        self.y += b
        return self
    def __str__(self):
         return f'pos({self.x},{self.y})'
    
class Shape:
    def __init__(self, color="yellow", filled=True, cpoint=None):
        self.__color = color
        self.__filled = filled
        self.cpoint = cpoint
        if(self.cpoint == None):
            self.cpoint = CPoint(0,0)
            #디폴트 인자로 주면 한번만 생성되므로
                
    def move(self, a, b):
        self.cpoint = self.cpoint.move(a,b)
        return self
    
    def __str__(self):
        return self.cpoint.__str__() + f'({self.__color},{self.__filled})'

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color,filled)
        self.radius = radius
    def area(self):
        return self.radius**2*3.14   
    def __str__(self):
        return super().__str__() + f'(radius = {self.radius})'
        
class Rectangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height
    def __str__(self):
        return super().__str__() + f'({self.width},{self.height})'

def main() :
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