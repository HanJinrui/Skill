n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(0, n - 1, 2):
	k = 1
	s = 0
	for j in range(i + 1, n, 2):
		ans += max(0, min(a[i], a[j] + s) - max(k, s) + 1)
		if j + 2 < n:
			s += a[j]
			k = max(k, s)
			s -= a[j + 1]
print(ans)
