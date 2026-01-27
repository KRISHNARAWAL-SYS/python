#write a program to greet all the person name stored ina list 'l' and which starts with 'S'
l = ["harry" , "soham" , "Sachin" , "rahul"]

for name in l:
    if(name.startswith("S")):
        print(f"hello {name} ,good evening")