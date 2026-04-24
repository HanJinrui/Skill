n = int(input())
A = list(map(int, input().split()))
print('NO' if any((A[i] > A[i + 1] < A[i + 2] for i in range(n - 2))) else 'YES')
