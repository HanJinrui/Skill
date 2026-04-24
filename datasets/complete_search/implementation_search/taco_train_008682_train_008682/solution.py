n = int(input())
a = [int(c) for c in input().split()]
tot = sum(a)
b = [i + 1 for (i, c) in enumerate(a) if c * n == tot]
print(len(b))
print(*b)
