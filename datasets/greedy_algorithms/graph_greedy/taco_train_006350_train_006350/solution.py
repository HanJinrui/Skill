import collections
import math
import sys

def main():
	n = int(input())
	a = list(map(int, input().split()))
	cnt = collections.Counter(a)
	mx = max(cnt.values())
	a = zip(a, range(n))
	a = sorted(a, key=lambda x: x[0])
	b = a[mx:] + a[:mx]
	res = [0] * n
	for (i, x) in enumerate(a):
		res[x[1]] = b[i][0]
	print(*res)
t = int(input())
while t > 0:
	main()
	t -= 1
