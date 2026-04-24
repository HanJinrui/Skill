from collections import Counter
(n, p, k) = map(int, input().split())
c = Counter(((pow(v, 4, p) - k * v) % p for v in map(int, input().split())))
print(sum((v * (v - 1) // 2 for v in c.values())))
