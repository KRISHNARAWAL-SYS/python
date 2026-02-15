#create a class "programmer" for storing information of few programmers working at microsoft 

class programmer:
    company = "microsoft"
    
    def __init__(self , name , product):
        self.name = name
        self.product = product
k = programmer("krishna" , "windows")
print(k.name , k.product , k.company)   
r = programmer("rohan" , "linux")
print(r.name , r.product , r.company)