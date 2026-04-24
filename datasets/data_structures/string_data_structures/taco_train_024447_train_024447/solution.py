for _ in range(int(input())):
	(n, k) = map(int, input().split())
	s = input()
	sm = 0
	for i in range(1, n):
		if s[i] != s[i - 1]:
			sm += min(i, k, n - k, n - i)
	print(sm)
