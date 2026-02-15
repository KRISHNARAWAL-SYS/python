class employee :
    language = "python" # this is a class attribute
    salary = 120000
 
    def getinfo(self):
        print(f"The language is {self.language}.the salary is {self.salary}")
    @staticmethod   #this means function didnt need any object like self
    def greet():
        print("good moring!!")   
    
harry = employee ()
harry.language = "C++"    # instance attribute has precedance over class attribute
print(  harry.salary , harry.language)

harry.getinfo() # same call with Employee.getinfo(harry)
harry.greet()   # no argument is given thats why we give self as a argument