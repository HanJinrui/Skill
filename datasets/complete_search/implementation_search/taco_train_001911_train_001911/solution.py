n = int(input())
A = list(map(int, input().split()))
print(2 * min((abs(180 - sum(A[i:j])) for i in range(n) for j in range(i, n))))
