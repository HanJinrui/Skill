I = lambda : map(int, input().split())
(_, k) = I()
A = list(I())
print(min(A) if k < 2 else max(A) if k > 2 else max(A[0], A[-1]))
