for i in range(int(input())):
	n = int(input())
	p = list(map(int, input().split()))
	c = list(map(int, input().split()))
	p = [x - 1 for x in p]
	used = [0] * n
	ret = n
	for j in range(n):
		if used[j] == 0:
			cycle = []
			v = j
			while used[v] == 0:
				used[v] = 1
				cycle.append(v)
				v = p[v]
			l = len(cycle)
			for k in range(1, l + 1):
				if l % k == 0:
					for s in range(k):
						eq = True
						pos = s
						while pos + k < l:
							if c[cycle[pos]] != c[cycle[pos + k]]:
								eq = False
							pos += k
						if eq:
							ret = min(ret, k)
							break
	print(ret)
