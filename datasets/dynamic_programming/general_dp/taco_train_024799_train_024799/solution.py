for _ in range(int(input())):
	n = int(input())
	b = list(map(int, input().split()))
	assert n == len(b)
	s = [0, 0]
	for i in range(1, n):
		s = [b[i - 1] - 1 + s[1], max(b[i] - 1 + s[0], b[i - 1] - b[i] + s[1])]
	print(max(s))
