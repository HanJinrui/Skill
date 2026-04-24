I = lambda : map(int, input().split())
(n, *_) = I()
A = list(I())
B = list(I())
for j in range(n):
	print(*(min(A[i], B[j]) if h else 0 for (i, h) in enumerate(I())))
