#List Methods

list = [1 , 3, 8 ,8 ,5 ,6]
list2 = [ "a", "f" , 'e' , 'd' , 'g' ,'b' ]

list.append(7)         # append
print(list)

list.sort()         # ascending order
print(list)

list.sort(reverse=True)   #descending order
print(list)
list2.sort(reverse = True)
print(list2)

list2.reverse()
print(list2)

#most imp insert

list.insert(0 , 2)
list2.insert(2,"hello")
print(list2)
print(list)

list3 = [ 2 , 1 , 3 , 1]
list3.remove(1)  #removes fisrt occurance of element
print(list3)

list3.pop(2)  #removes elemet at index 
print(list3) 

