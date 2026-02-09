class employee :
    language = "python" # this is a class attribute
    salary = 120000
    
harry  = employee ()
harry.name = "harry hariyala"    # this is an instance attribute
print(harry.name , harry.salary , harry.language)

divyanshu = employee()
divyanshu.name = " divyabhanshu desola"
print(divyanshu.name , divyanshu.salary , divyanshu.language) 

#here name is instance attribute and salary and lang. is 
# class attributes as they directly belong to the class
