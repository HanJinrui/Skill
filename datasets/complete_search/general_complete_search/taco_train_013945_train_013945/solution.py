t = int(input())
for _ in range(t):
	n = int(input())
	v = list(map(int, input().split()))
	ans = [1 for i in range(n)]
	for i in range(n):
		minimum = min(v[i:])
		maximum = max(v[:i + 1])
		for j in range(i):
			if v[j] > minimum:
				ans[i] += 1
		for j in range(i + 1, n):
			if v[j] < maximum:
				ans[i] += 1
	print(min(ans), max(ans))
