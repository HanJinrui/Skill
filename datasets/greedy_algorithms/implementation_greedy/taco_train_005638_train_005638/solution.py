for _ in range(int(input())):
	v = int(input())
	m = input().split()
	n = input()
	d = {}
	ans = 'YES'
	for (i, x) in enumerate(m):
		if x not in d:
			d[x] = n[i]
		elif n[i] != d[x]:
			ans = 'NO'
			break
	print(ans)
