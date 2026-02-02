''' 
    for n = 3
        *
       ***
      *****

'''
n = int(input("enter the number of rows :"))

for i in range(1, n+1):
    # print spaces
    for j in range(n-i):         # print n-i spaces in ith row
        print(" ", end="")
    # print stars
    for k in range(2*i - 1):      # print 2*i-1 stars in ith row
        print("*", end="")
    print("")               # move to next line
    
    

