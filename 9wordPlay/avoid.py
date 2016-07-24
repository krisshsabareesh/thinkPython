def avoid(word,forbidden):
	for letter in word:
		if letter.upper() ==forbidden.upper():
			return False
	print word
	return True

line=raw_input('Input a sentence : ')
word=line.split()
n=len(word)
forbidden=raw_input('Enter the forbidden letter:')

for i in range(n):
	avoid(word[i],forbidden)
