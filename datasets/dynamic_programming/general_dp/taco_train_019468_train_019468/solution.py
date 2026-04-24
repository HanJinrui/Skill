def Res(N):
	if N < 10:
		return N
	if N in a:
		return a[N]
	a[N] = max(N, Res(N // 2) + Res(N // 3) + Res(N // 4))
	return a[N]
a = {}
while True:
	try:
		print(Res(int(input())))
	except:
		break
