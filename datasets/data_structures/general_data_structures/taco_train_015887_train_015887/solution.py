arr = []
for _ in range(int(input())):
	lst = list(map(int, input().split()))
	if lst[0] == 1:
		arr.append(lst[1:])
		continue
	res = [False] * (len(arr) + 1)
	q = [lst[1] - 1]
	while len(q):
		p = q[0]
		q = q[1:]
		for (i, v) in enumerate(arr):
			if (v[0] < arr[p][0] < v[1] or v[0] < arr[p][1] < v[1]) and (not res[i]):
				res[i] = True
				q.append(i)
	print('YES' if res[lst[2] - 1] else 'NO')
