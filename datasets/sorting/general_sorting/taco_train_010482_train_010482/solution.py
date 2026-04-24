for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	v = list(zip(a, b))
	v.sort(key=lambda x: -x[0] / x[1])
	s = 0
	sm = 0
	for e in v:
		sm += s * e[1]
		s += e[0]
	print(sm)
