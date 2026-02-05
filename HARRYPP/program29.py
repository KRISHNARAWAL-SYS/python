#write a recursive function to calc. the sum of first n natural numbers
'''
sum(1) = 1
sum(2) = sum(1) + 2
sum(3) = sum(2) + 3
sum(n) = sum(n-1) + n

'''




def sum(n):
    if n == 1:
        return 1
    return sum(n-1) + n
print(sum(5))
    