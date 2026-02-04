#write a python program using function to convert celsius 
# to Fahrenheit

def CtoF(c):
    
    f = c*(9/5) + 32
    return f

c = int(input("enter temperature in celsius"))
f = CtoF(c)
print(f"{round(f,2)} degree F")
     
    