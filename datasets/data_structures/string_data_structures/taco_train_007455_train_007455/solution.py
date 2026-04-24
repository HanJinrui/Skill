t = int(input())
for I in range(t):
	n = int(input())
	l = list(input())
	k = sorted(l)
	for i in range(n):
		if l[i] != k[i] and l[i] != k[n - i - 1]:
			print('NO')
			break
	else:
		print('YES')
