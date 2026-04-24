R = lambda : map(int, input().split())
(n, k) = R()
a = iter(sorted(set(R())))
p = 0
while k:
	x = next(a, p)
	print(x - p)
	p = x
	k -= 1
