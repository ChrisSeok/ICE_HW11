#3번 c111152 임종욱

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

def main() :
    p = CPoint()
    q = CPoint(3,4)
    print(p,q)
    print(q.move(-4,5))
    print(p.move(5,6).move(2,3))

main()