for _ in range(int(input())):
	n = int(input())
	f3 = []
	for _ in range(n):
		x = input()
		f3.append(x[:n // 2].count('1') - x[n // 2:].count('1'))
	s = sum(f3)
	m = abs(s)
	for i in f3:
		m = min(m, abs(s - 2 * i))
	print(m)
