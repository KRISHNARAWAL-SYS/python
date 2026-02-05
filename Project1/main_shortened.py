import random     #importing random module to generate random number for computer choice

computer = random.choice([-1,0,1])
youstr = input("enter your choice :")
youDict = {"s":1,"w":-1,"g":0}
reverseDict = {1:"snake",-1:"water",0:"gun"}
you = youDict[youstr]

print(f"you chose {reverseDict[you]}")
print(f"computer chose {reverseDict[computer]}")

if(computer == you):
    print("tie")
else:
    if((computer - you )== -2) or ((computer - you )== 1):
        print("you win")
    else:
        print("you lose")