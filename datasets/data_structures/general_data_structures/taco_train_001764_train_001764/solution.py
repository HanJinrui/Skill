def implementOps(n, ops):
	arr = [0] * n
	res = []
	for op in ops:
		z = op[0]
		if z == 'U':
			(x, y, a, b) = list(map(int, op[1:]))
			t = a ** b + (a + 1) ** b + (b + 1) ** a
			if int(x) > int(y):
				for i in range(y):
					arr[i] += t
			else:
				for i in range(x, len(arr)):
					arr[i] += t
		else:
			(x, y, m) = list(map(int, op[1:]))
			if int(x) > int(y):
				res.append(sum(arr[:y]) % m)
			else:
				res.append(sum(arr[x:]) % m)
	return res
n = int(input())
edges = []
for i in range(n - 1):
	edges.append(list(map(int, input().split())))
q = int(input())
ops = []
for i in range(q):
	ops.append(input().split())
res = implementOps(n, ops)
for v in res:
	print(v)
