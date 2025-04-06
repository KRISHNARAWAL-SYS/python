#conditional statement
age = int(input("enter age :"))


if (age >= 18):
    print("can vote ")
    print("can drive")
elif(age == 18):
    print("should make voter id")
    print("should make licence")
else :
    print("not eligible")
    
