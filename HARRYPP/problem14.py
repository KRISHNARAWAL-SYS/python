# write a program to check whether a given post is talking about about krishna or not

post = " hey i am krishna bhai , what about you diyanshu"

if ("Krishna" in post):
    print("Yes, the post is talking about krishna.")
else:
    print("No, the post is not talking about krishna.")
    
# to avoid case sensitivity
post = post.lower()
if ("Krishna".lower() in post):
    print("Yes, the post is talking about krishna.")
else:
    print("No, the post is not talking about krishna.")