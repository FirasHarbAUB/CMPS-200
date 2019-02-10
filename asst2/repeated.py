s = input("Input a word...\n").lower()

def repeated(s, sub):
	sum_sub = 0
	for i in range(len(s)):
		if s.startswith(sub, i):
			sum_sub += 1
	print("Number of times 'aaa' occurs is:", sum_sub)

repeated(s, "aaa")    