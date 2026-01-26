s = set()
s.add(18)
s.add("18")
s.add(18.0)

print(len(s)) # it will print 2 because 18 and 18.0 are considered the same in a set