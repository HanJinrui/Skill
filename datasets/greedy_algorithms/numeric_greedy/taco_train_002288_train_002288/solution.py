S = input
for _ in [0] * int(S()):
	k = int(S().split()[1])
	t = '0' * k
	print(sum((max(0, len(s) - k) // (k + 1) for s in (t + S() + t).split('1'))))
