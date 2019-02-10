number = int(input("Enter a number... "))
n = int(input("Enter a desired position... "))

def nth_digit(number, n):
    number = number    
    n = n
    if n >= 0 and n <= len(str(number)):
        if n == 0:
            return number % 10
        else:
            return int((number % (10 ** (n+1)))/(10 ** (n)))
    else:
        print("Index Error.. Out of bounds.")
print(nth_digit(number, n))