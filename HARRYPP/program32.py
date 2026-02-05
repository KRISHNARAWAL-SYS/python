 #write a python program to strip a given word from list
 
def rem(l,word):
    n = []
    for item in l :
        if not(item == word):
            n.append(item.strip(word))
    return n

l = [ "krishan" , " rohan" , "an ", "ansakshy"]  
print(rem(l , "an"))     