for test in range(int(input())):
	(n, k) = map(int, input().split())
	a = [0] * 30
	for A in input().split():
		A = int(A)
		for i in range(30):
			if 1 << i & A:
				a[i] += 1 << i
	ans = 0
	for i in sorted(list(range(30)), key=lambda i: (-a[i], i))[:k]:
		ans |= 1 << i
	print(ans)
