#!/usr/bin/env python
import math
class fireFly:
	def __init__(self, info):
		self.x = int(info[0])
		self.y = int(info[1])
		self.z = int(info[2])
		self.vx = int(info[3])
		self.vy = int(info[4])
		self.vz = int(info[5])
		
class point:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	def __add__(self, other):
		return point(self.x + other.x, self.y + other.y, self.z + other.z)
	def __sub__(self, other):
		return point(self.x - other.x, self.y - other.y, self.z - other.z)
	def __mul__(self, other):
		return point(self.x * other.x, self.y * other.y, self.z * other.z)
	def __div__(self,other):
		if other.x == 0:
			tX = 0
		else:
			tX = self.x / other.x
		if other.y == 0:
			tY = 0
		else:
			tY = self.y / other.y
		if other.z == 0:
			tZ = 0
		else:
			tZ = self.z / other.z

		return point(tX, tY, tZ)
	def __pow__(self, p):
		return point(self.x ** p, self.y ** p, self.z ** p)

def center(fireFlies, t):
	N = len(fireFlies)
	x = y = z = 0
	for f in fireFlies:
		x += f.x + (t * f.vx)
		y += f.y + (t * f.vy)
		z += f.z + (t * f.vz)

	return point(x/N,y/N,z/N)

def dist(x, y, z):
	return Math.sqrt(x**2 + y**2 + z**2)

def getClosestPoint(A, B, P = point(0,0,0)):
	AP = P - A
	AB = B - A

	print
	print "A", A.x, A.y, A.z
	print "B", B.x, B.y, B.z
	print "AB:", AB.x, AB.y, AB.z
	ab2 = AB**2
	ap_ab = AP*AB
	t = ap_ab / ab2
	return A + AB * t
	'''
Vector GetClosetPoint(Vector A, Vector B, Vector P, bool segmentClamp)
{
    Vector AP = P - A:
    Vector AB = B - A;
    float ab2 = AB.x*AB.x + AB.y*AB.y;
    float ap_ab = AP.x*AB.x + AP.y*AB.y;
    float t = ap_ab / ab2;
    if (segmentClamp)
    {
         if (t < 0.0f) t = 0.0f;
         else if (t > 1.0f) t = 1.0f;
    }
    Vector Closest = A + AB * t;
    return Closest;
}
	'''
numLines = int(raw_input())

for z in range(numLines):
	#number of fireflies
	N = int(raw_input())
	fireFlies = []
	for i in range(N):
		line = raw_input().split()
		fireFlies.append(fireFly(line))
	
	#time at 0
	p0 = center(fireFlies,0)
	#time at 1
	p1 = center(fireFlies,100)
	#time at 2
	p2 = center(fireFlies,2)
	print "p2",p2.x, p2.y, p2.z
	print
	centerPoint = getClosestPoint(p0, p1) 	
	print "centerPoint:", centerPoint.x, centerPoint.y, centerPoint.z

	#print "Case #" + str(z+1) + ":", dMin, tMin
