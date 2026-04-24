for _ in range(int(input())):
	n = int(input())
	a = [int(x) for x in input().split()]
	assert len(a) == n
	assert all((x > 0 for x in a))
	sm = sum(a)
	if sm % 2 != 0:
		print(-1)
		continue
	ps_sm = {0: []}
	for (i, x) in enumerate(a):
		ps_sm_new = ps_sm.copy()
		for (v, indices) in ps_sm.items():
			if v + x not in ps_sm_new:
				ps_sm_new[v + x] = indices + [i]
		ps_sm = ps_sm_new
	if sm // 2 not in ps_sm:
		print(-1)
		continue
	indices_1 = ps_sm[sm // 2]
	indices_2 = [i for i in range(len(a)) if i not in indices_1]
	vals_1 = [[a[i], i] for i in indices_1]
	vals_2 = [[a[i], i] for i in indices_2]
	ops = []
	while len(vals_1) != 0:
		ops.append([vals_1[0][1], vals_2[0][1]])
		min_v = min(vals_1[0][0], vals_2[0][0])
		vals_1[0][0] -= min_v
		vals_2[0][0] -= min_v
		if vals_1[0][0] == 0:
			del vals_1[0]
		if vals_2[0][0] == 0:
			del vals_2[0]
	assert len(vals_2) == 0
	print(len(ops))
	for (x, y) in ops:
		print(x + 1, y + 1)
