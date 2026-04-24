from itertools import accumulate
from fractions import Fraction
n = int(input())
A = [int(x) for x in input().split()]
A.sort()
B = list(accumulate([0] + A))

def condition(i, z):
	return (2 * z - 1) * (A[i - z] + A[-z]) > 2 * (B[i + 1] - B[i - z + 1] + B[-1] - B[-z])

def average(i, z):
	return Fraction(B[i + 1] - B[i - z] + B[-1] - B[-z - 1], 2 * z + 1)
maxans = 0
argmax = (0, 0)
for i in range(1, n - 1):
	(x, y) = (0, min(i, n - 1 - i))
	while y - x > 1:
		z = (x + y) // 2
		if condition(i, z):
			x = z
		else:
			y = z
	if condition(i, y):
		x = y
	if maxans < average(i, x) - A[i]:
		maxans = average(i, x) - A[i]
		argmax = (i, x)
print(argmax[1] * 2 + 1)
for i in range(argmax[0] - argmax[1], argmax[0] + 1):
	print(A[i], end=' ')
for i in range(-argmax[1], 0):
	print(A[i], end=' ')
