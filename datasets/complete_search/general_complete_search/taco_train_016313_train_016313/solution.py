n = int(input())
(a, b) = zip(*[map(int, input().split()) for _ in range(n)])
print(sum([b.count(a[i]) <= (a[i] == b[i]) for i in range(n)]))
