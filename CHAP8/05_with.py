
# f = open("myfile.txt")
# print(f.read())
# f.close()

# now with with statement

with open("myfile.txt") as f:
    print(f.read())