import sys

s = int(sys.argv[1])

for i in range(s,0,-1):
    f = ((s - i) * " '" + i * ' *')
    print(f)
