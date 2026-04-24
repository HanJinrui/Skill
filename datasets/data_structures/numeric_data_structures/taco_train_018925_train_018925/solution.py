t = int(input())
while t > 0:
	(n, m, k) = map(int, input().split())
	a = set(map(int, input().split()))
	b = set(map(int, input().split()))
	c = a & b
	d = a | b
	print(len(c), n - len(d))
	t = t - 1
