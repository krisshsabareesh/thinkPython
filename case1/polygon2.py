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

def polyline(t,n,length,angle):
	for i in range(n):
		fd(t,length)
		lt(t,angle)


def polygon(t,n,length):
	t.delay=0.01
	angle = 360.0/n
	polyline(t,n,length,angle)

def arc(t,r,angle):
	arc_length=2*math.pi*r*angle/360
	n=int(arc_length/3)+1
	step_length=arc_length/n
	step_angle=float(angle)/n
	polyline(t,n,step_length,step_angle)

def circle(t,r):
	arc(t,r,360)

pd(sabru)
pd(bob)
polygon(bob,7,70)
circle(sabru,100)
arc(bob,100,360)
wait_for_user()
