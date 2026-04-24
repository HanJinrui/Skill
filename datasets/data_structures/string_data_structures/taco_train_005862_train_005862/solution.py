for _ in range(int(input())):
	n = int(input())
	s = 1
	v = 1
	ans = 'draw'
	f = 1
	for i in range(n):
		a = input().strip()
		if a.endswith('man'):
			s += 1
		else:
			v += 1
		if s - v >= 2 and f:
			ans = 'superheroes'
			f = 0
		elif v - s >= 3 and f:
			ans = 'villains'
			f = 0
	print(ans)
