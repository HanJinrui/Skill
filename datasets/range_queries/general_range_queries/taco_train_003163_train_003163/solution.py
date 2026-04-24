def solve(arr, b, c, n):
	b[0] = c[0] = -float('inf')
	mps = 0
	s = 0
	for i in range(n):
		s += arr[i]
		b[i + 1] = max(b[i], s - mps)
		c[i + 1] = max(c[i], s)
		mps = min(mps, s)
	return (b, c)
for tc in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	(b1, c1) = solve(arr, [0] * (n + 1), [0] * (n + 1), n)
	arr.reverse()
	(b2, c2) = solve(arr, [0] * (n + 1), [0] * (n + 1), n)
	for i in range(n):
		ans = max(b1[i], b2[n - i], c1[i] + c2[n - i])
		print(ans, end=' ')
