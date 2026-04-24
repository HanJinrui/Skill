N = int(input())
A = [(int(i), s if n >= N // 2 else '-') for (i, s, n) in (input().split() + [n] for n in range(N))]
print(*(s for (i, s) in sorted(A, key=lambda x: x[0])))
