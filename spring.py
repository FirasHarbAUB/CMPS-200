import sys

m = int(sys.argv[1])  # Input the 2nd argument in the command line 
d = int(sys.argv[2])  # Input the 3rd argument in the command line

if (m >= 1 and m <= 12) and (d >= 1 and d <= 31):
    if (m == 3 and (d >= 21 and d <= 31)) or (m >= 4 and m <= 5) or (m == 6 and (d >=1 and d <= 20)):
        print(True)
    else:
        print(False)
else:
    print("Error: Value of Month or Day are out of context. Check Inputs.")

    #This is the banda2a of myself
