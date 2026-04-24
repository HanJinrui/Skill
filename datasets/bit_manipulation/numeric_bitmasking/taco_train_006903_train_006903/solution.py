import math
for _ in range(int(input())):
	(l, r) = map(int, input().split())
	ans = 0
	for i in range(60):
		if l & 1 << i > 0:
			pr = min((1 << i) - (l & (1 << i) - 1), r - l + 1)
			ans += pr * (1 << i)
	print(ans % (10 ** 9 + 7))
