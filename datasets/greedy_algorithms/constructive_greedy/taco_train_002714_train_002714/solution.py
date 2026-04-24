(n, k) = map(int, input().split())
A = [0] * (k + 1)
(A[::2], A[1::2]) = (range(1, k // 2 + 2), range(k + 1, k // 2 + 1, -1))
print(*A, *range(k + 2, n + 1))
