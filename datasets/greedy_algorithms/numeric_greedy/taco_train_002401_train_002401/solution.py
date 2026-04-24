(n, m) = map(int, input().split())
matr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(m):
	cost = list(range(n, 2 * n))
	for j in range(n):
		matr[j][i] -= i + 1
		if matr[j][i] % m == 0:
			matr[j][i] //= m
			if 0 <= matr[j][i] < n:
				shift = (j + n - matr[j][i]) % n
				cost[shift] -= 1
	ans += min(cost)
print(ans)
