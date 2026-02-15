class employee:
    salary = 100000
    language = "python"
    
    def __init__(self):  # this is a constructor , also called dunder method which is automatically called when we create an object of a class
        print("employee created")
        
krishna = employee()
krishna.name = "krishna "
print(krishna.name , krishna.salary)
      