#1번_B735042_김대겸

class Shape:
    def __init__(self, color='yellow', filled=True):
        self.__color = color
        self.__filled = filled 
    def __str__(self):
        return f'({self.__color},{self.__filled})'

class Circle(Shape):
    def __init__(self, color='yellow', filled=True, radius=0):
        super().__init__(color, filled)            
        self.radius = radius  
    def area(self):
        return ((self.radius**2) * 3.14)
    def __str__(self):
        return f'{super().__str__()}(radius = {self.radius})'

def main():
    a = Shape()
    b = Shape("red")
    print(a,b)
    c = Circle("blue",False,10)
    print(c)
    print(c.area())

main()
    