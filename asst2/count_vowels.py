c = input("Enter one Word... ").lower()

def count_vowels(string):    #Prints the number of vowels in a string
	vowels = "aeiou"
	num_cons = 0
	for i in c:
		for y in vowels:
			if y == i:
				num_cons+= 1
				break
	print("The number of vowels in", c, "is:", num_cons)
count_vowels("word")