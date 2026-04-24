mod = 10 ** 9 + 7

def find(n):
	if parent[n] < 0:
		return n
	else:
		pt = find(parent[n])
		xor[n] ^= xor[parent[n]]
		parent[n] = pt
		return pt
for _ in range(int(input())):
	(n, q) = map(int, input().split())
	for i in range(n - 1):
		input()
	parent = [-1] * n
	xor = [0] * n
	f = n - 1
	for qq in range(q):
		(i, j, w) = map(int, input().split())
		if f == -1:
			continue
		i -= 1
		j -= 1
		fi = find(i)
		fj = find(j)
		if fi == fj:
			if xor[i] ^ xor[j] ^ w:
				f = -1
		else:
			f -= 1
			if parent[fi] == parent[fj]:
				parent[fi] -= 1
			if parent[fi] > parent[fj]:
				parent[fi] = fj
				xor[fi] = xor[i] ^ xor[j] ^ w
			else:
				parent[fj] = fi
				xor[fj] = xor[i] ^ xor[j] ^ w
	print(pow(2, f, mod)) if f >= 0 else print(0)
