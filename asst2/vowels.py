import sys

s = sys.argv[1].lower()
vowels = "aeiou"
num_cons = 0

for i in s:
    for y in vowels:
        if y == i:
            num_cons+= 1
            break
print(num_cons)

