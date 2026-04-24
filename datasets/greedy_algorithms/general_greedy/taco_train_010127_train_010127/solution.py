for T in range(int(input())):
	(M, N) = map(int, input().split())
	h = [(int(i), 0) for i in input().split()] + [(int(i), 1) for i in input().split()]
	(mod, p, ans) = (1000000007, [1, 1], 0)
	for i in sorted(h, reverse=True):
		ans = (ans + i[0] * p[1 - i[1]] % mod) % mod
		p[i[1]] += 1
	print(ans)
