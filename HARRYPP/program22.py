 
 
n = int(input("enter the number of rows :"))

# MY WAY
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print("")               # move to next line
 
 #HARRY WAY
for i in range(1, n+1):
    print("*" * i , end="")   #end="" is used to avoid new line after each print
    print("")               # move to next line
    