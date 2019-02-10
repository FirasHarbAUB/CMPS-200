s = input("Enter a word... ").lower()

string_lengh = 0
string_start = False
max_lengh = 0

for letter in s:
    if letter == "a":
        string_start = True
        string_lengh = 1
    elif letter == "z":
        string_lengh += 1
        string_start = False
    else:
        if string_start == True:
            string_lengh += 1
        else:
            string_lengh = 0
    if string_lengh > max_lengh:
        max_lengh = string_lengh
print("The longest substring found has length:", max_lengh)




