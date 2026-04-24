for _ in range(int(input())):
	(n, m) = map(int, input().split())
	v = []
	for i in range(n):
		v += list(map(int, input().split()))
	v.sort(reverse=True)
	sc = sum(v[::2])
	sg = sum(v[1::2])
	if sc == sg:
		print('Draw')
	elif sc > sg:
		print('Cyborg')
	else:
		print('Geno')
