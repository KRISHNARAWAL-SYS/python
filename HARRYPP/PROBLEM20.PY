#FACTORIAL

N = int(input("Enter a number to find its factorial: "))

factorial = 1
for i in range(1, N + 1):
    factorial *= i
print("Factorial of", N, "is", factorial)
