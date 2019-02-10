c = input("Enter one letter... ")

def is_vowel(c):	#Prints True if letter is a vowels else prints False
	c = c
	exp = (c=='A' or c=='a' or c=='E' or c=='e' or c=='I'
 or c=='i' or c=='O' or c=='o' or c=='U' or c=='u')
	print(exp)

is_vowel(c)