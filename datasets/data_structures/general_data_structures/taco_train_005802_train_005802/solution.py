def query(C, a, b, r):
	S = [0] * 1001
	for c in C[a:b + 1]:
		S[c] += 1
	total = 0
	for (i, s) in enumerate(S):
		total += s
		if total >= r:
			return i
t = int(input().strip())
for _ in range(t):
	n = int(input().strip())
	C = [int(c) for c in input().strip().split(' ')]
	q = int(input().strip())
	for _ in range(q):
		qry = input().strip()
		if qry.startswith('0'):
			(x, y, k) = [int(w) for w in qry.split(' ')[1:]]
			print(query(C, x - 1, y - 1, k))
		elif qry.startswith('1'):
			(x, k) = [int(w) for w in qry.split(' ')[1:]]
			C[x - 1] = k
		else:
			raise ValueError('Invalid query type')
