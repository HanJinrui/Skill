(n, m, q) = map(int, input().split())
(s, t) = (input(), input())
a = [0, 0]
b = 0
for i in range(n):
	b += s[i:i + m] == t
	a += [b]
for _ in [0] * q:
	(l, r) = map(int, input().split())
	print(a[max(l, r - m + 2)] - a[l])
