(n, k) = map(int, input().split())
(i, j) = (1, 2)
while n >= i and k > 0:
	print((str(n - i) + ' ') * max(0, n - j) + ' '.join(map(str, range(max(i + 1, n - i + 1), n + 1))) + (' ' + str(n)) * i)
	(i, j, k) = (j, 2 * j, k - 1)
for i in range(k):
	print((str(n) + ' ') * n)
