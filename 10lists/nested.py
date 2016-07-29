t = [[1, 2], [3, 4]]
t1 = [1, 2, 4]
print sum(t1)
total = 0
for a in t:
	#print sum(a)
	total += sum(a)

print total

t = ['a', 'b', 'c', 'd']

res = []
for s in t:
	res.append(s.capitalize())
print res

t.pop(1)
print t
t.pop()
print t

del t[1]
print t

t.remove('a')
print t 
