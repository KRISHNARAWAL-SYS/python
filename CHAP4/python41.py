#Dictionaries
#mutable

data = {
    "name" :'Krishna rawal',
    "subjects" : ["python" , "C" , "R"],
    "topic" : ("dict" , "set"),
    "age" : 20,
    "is_adult " : True,
    "marks" : 95.6
}
print(data)
print(data["name"])
data["name"] = "stpaul"
print(data["name"])
print(data['age'])
data["age"]