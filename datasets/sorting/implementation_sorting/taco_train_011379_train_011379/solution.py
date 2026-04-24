I = lambda : map(int, input().split())
(n, k) = I()
A = sorted((tuple(I()) for _ in range(n)), key=lambda x: (-x[0], x[1]))
print(A.count(A[k - 1]))
