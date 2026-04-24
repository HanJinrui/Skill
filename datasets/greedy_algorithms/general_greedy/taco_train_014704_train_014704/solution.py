t = int(input())
for _ in range(t):
	(n, u, d) = map(int, input().split())
	h = list(map(int, input().split()))
	j = 1
	p = 1
	for i in range(1, n):
		if -d <= h[i] - h[i - 1] <= u:
			j += 1
		elif p and h[i] < h[i - 1]:
			p = 0
			j += 1
		else:
			break
	print(j)
