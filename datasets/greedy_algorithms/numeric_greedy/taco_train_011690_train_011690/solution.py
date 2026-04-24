(n, m) = input().split()
a = [0] + list(map(float, input().split()))
ans = 0
for _ in range(int(m)):
	(u, v, c) = input().split()
	ans = max(ans, (a[int(u)] + a[int(v)]) / float(c))
print(ans)
