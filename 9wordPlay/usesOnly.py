def avoid(word,allowedlist):
	for letter in word:
		flag=0
		for ltr in allowedlist:
			if letter.upper() == ltr.upper():
				flag=1
		if flag==0:
			return False	
	print word



line=raw_input('Input a sentence : ')
word=line.split()
n=len(word)
allowedlist=raw_input('Enter the allowed list:')

for i in range(n):
	avoid(word[i],allowedlist)
