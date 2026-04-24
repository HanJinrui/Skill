for _ in range(int(input())):
	(N, P, Q) = list(map(int, input().split()))
	A = list(map(int, input().split()))
	A.sort()
	z = 0
	for i in A:
		x = min(Q, i // 2)
		y = min(P, i - 2 * x)
		if y + 2 * x >= i:
			P -= y
			Q -= x
			z += 1
	print(z)
