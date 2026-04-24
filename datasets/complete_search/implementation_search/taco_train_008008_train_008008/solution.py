(n, t, k, d) = map(int, input().split())
print('YES' if (d // t + 1) * k < n else 'NO')
