t = int(input())
a = []
for _ in range(t):
	(n, s, r) = map(int, input().split())
	m = s - r
	mas = []
	while s != 0:
		if s >= m:
			mas.extend([m] * (s // m))
			s %= m
		m -= 1
	if n == len(mas):
		a.append(mas)
	else:
		g = n - len(mas)
		while g != 0:
			for i in range(1, len(mas)):
				if mas[i] != 1:
					mas[i] -= 1
					mas.append(1)
					g -= 1
				if g == 0:
					a.append(mas)
					break
print(*[' '.join(map(str, i)) for i in a], sep='\n')
