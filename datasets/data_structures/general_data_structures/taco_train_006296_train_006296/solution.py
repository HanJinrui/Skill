import bisect
t = int(input())
for _ in range(t):
	n = int(input())
	a = map(int, input().split())
	w = map(int, input().split())
	maw = [(0, 0)]
	nmaw = 1
	for (ai, wi) in zip(a, w):
		j1 = bisect.bisect_left(maw, (ai, 0))
		(aj, wj) = maw[j1 - 1]
		aw = awi = (ai, wi + wj)
		while j1 < len(maw) and maw[j1][1] <= wi + wj:
			del maw[j1]
		if j1 >= len(maw) or maw[j1][0] > ai:
			maw.insert(j1, (ai, wi + wj))
	print(max((wi for (ai, wi) in maw)))
