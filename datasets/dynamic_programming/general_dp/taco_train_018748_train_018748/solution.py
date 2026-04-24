import sys
M = 10 ** 9 + 7
mb = 201

def solve(ss):
	A = ss
	t = [[(0, 1)]]
	for x in A:
		f = [[] for _ in range(mb)]
		for (tb, b) in zip(t, range(mb)):
			if tb:
				tb.sort(reverse=True)
				(c, k) = (0, 0)
				for d in range(min(tb[0][0], b + x), -1, -1):
					while k < len(tb) and tb[k][0] >= d:
						(c, k) = ((c + tb[k][1]) % M, k + 1)
					f[d].append((b + x - d, c))
		t = f
	return str(sum(map(lambda v: sum(map(lambda x: x[1], v)), t)))
for t in range(int(input())):
	n = int(input())
	A = list(map(int, input('').split())) + [0] * 15
	print(solve(A))
