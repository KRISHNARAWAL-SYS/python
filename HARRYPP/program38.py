'''
  create a class with a class attribute a ; 
  create an object from it and set'a'
  diectly using object.a = 0 .
  Does this change the class attriute
  '''

class Demo:
    a = 4
    
O = Demo()
print(O.a)
O.a = 0        #instance attribute is set
print(O.a)
#No it doesn't change the class attribute
print(Demo.a)