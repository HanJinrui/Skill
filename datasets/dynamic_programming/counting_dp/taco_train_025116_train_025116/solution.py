(n, k) = map(int, input().split())
c = lambda i: c(i - 1) * (n - i + 1) // i if i else 1
print(sum([1, c(2), 2 * c(3), 9 * c(4)][:k]))
