class employee:
    salary = 100000
    language = "python"
    
    def __init__(self , name , salary , language):# this is a constructor , also called dunder method which is automatically called when we create an object of a class
        self.name = name
        self.salary = salary
        self.language = language
        print("employee created")
        
krishna = employee( "krishna" , 1200000 , "javascript")
#krishna.name = "krishna "
print(krishna.name , krishna.salary , krishna.language)
      