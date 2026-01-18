#Dictionaries Methods

student = {
    "name" : "Krishna Rawal",
    "subject" :{
        "phy" : 87,
        "chem" : 83,
        "math"  : 94,
        }
}

#1.
print(student.keys())
print(list(student.keys()))  #to print keys in list

#2.
print(student.values())

#3.
print(student.items())

#4.
print(student.get("name"))
print(student["name"])
#same

#here is the difference
#print(student.get("name2")) # error
#print(student["name2"])     # ---> none

#5.
new_dict = {"city" : "delhi" , "state" : "rajs" }
student.update(new_dict)
print(student)
# in case of same key it will overwrite the previous key
