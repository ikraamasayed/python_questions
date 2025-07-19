class myclass:
    a = "this is the class variable"

    def __init__(self,len):
        self.lenght = len

    @classmethod
    def class_method(cls):
        print("thsi is class method")
        print(f"using the class variable '{cls.a}' ")

myclass.class_method()


class Calculator:
    @staticmethod
    def add(x,y):
        return x+y
    
    @staticmethod
    def subtract(x,y):
        return x-y 
    
    @staticmethod
    def multiply(x,y):
        return x*y
    