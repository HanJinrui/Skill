for i in range(int(input())):
	n = int(input())
	x = {}
	for i in range(n):
		(s, a) = input().split()
		a = int(a)
		if a not in x.keys():
			x[a] = s
		else:
			x[a] = '-1'
	ans = 'Nobody wins.'
	m = 200000000001
	for i in x.keys():
		if i < m and x[i] != '-1':
			ans = x[i]
			m = i
	print(ans)
