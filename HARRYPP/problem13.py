math = int(input("enter marks of maths :"))
GS = int(input("enter marks of GS :"))
SS = int(input("enter marks of SS :"))

if(math > 33 and GS > 33 and SS > 33 ):
    print(" passed in each subject")
else:
    print(" not passed in each subject ")
    
TOTAL_percentage = ((math + GS + SS)/300 ) * 100

if(TOTAL_percentage > 40):
    print(" PASSED ")
else:
    print("failed")   








