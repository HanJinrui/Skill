for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	a.sort()
	s = sum(a)
	p = 0
	m = 0
	for i in a:
		s -= i
		p += 1000 - i
		m = max(m, s * p)
	print(m)
