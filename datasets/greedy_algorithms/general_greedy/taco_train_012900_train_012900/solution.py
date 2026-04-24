t = int(input())
for i in range(t):
	(n, s) = map(int, input().split())
	c = list(map(int, input().split()))
	p = list(map(int, input().split()))
	d = 100
	f = 100
	for i in range(n):
		if p[i] == 0:
			d = min(d, c[i])
		else:
			f = min(f, c[i])
	print('yes' if s + d + f <= 100 else 'no')
