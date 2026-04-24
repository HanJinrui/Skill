(n, p) = map(int, input().split())
l = []
for i in range(n):
	(a, b) = map(int, input().split())
	l.append((a, b, b / a))
l.sort(key=lambda x: x[2])
(sum_a, sum_b, sumt) = (0, 0, 0)
for i in range(n):
	(a, b, _) = l[i]
	c = 1e+18 if i == n - 1 else l[i + 1][2]
	sum_a += a
	sum_b += b
	dp = sum_a - p
	if dp > 0 and sum_b / dp < c:
		print(sum_b / dp)
		exit()
print(-1)
