R = lambda : map(int, input().split())
(n, k) = R()
a = list(range(0, 257))
v = [1] * 257
for p in R():
	if v[p]:
		t = p
		while t >= 0 and p - a[t] <= k - 1:
			t -= 1
		t += 1
		for i in range(t, p + 1):
			a[i] = a[t]
			v[i] = 0
	print(a[p], end=' ')
