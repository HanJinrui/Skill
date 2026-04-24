n = int(input())
a = list(map(int, input().split()))
print(max(max(a), (sum(a) + n - 2) // (n - 1)))
