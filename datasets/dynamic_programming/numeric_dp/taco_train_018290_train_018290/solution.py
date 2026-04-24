n = 10 ** 5 + 1
l = [0] * n
for i in range(2, n):
	if l[i] == 0:
		for j in range(i, n, i):
			l[j] += 1
x = [0]
for k in range(1, 6):
	m = [0] * n
	for i in range(2, n):
		if l[i] == k:
			m[i] += 1
		m[i] += m[i - 1]
	x.append(m)
t = int(input())
while t > 0:
	(a, b, k) = map(int, input().split())
	ans = x[k][b] - x[k][a - 1]
	print(ans)
	t -= 1
