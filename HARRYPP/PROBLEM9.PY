#WRITE A PROGRAM TO INPUT  5 NUMBERS FROM THE USER AND DISPLAY THE UNIQUES
S = set()

n = int(input("Enter number 1: "))
S.add(int(n))
n = int(input("Enter number 2: "))
S.add(int(n))
n = int(input("Enter number 3: "))
S.add(int(n))
n = int(input("Enter number 4 : "))
S.add(int(n))
n = int(input("Enter number 5: "))
S.add(int(n))

print ("The unique numbers are : ", S)