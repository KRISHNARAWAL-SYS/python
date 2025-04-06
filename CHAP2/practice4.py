a = int(input("enter first no."))
b = int(input("enter second no."))
c = int(input("enter third no."))

if(a > b):
    if(a > c):
        print("a is the greatest")
    else:
        print("c is the greatest")
elif(c > b):
    print("c is the greatest")
else:
    print(" b is greatest")               