s = 'spam'
t = list(s)
print t

s = 'pining for the fjorsd'
t = s.split()
print t

s = 'pin-ing fo-r t-he fj- or-sd'
delimiter = '-'
print s.split(delimiter)

print delimiter.join(t)
