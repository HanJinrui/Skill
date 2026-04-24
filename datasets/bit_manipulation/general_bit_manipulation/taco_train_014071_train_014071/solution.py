for T in range(int(input())):
	(n, A) = (int(input()), list(map(int, input().split())))
	if n & 1:
		A.append(0)
	if len(A) < 4:
		A = [0, 1] + A
	C = A[:-4]
	if A[-3] > 1:
		C.extend([A[-4], A[-3] - 1, 1])
	else:
		C.extend([A[-4] + 1])
	C.append(A[-1] + 1)
	if A[-2] > 1:
		C.append(A[-2] - 1)
	print(len(C))
	print(' '.join(map(str, C)))
