class employee :
    language = "python" # this is a class attribute
    salary = 120000
    
    
        
    
harry = employee ()
harry.language = "C++"    # instance attribute has precedance over class attribute
print(  harry.salary , harry.language)