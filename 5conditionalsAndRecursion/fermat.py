import math

def pow(a,n):
	p=1
	for i in range(n):
		p=a*p
	return(p)

def ln(x,base):
	count=-1
	while x>0:
		x/=base
		count+=1
		if x==0:
			return count

def check_fermat(a,b,n):
	an=pow(a,n)
	bn=pow(b,n)
	cn=an+bn
	print cn		
	c=ln(cn,3)
	print c
	bc=int(c)
	print bc
	if(c%bc==0):
		print 'Holy Smokes, Fermat was wrong'
	else:
		print 'Yes, it does not work'

a=2
b=1
n=3
check_fermat(a,b,n)

x=2.34
y=int(x)
print x
print y

