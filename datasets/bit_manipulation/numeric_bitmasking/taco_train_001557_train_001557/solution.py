for i in range(int(input())):
	n = int(input())
	l = list(map(int, input().split()))
	m = max(l)
	m1 = 0
	for i in l:
		m1 |= m ^ i
	print(m, m1)
