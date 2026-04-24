n = int(input())
A = list(map(int, input().split()))
A.sort()
print(sum(A[1::2]) - sum(A[0::2]))
