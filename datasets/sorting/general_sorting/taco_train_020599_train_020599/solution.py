t = int(input())
for _ in range(t):
	(n, k, x) = map(int, input().split())
	s = list(map(int, input().split()))
	ul = min(s) + x
	ll = ul - n
	ssm = ul * (ul + 1) // 2 - ll * (ll + 1) // 2
	s.sort()
	ll += 1
	for i in s:
		if i < ll:
			ssm -= ll - i
			ll += 1
	print(ssm)
