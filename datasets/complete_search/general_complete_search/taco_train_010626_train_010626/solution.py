t = int(input())
for _ in range(t):
	m = int(input())
	input()
	s = {}
	for (i, v) in enumerate(input().split()):
		v = int(v)
		if m - v in s:
			print(s[m - v], i + 1)
			break
		else:
			s[v] = i + 1
