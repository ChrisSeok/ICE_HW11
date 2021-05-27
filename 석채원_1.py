#1번, B835193 석채원
class Shape:
    def __init__(self, color="yellow", filled=True):
        self.__color = color
        self.__filled = filled
    def __str__(self):
        return f'({self.__color},{self.__filled})'
        #자식클래스에서 부모의 private변수 접근: self._부모클래스__변수명
class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color,filled)
        self.radius = radius
    def area(self):
        return self.radius**2*3.14   
    def __str__(self):
        return super().__str__() + f'(radius = {self.radius})'
        
def main() :
    a = Shape()
    b = Shape("red")
    print(a,b)
    c = Circle("blue",False,10)
    print(c)
    print(c.area())
main()
