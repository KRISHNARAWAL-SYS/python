#Q1.  write a program to find greatest of four number

a = int(input("enter your number:"))
b = int(input("enter your number:"))
c = int(input("enter your number:"))
d = int(input("enter your number:"))

if(a>b and a>c and a>d):
    print("a is greatest")    
elif(b>a and b>c and b>d):
    print("b is greatest")    
elif(c>a and c>b and c>d):
    print("c is greatest")        
elif(d>a and d>b and d>c):
    print("d is greatest")    
    
    