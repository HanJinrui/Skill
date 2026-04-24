for _ in range(int(input())):
	n = int(input())
	up = int(1e+18)
	mat = [input() for i in range(n)]
	(a, c, answer) = (10 * [0], 10 * [0], 10 * [0])
	(b, d) = (10 * [up], 10 * [up])
	for i in range(n):
		for j in range(n):
			digit = int(mat[i][j])
			a[digit] = max(a[digit], i)
			b[digit] = min(b[digit], i)
			c[digit] = max(c[digit], j)
			d[digit] = min(d[digit], j)
	for i in range(n):
		for j in range(n):
			digit = int(mat[i][j])
			answer[digit] = max(answer[digit], max(max(i, n - i - 1) * max(j - d[digit], c[digit] - j), max(j, n - j - 1) * max(i - b[digit], a[digit] - i)))
	print(*answer)
