class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Point(self.x + other.x , self.y + other.y)
    
    def __sub__(self,other):
        return Point(self.x + other.x,self.y+other.y)
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
fist= Point(10,13)
scnd = Point(20,17)

result = fist + scnd
print(result)