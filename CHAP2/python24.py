#String Function
str = "i am a coder. \n and i am also a student \n work at jecrc college\n I am pursueing Btech in IT\n "
#1.
a = str.endswith("er.\n") #returns true if string ends with substr
#2.
b = str.capitalize("")  #capitalize 1st char
#3.
c = str.replace("am", "are") #replaces all occurances of old
#4.
d = str.find("coder") # returns 1st index of  1st occurrer
#5.
e = str.count("am") #counts the occurrence of substr

print(str)

print(a)
print(b)
print(c)
print(d)
print(e)
