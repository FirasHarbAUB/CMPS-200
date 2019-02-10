s = input("Input a word...\n").lower()
s_rev = s[::-1]

if s == s_rev:
    print(s, "is a palindrome!")
else:
    print(s, "is not a palindrome.")