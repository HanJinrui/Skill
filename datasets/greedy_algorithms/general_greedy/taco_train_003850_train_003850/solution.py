n = int(input())
a = [int(x) for x in input().split()]
d = {}
for j in range(n):
	cur_sum = 0
	for i in range(j, -1, -1):
		cur_sum += a[i]
		if cur_sum not in d:
			d[cur_sum] = [(i, j)]
		else:
			(_, prev_j) = d[cur_sum][-1]
			if prev_j < i:
				d[cur_sum].append((i, j))
(mx, mx_key) = (0, 0)
for (key, value) in d.items():
	l = len(value)
	if l > mx:
		mx_key = key
		mx = l
print(mx)
for (i, j) in d[mx_key]:
	print(i + 1, j + 1)
