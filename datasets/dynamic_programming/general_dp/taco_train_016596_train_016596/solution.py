from functools import lru_cache
(N, K) = map(int, input().split())
costs = [list(map(int, input().split())) for _ in range(K)]

@lru_cache(None)
def get_best(n, mask):
	if n == 0:
		return 0
	best = 1000000000000
	for i in range(K):
		if mask >> i & 1 == 1:
			n_mask = mask ^ 1 << i
			for j in range(n):
				best = min(best, get_best(j, n_mask) + sum(costs[i][j:n]))
	return best
print(get_best(N, 2 ** K - 1))
