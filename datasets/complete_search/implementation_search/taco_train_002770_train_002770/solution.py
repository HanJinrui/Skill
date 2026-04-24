(n, s) = map(int, input().split())
r = -1
while n:
	(x, y) = map(int, input().split())
	if x * 100 + y <= s * 100:
		r = max(r, (100 - y) % 100)
	n -= 1
print(r)
