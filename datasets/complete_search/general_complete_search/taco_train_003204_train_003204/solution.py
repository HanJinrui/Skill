(n, b) = map(int, input().split())
a = list(map(int, input().split()))
print(max((b // a[i] * a[j] + b % a[i] for j in range(n) for i in range(j + 1))))
