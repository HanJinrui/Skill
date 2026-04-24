from math import factorial
for t in range(int(input())):
	(n, k) = map(int, input().split())
	l = list(map(int, input().split()))
	l.sort()
	q = l[:k]
	a = q.count(q[-1])
	b = l.count(q[-1])
	print(factorial(b) // (factorial(a) * factorial(b - a)))
