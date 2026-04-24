t = int(input())
while t > 0:
	n = int(input())
	l = list(map(int, input().split()))
	m = 0
	for i in range(n):
		m = max(m, l[i] + l[i - 1])
	print(m)
	t = t - 1
