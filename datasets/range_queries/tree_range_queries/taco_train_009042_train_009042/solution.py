MOD = 10 ** 9 + 7

def calc_hops(N, A, directed, to_directed, calc, node):
	if calc[node] != -1:
		return calc[node]
	our_a = A[node]
	hops = 0
	for i in directed[node]:
		if A[i] < our_a:
			hops += 1 + calc_hops(N, A, directed, to_directed, calc, i)
	for i in to_directed[node]:
		if A[i] < our_a:
			hops += 1 + calc_hops(N, A, directed, to_directed, calc, i)
	hops %= MOD
	calc[node] = hops
	return hops
for _ in range(int(input())):
	N = int(input())
	P = list(map(int, input().split()))
	A = list(map(int, input().split()))
	directed = [set([i]) for i in range(N)]
	to_directed = [set([i]) for i in range(N)]
	for i in range(N - 1):
		if P[i] - 1 != i:
			break
	else:
		print((pow(2, N, MOD) - 1 - N) % MOD)
		continue
	for i in range(N - 1):
		p = P[i] - 1
		directed[p].add(i + 1)
		to_directed[i + 1].add(p)
		for c in to_directed[p]:
			directed[c].update(directed[i + 1])
		for d in directed[i + 1]:
			to_directed[d].update(to_directed[p])
	calc = [-1 for i in range(N)]
	print(sum([calc_hops(N, A, directed, to_directed, calc, i) for i in range(N)]) % MOD)
