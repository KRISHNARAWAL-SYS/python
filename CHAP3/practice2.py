# Write a program to check if a list contains a 
# palindrome of elements.
# eg; [ 1 ,2 ,3 ,2, 1] ,  [1 , "abc" , "abc" , 1]

list1 = [1 , 2 , 1]
list2 = [2 , 2 , 3]

copy_list1 = list1.copy()
list1.reverse()
copy_list2 = list2.copy()
list2.reverse()

if(copy_list1 == list1):
    print('palindrome')
else :
    print("invalid")

if(copy_list2== list2):
    print('palindrome')
else :
    print("invalid")