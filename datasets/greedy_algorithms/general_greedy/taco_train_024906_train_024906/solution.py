T = int(input())
for k in range(T):
	(N, K) = map(int, input().split())
	t = {}
	for i in range(N):
		(s, f, p) = map(int, input().split())
		try:
			t[p].append((f, s))
		except:
			t[p] = [(f, s)]
	c = 0
	for i in t:
		t[i].sort()
		start = -1
		for j in t[i]:
			if j[1] >= start:
				c += 1
				start = j[0]
	print(c)
