R = lambda : map(int, input().split())
(h, a, c) = R()
(g, b) = R()
k = (g + a - 1) // a
n = max(b * (k - 1) - h, -1) // (c - b) + 1
print(str(n + k) + '\nHEAL' * n + '\nSTRIKE' * k)
