t = int(input())
for i in range(t):
	n = int(input())
	l = list(map(int, input().split()))
	a = l[0]
	b = l[0]
	for x in range(1, n):
		n = max(a, b)
		b = a + x * l[x] + l[x - 1]
		a = n + (x + 1) * l[x]
	print(max(a, b))
