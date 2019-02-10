import sys 

s = sys.argv[1].lower()      #Input any word
consonants =  "bcdfghjklmnpqrstvwxyz"
num_cons = 0

for i in s:
    for y in consonants:
        if y == i:
            num_cons+= 1
            break
print(num_cons)
        


