# write a program to find greatest of three numbers using functions

def GrtOfThree( x ,  y ,  z):
    if ( x>y and x>z):
        return x
    elif( y>x and y>z):
        return y
    else:
        return z

a = 5
b = 9
c = 2

print(GrtOfThree(a , b ,c ))
    

