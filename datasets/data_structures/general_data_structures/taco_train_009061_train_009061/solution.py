import math
import os
import random
import re

class Point:

	def __init__(self, newx=0, newy=0):
		self.x = newx
		self.y = newy

	def distance(self, other):
		d = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
		return d

	def is_inside(self, c):
		return self.distance(c.center) <= c.radius

	def __str__(self):
		return f'({self.x}, {self.y})'

class Circle:

	def __init__(self, c=Point(), r=0):
		self.center = c
		self.radius = r

	def is_valid(self, P):
		for p in P:
			if not p.is_inside(self):
				return False
		return True

def collinear(A, B, C):
	return abs((A.y - B.y) * (A.x - C.x) - (A.y - C.y) * (A.x - B.x)) <= 1e-09

def get_circle_center(A, B, C):
	bx = B.x - A.x
	by = B.y - A.y
	cx = C.x - A.x
	cy = C.y - A.y
	b = bx ** 2 + by ** 2
	c = cx ** 2 + cy ** 2
	d = bx * cy - by * cx
	if d == 0:
		print('div by zero')
	return Point((cy * b - by * c) / (2 * d), (bx * c - cx * b) / (2 * d))

def circle_from_2points(A, B):
	C = Point((A.x + B.x) / 2.0, (A.y + B.y) / 2.0)
	return Circle(C, A.distance(B) / 2.0)

def circle_from_3points(A, B, C):
	I = get_circle_center(A, B, C)
	I.x += A.x
	I.y += A.y
	return Circle(I, A.distance(I))

def min_circle_trivial(R):
	if len(R) == 0:
		return Circle()
	elif len(R) == 1:
		return Circle(R[0], 0)
	elif len(R) == 2:
		return circle_from_2points(R[0], R[1])
	c = circle_from_2points(R[0], R[1])
	if c.is_valid(P):
		return c
	c = circle_from_2points(R[0], R[2])
	if c.is_valid(P):
		return c
	c = circle_from_2points(R[1], R[2])
	if c.is_valid(P):
		return c
	return circle_from_3points(R[0], R[1], R[2])

def find_MEC(P, R, n):
	if n == 0 or len(R) == 3:
		return min_circle_trivial(R)
	ridx = random.randint(0, n - 1)
	rndm_p = P[ridx]
	(P[ridx], P[n - 1]) = (P[n - 1], P[ridx])
	d = find_MEC(P, R.copy(), n - 1)
	if rndm_p.is_inside(d):
		return d
	R.append(rndm_p)
	return find_MEC(P, R.copy(), n - 1)
nm = input()
N = eval(nm.split()[0])
M = eval(nm.split()[1])
A = [0, 0]
A[0] = [0] + list(map(int, input().split()))
A[1] = [0] + list(map(int, input().split()))
for _ in range(M):
	q = list(map(int, input().split()))
	qtype = q[0]
	if qtype == 1:
		(id, l, r) = q[1:]
		A[id][l:r + 1] = reversed(A[id][l:r + 1])
	elif qtype == 2:
		(id, l1, r1, l2, r2) = q[1:]
		A[id] = A[id][0:l1] + A[id][l2:r2 + 1] + A[id][r1 + 1:l2] + A[id][l1:r1 + 1] + A[id][r2 + 1:]
	elif qtype == 3:
		(l, r) = q[1:]
		temp = A[0][l:r + 1]
		A[0][l:r + 1] = A[1][l:r + 1]
		A[1][l:r + 1] = temp
	elif qtype == 4:
		(l, r) = q[1:]
		P = []
		for i in range(l, r + 1):
			p = Point(A[0][i], A[1][i])
			P.append(p)
		c = find_MEC(P, R=[], n=len(P))
		print(f'{c.radius:.2f}')
