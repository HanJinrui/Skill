(c, d) = list(map(int, input().split()))
(n, m) = list(map(int, input().split()))
k = int(input())
t = max(m * n - k, 0)
p = min(c, n * d)
ans = p * (t // n)
rem = t % n
ans = ans + min(c, rem * d)
print(ans)
