for _ in range(int(input())):
	n = int(input())
	l = [0] * 32
	d = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
	for i in range(n):
		s = list(set(list(input())))
		m = 0
		for j in s:
			m |= d[j]
		l[m] += 1
	ans = l[31] * (l[31] - 1) // 2
	for i in range(1, 32):
		for j in range(i + 1, 32):
			if i | j == 31:
				ans += l[i] * l[j]
	print(ans)
