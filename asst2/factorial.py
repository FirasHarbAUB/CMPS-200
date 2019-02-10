s = int(input("Enter an odd number between 1 and 10... "))

def factorial(n):
    if (s >= 1 and s < 10) and (s % 2 != 0):
        if n == 1:
            return 1
        else:
            return n * factorial(n-1)
print(factorial(s))