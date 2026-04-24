t = int(input())
while t:
	n = int(input())
	l = list(map(int, input().split()))
	r = list(map(int, input().split()))
	m = []
	for i in range(n):
		m.append(l[i] + r[i])
	print(m.index(max(m)) + 1)
	t -= 1
