for i in range(0,13):
    power = 2 ** i 

    if len(str(power)) == 1:
        print("0" + str(power))
    else:
        print(power % 100)
   