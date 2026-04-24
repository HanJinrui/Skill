n = int(input())
a = list(map(int, input().split()))
m = 1000000007
s = 0
a.sort()
for i in range(n):
	s = (s + a[i] * (pow(2, i, m) - pow(2, n - 1 - i, m))) % m
print(s)
