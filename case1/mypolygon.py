from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
sabru=Turtle()
print bob
print sabru

fd(bob,100)
lt(bob)
rt(sabru)
pu(sabru)
fd(sabru,100)
lt(sabru)
pd(sabru)
fd(sabru,100)
pu(bob)
fd(bob,100)
lt(bob)
pd(bob)
fd(bob,100)
lt(bob)
pu(bob)
pu(sabru)
fd(bob,100)
lt(sabru)
fd(sabru,100)

def polygon(t,n,length):
	pd(t)
	t.delay=0.01
	angle = 360.0/n
	for i in range(n):
		fd(t,length)
		lt(t,angle)

def circle(t,r):
	circumference = 2*math.pi*r
	n=int(circumference/3)+1
	length=circumference/n
	polygon(t,n,length)


polygon(bob,7,70)
circle(sabru,100)
wait_for_user()
