for _ in range(int(input())):
	N = int(input())
	(p, q) = (1, N - 1)
	for i in range(N):
		t = p
		l = q
		for j in range(N):
			if i + j > l:
				t += l
				l -= 1
			else:
				t += i + j
			print(t, end=' ')
		print()
		p += i + 1
