def answer():
	(ans, x) = (0, 0)
	d = dict()
	d[x] = -1
	for i in range(n):
		x ^= 1 << a[i] - 1
		if x not in d.keys():
			d[x] = i
		for j in range(30):
			ans = max(ans, i - d.get(x ^ 1 << j, i))
	return ans // 2
for T in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	print(answer())
