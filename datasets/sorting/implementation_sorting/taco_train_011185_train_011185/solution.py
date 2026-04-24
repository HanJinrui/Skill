n = int(input())
m = sorted(map(int, input().split()))
d = [m[i] - m[i - 1] for i in range(1, n)]
a = min(d)
print(a, d.count(a))
