def uses(word,allowedlist):
	for letter in word:
		flag=0
		for ltr in allowedlist:
			if letter.upper() == ltr.upper():
				flag=1
		if flag==0:
			return False
	return True	



line=raw_input('Input a sentence : ')
word=line.split()
n=len(word)
allowedlist=raw_input('Enter the allowed list:')

for i in range(n):
	flag1=False
	flag2=False
	flag1=uses(word[i],allowedlist)
	flag2=uses(allowedlist,word[i])
	if flag1==True and flag2==True:
		print word[i]

