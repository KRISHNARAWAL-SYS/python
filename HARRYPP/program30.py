def pattern(n):
     if(n==0):
         return
     print("*" * n)
     pattern(n-1)        # recursive call
                          # using of function inside itself is called recursion
        
     
        
n = int(input("enter the number of rows :"))
pattern(n)