#write a program to print multipication table of any given numberr

#              MY WAY 
# num = int(input("enter the number :"))

# for num in range(1 , num*11 , num):
#     print(num)
  
  
#              HARRY WAY

num = int(input("enter the number :"))

for i in range (1,11):
    print(f"{num} x {i} = {num*i}")
    