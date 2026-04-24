(n, m) = map(int, input().split())
(s, t, d) = (input(), input(), [0] * (n + 1))
for i in range(m - n + 1):
	C = [j + 1 for j in range(n) if s[j] != t[i + j]]
	if len(C) < len(d):
		d = C
print(len(d))
print(*d)
