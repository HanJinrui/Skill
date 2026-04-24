from math import *

def leftCandies(n, m):
	x = m % (n * (n + 1) // 2)
	a = (sqrt(8 * x + 1) - 1) // 2
	b = a * (a + 1) // 2
	return int(x - b)
