R = lambda : map(int, input().split())
(n, k) = R()
i = j = r = 0
for x in R():
	if x > n - k:
		r = r * (j - i) % 998244353 or 1
		i = j
	j += 1
print(n * k - k * (k - 1) // 2, r)
