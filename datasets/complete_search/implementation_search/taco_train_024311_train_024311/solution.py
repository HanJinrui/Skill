n = int(input())
A = list(map(int, input().split()))
print('Yes' if all(((A[i] - A[0] * (-1) ** i) % n == i for i in range(n))) else 'No')
