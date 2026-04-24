for _ in range(int(input())):
	N = int(input())
	s = input()
	d = {}
	max_k = 0
	for i in range(N):
		if s[i] in d:
			max_k = max(max_k, N + d[s[i]] - i)
		d[s[i]] = i
	print(max_k)
