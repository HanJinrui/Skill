n = int(input())
l = [-1, 0, -1, 1]
u = (n // 4 << 1) + l[n % 4]
print(u, n - u)
