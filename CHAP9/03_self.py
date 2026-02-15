class employee :
    language = "python" # this is a class attribute
    salary = 120000
  # self refers to a insance of a class. ti is automatically passed with a function call
  # from an object   
    def getinfo(self):
        print(f"The language is {self.language}.the salary is {self.salary}")
    def greet():
        print("good moring!!")   
    
harry = employee ()
harry.language = "C++"    # instance attribute has precedance over class attribute
print(  harry.salary , harry.language)

harry.getinfo() # same call with Employee.getinfo(harry)
harry.greet()   # no argument is given thats why we give self as a argument