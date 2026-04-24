for _ in '.' * int(input()):
	n = int(input())
	(s, t) = (input(), input())
	ans = 0
	l = False
	for i in range(n - 1, -1, -1):
		if s[i] < t[i]:
			l = True
		elif s[i] > t[i]:
			l = False
		ans += l
	print(ans)
