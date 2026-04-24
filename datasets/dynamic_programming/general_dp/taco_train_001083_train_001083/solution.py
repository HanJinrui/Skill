def bb(a):
	if len(a) < 2:
		return 0
	s = sum(a)
	x = 0
	for i in range(len(a) - 1):
		x += a[i]
		if x == s / 2:
			return 1 + max(bb(a[:i + 1]), bb(a[i + 1:]))
	return 0
for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	if sum(a) == 0:
		print(n - 1)
	else:
		print(bb(a))
