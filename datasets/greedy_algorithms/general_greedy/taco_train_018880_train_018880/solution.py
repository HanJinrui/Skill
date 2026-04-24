for _ in range(int(input())):
	n = int(input())
	l = list(map(int, input().split()))
	pos = [0 for i in range(n)]
	for i in range(n):
		pos[l[i]] = i
	l = pos[0]
	r = pos[0]
	ans = 0
	for i in range(1, n):
		cu = pos[i]
		if cu >= l and cu <= r:
			ans += r - l - i
		elif cu < l:
			l = cu
		else:
			r = cu
	print(ans)
