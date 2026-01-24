#  write a program to create a dictionary of hindi words with values as their english translation.

Translate ={
    "namaste" : "hello",
    "billi" : "cat",
    "kutta" : "dog",
    "aag" : "fire"
}

word = input(" enter the hindi word : ")

print("the english translation of the hindi word is :",Translate[word])
print("the english translation of the hindi word is :",Translate.get(word))
print("the english translation of the hindi word is :",Translate.get(word,"not found"))  # if word not found in dictionary then it will print not found