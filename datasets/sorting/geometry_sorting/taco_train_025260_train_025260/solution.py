import math
import functools
import sys

def eulen(x, y):
	r = functools.reduce(lambda x, y: x + y, map(lambda x: (x[0] - x[1]) ** 2, zip(x, y)))
	return math.sqrt(r)

def output(t, p):
	print('YES')
	print(t)
	print(' '.join(map(str, p)))
n = int(input())
points = []
for i in range(n + 1):
	points.append(tuple(map(int, input().split())))
(vp, vs) = map(int, input().split())
(x, y, z) = map(int, input().split())
curTime = 0
for i in range(n):
	endTime = curTime + eulen(points[i], points[i + 1]) / vs
	lies_in = lambda p, t: (x - p[0]) ** 2 + (y - p[1]) ** 2 + (z - p[2]) ** 2 <= (t * vp) ** 2 + 1e-07
	if lies_in(points[i + 1], endTime):
		if lies_in(points[i], curTime):
			output(curTime, points[i])
			sys.exit(0)
		(left, right) = (0, endTime - curTime + 1e-08)
		fc = eulen(points[i], points[i + 1])
		answer = None
		for j in range(100):
			mid = (left + right) / 2.0
			endPoint = tuple(map(lambda x: x[0] + (x[1] - x[0]) / fc * mid * vs, zip(points[i], points[i + 1])))
			if lies_in(endPoint, curTime + mid):
				answer = endPoint
				right = mid
			else:
				left = mid
		output(curTime + right, answer)
		sys.exit(0)
	curTime = endTime
print('NO')
