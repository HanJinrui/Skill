(n, k) = map(int, input().split())
c = list(map(int, input().split()))
l = 2 * k + 1
res = 10 ** 16
for i in range(k + 1):
	j = i
	a = 0
	while j < n:
		a += c[j]
		j += l
	if j - l + k + 1 >= n:
		res = min(res, a)
print(res)
