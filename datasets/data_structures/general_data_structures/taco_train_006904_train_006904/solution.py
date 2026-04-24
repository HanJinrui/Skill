for ti in range(int(input())):
	(n, k, p) = map(int, input().split())
	ays = list(map(int, input().split()))[:n]
	if k % 2 == 1:
		if p == 0:
			print(max(ays))
		else:
			print(min(ays))
	else:
		shu = ays[1:] + [ays[-2]]
		shd = [ays[1]] + ays[:n - 1]
		if p == 0:
			print(max((min(s) for s in zip(shu, shd))))
		else:
			print(min((max(s) for s in zip(shu, shd))))
