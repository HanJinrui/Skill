(q, x) = [int(i) for i in input().split()]
tree = []

def dfs(i, p, x):
	Z = [[a[i], 1]]
	Y = []
	for j in tree[i]:
		if j != p:
			Y.append(dfs(j, i, x))
	for sub in Y:
		temp = []
		for y in sub:
			for m in Z:
				flag = True
				flag0 = True
				if y[0] == x:
					for o in temp:
						if o[0] == m[0]:
							o[1] += y[1] * m[1]
							flag0 = False
					if flag0:
						temp.append([m[0], y[1] * m[1]])
				for o in temp:
					if o[0] == y[0] ^ m[0]:
						o[1] += y[1] * m[1]
						flag = False
						break
				if flag:
					temp.append([y[0] ^ m[0], y[1] * m[1]])
		Z = temp
	return Z
for _ in range(q):
	tree.append([])
a = [int(i) for i in input().split()]
for i in range(q - 1):
	(u, v) = [int(i) for i in input().split()]
	tree[u - 1].append(v - 1)
	tree[v - 1].append(u - 1)
ans = 0
Z = dfs(0, -1, x)
for m in Z:
	if m[0] == x:
		ans = m[1]
		break
print(ans % (10 ** 9 + 7))
