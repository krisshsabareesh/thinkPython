def has_no_e(word):
	for letter in word:
		if letter.upper() =='E':
			return False
	print word
	return True

line=raw_input('Input a sentence : ')
word=line.split()
n=len(word)
for i in range(n):
	has_no_e(word[i])
