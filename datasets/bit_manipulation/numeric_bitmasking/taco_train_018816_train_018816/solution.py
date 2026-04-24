R = lambda : map(int, input().split())
(t,) = R()
while t:
	t -= 1
	(n, x, y) = R()
	print('ABloibc e'[x + y + sum(R()) & 1::2])
