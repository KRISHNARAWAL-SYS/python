f = open("poem.txt", "r")
content = f.read
if ("twinkle" in content):
    print("twinkle is present the content")
else:
    print("not present")
    


f.close
 