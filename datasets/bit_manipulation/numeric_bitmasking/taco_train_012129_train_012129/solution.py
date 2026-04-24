for _ in range(int(input())):
	n = int(input())
	b = list(map(int, input().split()))
	p = list(map(float, input().split()))
	x = 0
	for i in range(30):
		pb = 0.0
		for j in range(n):
			if b[j] & 1 << i:
				pb = pb * (1 - p[j]) + (1 - pb) * p[j]
		x += (1 << i) * pb
	print(x)
