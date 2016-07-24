def has_no_e(word):
	for letter in word:
		if letter.upper() =='E':
			print word
			return True 
	return False


line=raw_input('Input a sentence : ')
word=line.split()
n=len(word)
c=0
flag=True

for i in range(n):
	flag=has_no_e(word[i])
	if flag==False:
		c+=1

print c
#count=float(c)
#length=float(n)

print float(c)/float(n)*100
