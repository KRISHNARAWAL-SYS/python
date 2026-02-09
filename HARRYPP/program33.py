st = '''twinkle twinkle litte star
how i wonder what u are
up above the world so high 
like a diamond in the sky'''
f = open("poem1.txt", "w")
f.write(st)

content = f.read
if ("twinkle" in content):
    print("twinkle is present the content")
else:
    print("not present")
    


f.close
 