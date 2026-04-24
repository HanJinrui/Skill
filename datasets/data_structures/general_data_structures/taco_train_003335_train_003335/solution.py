(n, k) = map(int, input().split())
if k << 1 > n:
	k = n - k
s = 1
for i in range(n):
	s += 1 + i * k // n + (i * k + k - 1) // n
	print(s)
