n = int(input())
t = [int(input()) for q in range(n)]
for i in range(1, 501):
	for j in range(i, 2 * i + 1):
		s = [i, j, 4 * i - j, 3 * i]
		for k in t:
			if k not in s:
				break
			s.remove(k)
		else:
			print('YES')
			for q in s:
				print(q)
			exit()
print('NO')
