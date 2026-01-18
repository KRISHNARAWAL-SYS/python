#                Set method  
# set is mutable
# but elemts of set is immutable


#1.
collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("krishna")
collection.add((1 , 4, 2,))

#2.
collection.remove(1)
print(collection)
print(len(collection))

#3.
#collection.clear() # will empty the set

#4.
print(collection.pop())
print(collection.pop())  #pop up any random value.

#5.
set2 = {1 , 2, 3, 3}
print(collection.union(set2))

#6.
set3 = {2 , 3 ,5 , 6}
print(set3.intersection(set2))






