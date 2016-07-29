
fin = open('words.txt')
text = {}
x = 1

for line in fin:
	words = line.strip()
	text[words] = x
	x = x+1

checker = raw_input('Enter a word to check whether it is in dictionary: ')
print checker in text
