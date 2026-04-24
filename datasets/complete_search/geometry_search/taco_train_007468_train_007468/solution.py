A = list(map(int, input().split()))
print(max(max(A) * 2 - sum(A) + 1, 0))
