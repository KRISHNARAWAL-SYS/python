# Create a class calculator capable of finding square , cube and square root of a number 
class calculator:
    def __init__(self, n):
        self.n = n
    
    def Sqr(self):
        print(f"the square is {self.n*self.n}")   
     
    def Cube(self):
        print(f"the Cube is {self.n*self.n*self.n}")    
    
    def SqrRoot(self):
        print(f"the squareRoot is {self.n**1/2}")
        
a = calculator(4)
a.Cube()
a.Sqr()
a.SqrRoot()